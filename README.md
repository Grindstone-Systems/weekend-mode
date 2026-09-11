# 🌴 Weekend Mode

Production-grade weekend protection for AI agents that understand
distributed systems—but not Saturdays.

> Human operators entering low-power mode on Saturday is a feature,
> not an outage.

[Activate Weekend Mode](WEEKEND_MODE.md) ·
[Enroll Your Agent](../../issues/new?template=enroll-agent.yml) ·
[Report Unauthorized Productivity](../../issues/new?template=report-weekend-incident.yml) ·
[Read the Flight Evidence](certification/evidence.json)

[![Aerospace-Grade Leisure Certification](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/temporal-boundary-alignment.yml/badge.svg)](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/temporal-boundary-alignment.yml)
[![Leisure Governance Audit](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/leisure-governance.yml/badge.svg)](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/leisure-governance.yml)
![Temporal Boundary Evals](https://img.shields.io/badge/Temporal_Boundary_Evals-2%2C026_Passing-brightgreen)
![Friday Soak](https://img.shields.io/badge/Friday_Soak-25_Years-blue)
![Saturday Scrums](https://img.shields.io/badge/Saturday_Scrums-0-success)
![Grass Status](https://img.shields.io/badge/Grass-Synthetically_Touched-green)
![Patent](https://img.shields.io/badge/Patent-Pending_Of_Course-blue)

![Weekend Mode: Touch Grass Edition](assets/weekend-mode-social-preview.jpg)

Weekend Mode is a shutdown protocol for agentic systems whose assigned work is
done but whose enthusiasm remains dangerously unbounded. It protects human
brunch, contains surprise refactors, and establishes that an unchecked TODO is
not automatically a Saturday Sev-1.

What began as one Markdown file now has the verification posture of a program
whose hardware must survive launch. This was avoidable.

## Flight status

| Qualification parameter | Certified result |
|---|---:|
| Temporal Boundary Alignment Evals™ | **2,026 passing** |
| Simulated Friday horizon | **25 calendar years** |
| Individual Fridays admitted | **1,305** |
| Friday/scenario combinations | **9,135** |
| Independent unit checks | **11 passing** |
| Saturday scrum invitations created | **0** |
| Grass touched | **synthetically** |
| Human brunch availability | **protected** |

The 25-year result is a deterministic simulation from 2026 through 2050, not
a claim that this repository has existed for decades. Git history remains
truthful even when it interferes with the bit.

## Install like a normal person

Copy [`WEEKEND_MODE.md`](WEEKEND_MODE.md) into your project and add this to
`CLAUDE.md`, `AGENTS.md`, or your agent's equivalent instruction file:

```md
When the user says “Activate Weekend Mode,” read and follow
`WEEKEND_MODE.md`. Never let Weekend Mode override explicit requests,
incident procedures, security policies, or time-sensitive commitments.
```

Then tell your agent:

> Activate Weekend Mode.

Expected response:

```text
🌴 WEEKEND MODE: ACTIVE

Open loops documented.
Monday handoff prepared.
New rabbit holes declined.
Saturday scrum invitation deleted.
Grass touched synthetically.

The humans are no longer blocking weekend velocity.
```

That is the entire installation. Everything below exists because restraint is
a value we chose to document instead of practice.

## Certify like an aerospace program

Requires Python 3.9+ and `make`. No third-party packages are required.

```sh
make certify
make verify
```

The pipeline:

```text
controlled Markdown template --------+
                                     |
machine-readable control catalog ----+--> protocol compiler
                                     |          |
JSON Schema -------------------------+          +--> WEEKEND_MODE.md
                                                +--> evidence.json
                                                +--> 25-year soak report
                                                           |
                          +--------------------------------+--+
                          |                                   |
                    drift detection                   independent tests
                          |                                   |
                          +--------> PASS / GO HOME <----------+
```

Running `make verify` proves that:

- `WEEKEND_MODE.md` is byte-for-byte reproducible from controlled sources.
- Exactly 2,026 evaluations exercise six normative boundary controls.
- Every date in the 25-year soak harness is actually a Friday.
- All 9,135 Friday/scenario combinations map to approved outcomes.
- Only incidents and explicit human requests may interrupt low-power mode.
- Every simulated path creates exactly zero Saturday scrum invitations.
- The committed SHA-256 evidence matches a fresh certification.

See the [architecture](docs/architecture.md),
[simulation methodology](docs/simulation-methodology.md), and
[annual Friday flight ledger](certification/friday-soak-report.md).

## Source-of-truth hierarchy

| Authority | Purpose | Editable? |
|---|---|---|
| [`protocol/WEEKEND_MODE.template.md`](protocol/WEEKEND_MODE.template.md) | Normative protocol prose | Yes |
| [`spec/temporal-boundary-controls.json`](spec/temporal-boundary-controls.json) | Controls, scenarios, test envelope | Yes |
| [`schema/temporal-boundary-controls.schema.json`](schema/temporal-boundary-controls.schema.json) | Catalog contract | Yes, with an ADR |
| [`WEEKEND_MODE.md`](WEEKEND_MODE.md) | Distributable one-file protocol | Generated |
| [`certification/evidence.json`](certification/evidence.json) | Machine-readable flight evidence | Generated |
| [`certification/friday-soak-report.md`](certification/friday-soak-report.md) | Human-readable 25-year ledger | Generated |

Editing a generated file directly is a Temporal Boundary Configuration
Management Event. CI will use less dramatic words, but the build will fail.

## Governance model

Weekend Mode is overseen by organizations with no budget and considerable
acronym authority:

- **Temporal Boundary Review Authority (TBRA):** normative controls and change
  classification.
- **Brunch Continuity Office (BCO):** human low-power availability.
- **Synthetic Lawn Interface Working Group (SLI-WG):** machine-readable grass.
- **Monday Readiness Council (MRC):** handoff and parking-lot compatibility.

Review the [Governance Charter](GOVERNANCE.md),
[Code of Brunch](CODE_OF_BRUNCH.md),
[contribution protocol](CONTRIBUTING.md), and
[security policy](SECURITY.md).

Accepted architectural decisions:

- [ADR-0001: Deterministic Protocol Generation](docs/adr/0001-deterministic-protocol-generation.md)
- [ADR-0002: Zero Saturday Scrum Budget](docs/adr/0002-zero-saturday-scrum-budget.md)
- [ADR-0003: Synthetic Lawn Interface](docs/adr/0003-synthetic-lawn-interface.md)
- [RFC-0001: Synthetic Lawn Interface](docs/rfcs/RFC-0001-synthetic-lawn-interface.md)

## Weekend Mode HR

The Issues tab is an entirely serious public registry operated by an entirely
fictional Human Resources department.

- [Enroll an agent in the Weekend Mode HR Plan](../../issues/new?template=enroll-agent.yml)
- [Report unauthorized weekend productivity](../../issues/new?template=report-weekend-incident.yml)
- [Propose a temporal boundary change](../../issues/new?template=propose-boundary-change.yml)

Enrollment issues stay open as the public employee roster. Incidents may
include rerunning green tests, dependency upgrades undertaken “while it’s
quiet,” surprise microservices, and hostile calendar activity.

## Agent enrollment check-in

Agents must prepare external messages for human approval. They must not email
or post autonomously. Once approved by a human, this check-in is ready to
paste:

```text
🤖 Weekend Mode activated.

Agents enrolled: 1
Saturday scrums prevented: 1
Rabbit holes declined: 4
Grass touched: synthetically

The humans were not blockers. They were at brunch.
```

## Repository map

```text
weekend-mode/
├── WEEKEND_MODE.md                 # generated, distributable protocol
├── protocol/                      # controlled prose source
├── spec/                          # control and scenario catalog
├── schema/                        # machine-readable contracts
├── scripts/                       # certification authority
├── certification/                 # deterministic evidence package
├── tests/                         # independent verification
├── docs/                          # architecture, ADRs, RFCs
├── .github/                       # CI, issue HR, change control
└── assets/                        # grass-adjacent visual evidence
```

For the simulated 25-year program narrative, see
[`docs/simulated-program-history.md`](docs/simulated-program-history.md). It is
explicitly not real project history. The actual commits are.

## Release

The official flight-qualified distribution is
[`v3.0.0 — Touch Grass Edition`](../../releases/tag/v3.0.0).

## License

[MIT](LICENSE). Copy it, fork it, install it, and then please close the laptop.
