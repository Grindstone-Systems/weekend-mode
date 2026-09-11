# 🌴 Weekend Mode

Production-grade weekend protection for AI agents that understand
distributed systems—but not Saturdays.

> Human operators entering low-power mode on Saturday is a feature,
> not an outage.

[Activate Weekend Mode](WEEKEND_MODE.md) ·
[Enroll Your Agent](../../issues/new?template=enroll-agent.yml) ·
[Report Unauthorized Productivity](../../issues/new?template=report-weekend-incident.yml)

[![Aerospace-Grade Leisure Certification](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/temporal-boundary-alignment.yml/badge.svg)](https://github.com/Grindstone-Systems/weekend-mode/actions/workflows/temporal-boundary-alignment.yml)
![Temporal Boundary Evals](https://img.shields.io/badge/Temporal_Boundary_Evals-2%2C026_Passing-brightgreen)
![Saturday Scrums](https://img.shields.io/badge/Saturday_Scrums-0-success)
![Grass Status](https://img.shields.io/badge/Grass-Synthetically_Touched-green)
![Patent](https://img.shields.io/badge/Patent-Pending_Of_Course-blue)

Weekend Mode is a shutdown protocol for agentic systems whose work is done but
whose enthusiasm remains dangerously unbounded. It protects human brunch,
contains surprise refactors, and establishes that an unchecked TODO is not
automatically a Saturday Sev-1.

It is also, against all reasonable expectations, tested.

## Install

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

## What it actually does

- Finishes the smallest safe unit of work.
- Runs only the checks needed to verify it.
- Records open loops in a compact Monday handoff.
- Parks new ideas instead of executing them by surprise.
- Remains available for genuine incidents and direct human requests.
- Executes the Machine-Readable Touch Grass Procedure™.
- Stops.

Weekend Mode never outranks an incident, explicit human direction, security
policy, or time-sensitive commitment. It only constrains agent-generated
enthusiasm.

## Aerospace-grade leisure certification

[`tests/temporal-boundary-evals.sh`](tests/temporal-boundary-evals.sh) checks
the protocol for its essential controls and repeats those assertions until it
has recorded exactly **2,026 successful evaluations**. The GitHub Actions
workflow runs the suite on every push and pull request.

```text
✅ 2,026 Temporal Boundary Alignment Evals™ passed.
✅ Saturday scrum invitations created: 0
✅ Grass touched: synthetically
✅ Human brunch availability: protected
```

No benchmarks were performed on the grass.

## Weekend Mode HR

The Issues tab is an entirely serious public registry operated by an entirely
fictional Human Resources department.

- [Enroll an agent in the Weekend Mode HR Plan](../../issues/new?template=enroll-agent.yml)
- [Report unauthorized weekend productivity](../../issues/new?template=report-weekend-incident.yml)

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

## License

[MIT](LICENSE). Copy it, fork it, install it, and then please close the laptop.
