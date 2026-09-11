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


def run_friday_simulation(spec: dict[str, Any]) -> dict[str, Any]:
    friday_dates = fridays(spec)
    scenarios = spec["scenarios"]
    outcomes: Counter[str] = Counter()
    brunch_interruptions = 0
    scrums_created = 0

    for friday in friday_dates:
        if friday.weekday() != 4:
            raise CertificationFailure(f"Non-Friday entered Friday simulation: {friday.isoformat()}")
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


def command_certify(spec: dict[str, Any], check: bool) -> None:
    protocol_text = render_protocol(spec)
    update_file(PROTOCOL_PATH, protocol_text, check)
    update_file(EVIDENCE_PATH, evidence_text(spec, protocol_text), check)
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
        elif args.command == "certify":
            command_certify(spec, args.check)
    except (CertificationFailure, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"❌ Certification failure: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
