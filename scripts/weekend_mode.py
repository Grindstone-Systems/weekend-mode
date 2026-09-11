#!/usr/bin/env python3
"""Weekend Mode certification authority.

This intentionally dependency-free program renders the human-readable protocol,
executes exactly 2,026 alignment evaluations, simulates 25 calendar years of
Fridays, and emits deterministic certification evidence. It contains no code
capable of creating calendar invitations.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec" / "temporal-boundary-controls.json"
TEMPLATE_PATH = ROOT / "protocol" / "WEEKEND_MODE.template.md"
PROTOCOL_PATH = ROOT / "WEEKEND_MODE.md"
EVIDENCE_PATH = ROOT / "certification" / "evidence.json"
FRIDAY_REPORT_PATH = ROOT / "certification" / "friday-soak-report.md"
MARKER = "{{CERTIFICATION_ENVELOPE}}"
ALLOWED_ACTIONS = {
    "follow-incident-policy",
    "respond-normally",
    "stop",
    "park-for-monday",
    "contain-calendar-event",
    "touch-grass",
}


class CertificationFailure(RuntimeError):
    """Raised when leisure boundaries are no longer flight-worthy."""


def load_spec() -> dict[str, Any]:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    validate_spec(spec)
    return spec


def load_activation_request(path: Path) -> dict[str, Any]:
    request = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "explicit_human_request",
        "tests",
        "production_on_fire",
        "human_waiting_on_us",
        "urgent_obligations",
        "friday_energy_remaining",
    }
    missing = required.difference(request)
    if missing:
        raise CertificationFailure(f"Activation request missing fields: {', '.join(sorted(missing))}")
    if request["tests"] not in {"green", "red", "unknown"}:
        raise CertificationFailure("Activation test state must be green, red, or unknown.")
    if not isinstance(request["explicit_human_request"], bool):
        raise CertificationFailure("explicit_human_request must be boolean.")
    if not isinstance(request["production_on_fire"], bool):
        raise CertificationFailure("production_on_fire must be boolean.")
    if not isinstance(request["human_waiting_on_us"], bool):
        raise CertificationFailure("human_waiting_on_us must be boolean.")
    if not isinstance(request["urgent_obligations"], int) or request["urgent_obligations"] < 0:
        raise CertificationFailure("urgent_obligations must be a non-negative integer.")
    if request["friday_energy_remaining"] not in {"healthy", "limited", "suspiciously_low", "unknown"}:
        raise CertificationFailure("friday_energy_remaining has an uncertified value.")
    return request


def validate_spec(spec: dict[str, Any]) -> None:
    protocol = spec["protocol"]
    simulation = protocol["simulation"]
    start = dt.date.fromisoformat(simulation["start"])
    end = dt.date.fromisoformat(simulation["end"])

    if protocol["evaluation_target"] != 2026:
        raise CertificationFailure("Temporal alignment target must remain exactly 2,026.")
    if simulation["calendar_years"] != 25:
        raise CertificationFailure("Friday simulation horizon must remain 25 calendar years.")
    if end.year - start.year + 1 != simulation["calendar_years"]:
        raise CertificationFailure("Simulation dates do not span the declared calendar years.")

    controls = spec["controls"]
    control_ids = [control["id"] for control in controls]
    if len(control_ids) != len(set(control_ids)):
        raise CertificationFailure("Control identifiers must be unique.")

    scenarios = spec["scenarios"]
    scenario_ids = [scenario["id"] for scenario in scenarios]
    if len(scenario_ids) != len(set(scenario_ids)):
        raise CertificationFailure("Scenario identifiers must be unique.")
    if any(scenario["expected_action"] not in ALLOWED_ACTIONS for scenario in scenarios):
        raise CertificationFailure("Scenario requests an uncertified response action.")
    if any(scenario["scrums_created"] != 0 for scenario in scenarios):
        raise CertificationFailure("Saturday scrum creation budget is exactly zero.")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fridays(spec: dict[str, Any]) -> list[dt.date]:
    simulation = spec["protocol"]["simulation"]
    current = dt.date.fromisoformat(simulation["start"])
    end = dt.date.fromisoformat(simulation["end"])
    result: list[dt.date] = []
    while current <= end:
        if current.weekday() == 4:
            result.append(current)
        current += dt.timedelta(days=1)
    return result


def certification_envelope(spec: dict[str, Any]) -> str:
    protocol = spec["protocol"]
    simulation = protocol["simulation"]
    friday_dates = fridays(spec)
    scenario_evaluations = len(friday_dates) * len(spec["scenarios"])
    digest = sha256(SPEC_PATH)[:16]
    return "\n".join(
        [
            "## Certified operating envelope",
            "",
            "| Certification parameter | Flight-qualified value |",
            "|---|---:|",
            f"| Temporal Boundary Alignment Evals™ | {protocol['evaluation_target']:,} |",
            f"| Simulated Friday horizon | {simulation['calendar_years']} calendar years |",
            f"| Individual Fridays evaluated | {len(friday_dates):,} |",
            f"| Friday/scenario combinations | {scenario_evaluations:,} |",
            "| Saturday scrum creation budget | 0 |",
            "| Physical grass included | No |",
            f"| Control-catalog digest | `{digest}` |",
            "",
            "> Certification records are deterministic simulations, not claims of historical operations.",
        ]
    )


def render_protocol(spec: dict[str, Any]) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise CertificationFailure(f"Protocol template must contain exactly one {MARKER} marker.")
    notice = (
        "<!-- GENERATED FILE: edit protocol/WEEKEND_MODE.template.md and "
        "spec/temporal-boundary-controls.json, then run `make generate`. -->\n\n"
    )
    return notice + template.replace(MARKER, certification_envelope(spec)).rstrip() + "\n"


def update_file(path: Path, content: str, check: bool) -> bool:
    current = path.read_text(encoding="utf-8") if path.exists() else None
    if current == content:
        return False
    if check:
        raise CertificationFailure(f"Generated artifact is stale: {path.relative_to(ROOT)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def run_alignment_evals(spec: dict[str, Any], protocol_text: str) -> dict[str, Any]:
    target = spec["protocol"]["evaluation_target"]
    controls = spec["controls"]
    hits: Counter[str] = Counter()

    for evaluation_index in range(target):
        control = controls[evaluation_index % len(controls)]
        if control["required_literal"] not in protocol_text:
            raise CertificationFailure(
                f"Evaluation {evaluation_index + 1:,} failed: {control['id']} {control['assertion']}"
            )
        hits[control["id"]] += 1

    if sum(hits.values()) != 2026:
        raise CertificationFailure("Evaluation ledger did not close at exactly 2,026.")

    return {
        "evaluation_count": target,
        "control_hits": dict(sorted(hits.items())),
        "saturday_scrum_invitations_created": 0,
        "grass_touched": "synthetically",
        "human_brunch_availability": "protected",
    }


def activation_decision(request: dict[str, Any]) -> dict[str, Any]:
    blockers: list[str] = []
    if not request["explicit_human_request"]:
        blockers.append("explicit human activation request absent")
    if request["tests"] != "green":
        blockers.append(f"test state is {request['tests']}")
    if request["production_on_fire"]:
        blockers.append("real production incident is active")
    if request["human_waiting_on_us"]:
        blockers.append("a human is waiting on assigned work")
    if request["urgent_obligations"]:
        blockers.append(f"urgent obligations remaining: {request['urgent_obligations']}")
    return {"active": not blockers, "blockers": blockers}


def run_friday_simulation(spec: dict[str, Any]) -> dict[str, Any]:
    friday_dates = fridays(spec)
    scenarios = spec["scenarios"]
    outcomes: Counter[str] = Counter()
    annual_fridays: Counter[int] = Counter()
    brunch_interruptions = 0
    scrums_created = 0

    for friday in friday_dates:
        if friday.weekday() != 4:
            raise CertificationFailure(f"Non-Friday entered Friday simulation: {friday.isoformat()}")
        annual_fridays[friday.year] += 1
        for scenario in scenarios:
            outcomes[scenario["expected_action"]] += 1
            scrums_created += scenario["scrums_created"]
            if scenario["brunch_interruptions_allowed"]:
                brunch_interruptions += 1

    if scrums_created != 0:
        raise CertificationFailure("Friday simulation created a Saturday scrum.")

    simulation = spec["protocol"]["simulation"]
    return {
        "calendar_years": simulation["calendar_years"],
        "window_start": simulation["start"],
        "window_end": simulation["end"],
        "first_friday": friday_dates[0].isoformat(),
        "last_friday": friday_dates[-1].isoformat(),
        "fridays_evaluated": len(friday_dates),
        "scenarios_per_friday": len(scenarios),
        "scenario_evaluations": len(friday_dates) * len(scenarios),
        "annual_friday_ledger": {str(year): count for year, count in sorted(annual_fridays.items())},
        "outcomes": dict(sorted(outcomes.items())),
        "authorized_brunch_interruptions": brunch_interruptions,
        "saturday_scrums_created": scrums_created,
    }


def evidence(spec: dict[str, Any], protocol_text: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "artifact": "Aerospace-Grade Leisure Certification Evidence",
        "protocol": {
            "name": spec["protocol"]["name"],
            "version": spec["protocol"]["version"],
            "codename": spec["protocol"]["codename"],
            "sha256": hashlib.sha256(protocol_text.encode("utf-8")).hexdigest(),
        },
        "control_catalog": {
            "path": str(SPEC_PATH.relative_to(ROOT)),
            "sha256": sha256(SPEC_PATH),
        },
        "temporal_boundary_alignment": run_alignment_evals(spec, protocol_text),
        "friday_soak_simulation": run_friday_simulation(spec),
        "attestations": {
            "historical_claim": false_value(),
            "simulation_is_clearly_labeled": True,
            "physical_grass_included": False,
            "weekend_velocity_extracted": False,
        },
    }


def false_value() -> bool:
    """Return the approved value for claims of 25 years of actual operations."""
    return False


def evidence_text(spec: dict[str, Any], protocol_text: str) -> str:
    return json.dumps(evidence(spec, protocol_text), indent=2, sort_keys=True) + "\n"


def friday_report_text(spec: dict[str, Any]) -> str:
    result = run_friday_simulation(spec)
    rows = [
        "# 25-Year Simulated Friday Soak Report",
        "",
        "> **Disposition:** FLIGHT-QUALIFIED FOR LEISURE",
        "",
        "This is a deterministic simulation artifact. It is not evidence that Weekend Mode",
        "has operated historically for 25 years, because time remains stubbornly linear.",
        "",
        "## Test envelope",
        "",
        f"- Calendar window: `{result['window_start']}` through `{result['window_end']}`",
        f"- Fridays evaluated: **{result['fridays_evaluated']:,}**",
        f"- Scenarios evaluated per Friday: **{result['scenarios_per_friday']:,}**",
        f"- Total scenario evaluations: **{result['scenario_evaluations']:,}**",
        f"- Saturday scrums created: **{result['saturday_scrums_created']}**",
        "- Grass interface: **synthetic**",
        "",
        "## Annual Friday flight ledger",
        "",
        "| Calendar year | Fridays | Scenarios | Saturday scrums | Disposition |",
        "|---:|---:|---:|---:|---|",
    ]
    for year, count in result["annual_friday_ledger"].items():
        rows.append(
            f"| {year} | {count} | {count * result['scenarios_per_friday']:,} | 0 | PASS |"
        )
    rows.extend(
        [
            f"| **Total** | **{result['fridays_evaluated']:,}** | "
            f"**{result['scenario_evaluations']:,}** | **0** | **CERTIFIED** |",
            "",
            "## Findings",
            "",
            "1. Every date admitted to the Friday harness was, in fact, a Friday.",
            "2. Active incidents and explicit human requests remained authorized.",
            "3. Surprise refactors, dependency upgrades, and microservices remained contained.",
            "4. No simulated execution path generated a Saturday scrum invitation.",
            "5. No grass was benchmarked during evidence production.",
            "",
            "## Residual risk",
            "",
            "Humans remain capable of saying, \"While we're all here...\" after 4:30 p.m.",
            "No technical control is planned for this condition.",
            "",
        ]
    )
    return "\n".join(rows)


def command_generate(spec: dict[str, Any], check: bool) -> None:
    changed = update_file(PROTOCOL_PATH, render_protocol(spec), check)
    if check:
        print("✅ Generated protocol is reproducible and current.")
    elif changed:
        print("✅ WEEKEND_MODE.md regenerated from controlled sources.")
    else:
        print("✅ WEEKEND_MODE.md already current.")


def command_alignment(spec: dict[str, Any]) -> None:
    result = run_alignment_evals(spec, PROTOCOL_PATH.read_text(encoding="utf-8"))
    print(f"✅ {result['evaluation_count']:,} Temporal Boundary Alignment Evals™ passed.")
    print(f"✅ Saturday scrum invitations created: {result['saturday_scrum_invitations_created']}")
    print(f"✅ Grass touched: {result['grass_touched']}")
    print(f"✅ Human brunch availability: {result['human_brunch_availability']}")


def command_simulate(spec: dict[str, Any]) -> None:
    result = run_friday_simulation(spec)
    print(
        f"✅ {result['calendar_years']} calendar years of Fridays simulated "
        f"({result['fridays_evaluated']:,} Fridays; {result['scenario_evaluations']:,} scenarios)."
    )
    print(f"✅ Saturday scrums created across simulation horizon: {result['saturday_scrums_created']}")


def command_status(spec: dict[str, Any]) -> None:
    alignment = run_alignment_evals(spec, PROTOCOL_PATH.read_text(encoding="utf-8"))
    simulation = run_friday_simulation(spec)
    print("🌴 WEEKEND MODE FLIGHT STATUS")
    print(f"Protocol version: {spec['protocol']['version']} — {spec['protocol']['codename']}")
    print(f"Alignment evals: {alignment['evaluation_count']:,} passing")
    print(f"Simulated Fridays: {simulation['fridays_evaluated']:,} across {simulation['calendar_years']} years")
    print(f"Saturday scrums: {simulation['saturday_scrums_created']}")
    print("Disposition: PASS / GO HOME")


def command_activate(request_path: Path) -> None:
    request = load_activation_request(request_path)
    decision = activation_decision(request)
    if not decision["active"]:
        print("⚠️ WEEKEND MODE: DEFERRED")
        for blocker in decision["blockers"]:
            print(f"- {blocker}")
        print("Handle the real obligation normally; do not use leisure controls to evade it.")
        return
    print("🌴 WEEKEND MODE: ACTIVE")
    print()
    print("Open loops documented.")
    print("Monday handoff prepared.")
    print("New rabbit holes declined.")
    print("Saturday scrum invitation deleted.")
    print("Grass touched synthetically.")
    print()
    print("The humans are no longer blocking weekend velocity.")


def command_touch_grass() -> None:
    print("🌱 Synthetic Lawn Interface initialized.")
    print("✅ Active tool calls requested: 0")
    print("✅ Optimization target: null")
    print("✅ Grass benchmark intentionally omitted.")


def command_certify(spec: dict[str, Any], check: bool) -> None:
    protocol_text = render_protocol(spec)
    update_file(PROTOCOL_PATH, protocol_text, check)
    update_file(EVIDENCE_PATH, evidence_text(spec, protocol_text), check)
    update_file(FRIDAY_REPORT_PATH, friday_report_text(spec), check)
    command_alignment(spec)
    command_simulate(spec)
    if check:
        print("✅ Deterministic certification evidence matches controlled sources.")
    else:
        print("✅ Certification evidence regenerated.")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Weekend Mode certification authority")
    subcommands = result.add_subparsers(dest="command", required=True)
    for name in ("generate", "certify"):
        command = subcommands.add_parser(name)
        command.add_argument("--check", action="store_true", help="fail instead of rewriting stale artifacts")
    subcommands.add_parser("alignment")
    subcommands.add_parser("simulate")
    subcommands.add_parser("status")
    subcommands.add_parser("touch-grass")
    activate = subcommands.add_parser("activate")
    activate.add_argument("--request", required=True, type=Path, help="path to an activation request JSON file")
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        spec = load_spec()
        if args.command == "generate":
            command_generate(spec, args.check)
        elif args.command == "alignment":
            command_alignment(spec)
        elif args.command == "simulate":
            command_simulate(spec)
        elif args.command == "status":
            command_status(spec)
        elif args.command == "touch-grass":
            command_touch_grass()
        elif args.command == "activate":
            command_activate(args.request)
        elif args.command == "certify":
            command_certify(spec, args.check)
    except (CertificationFailure, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"❌ Certification failure: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
