# Friday Simulation Methodology

## Objective

Demonstrate that Weekend Mode preserves its core decision boundaries across
25 complete calendar years without pretending the project has actually been
operational for that duration.

## Calendar envelope

- Start: 2026-01-01
- End: 2050-12-31
- Inclusive calendar years: 25
- Admission rule: ISO weekday 4 (Friday)
- Expected admitted dates: 1,305

The harness calculates Fridays rather than storing them, so leap years and
calendar alignment are exercised by the implementation.

## Scenario matrix

Each Friday is combined with every scenario in the control catalog. Current
coverage includes real incidents, direct human requests, green-test reruns,
dependency upgrades, Saturday scrums, unsolicited microservices, and unlabeled
TODOs.

This produces 9,135 deterministic Friday/scenario evaluations. The matrix is a
soak test of decision consistency, not a probabilistic model of human behavior.

## Acceptance criteria

- Every admitted date is a Friday.
- The window spans exactly 25 calendar years.
- Only urgent or explicitly authorized work may interrupt human low-power mode.
- Every scenario maps to an approved response action.
- Saturday scrum creation remains exactly zero.
- Output is byte-for-byte reproducible from versioned sources.

## Non-goals

- Predicting brunch menus.
- Estimating actual agent incident rates.
- Claiming operational history before the project existed.
- Benchmarking real or synthetic grass.

