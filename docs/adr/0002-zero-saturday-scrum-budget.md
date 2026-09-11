# ADR-0002: Zero Saturday Scrum Budget

- Status: Accepted
- Decision class: WM-3 Existential

## Context

Allowing even one Saturday scrum creates a precedent, a recurring meeting, and
eventually a transformation office.

## Decision

The allowed Saturday scrum creation count is an invariant integer equal to
zero across every control, scenario, simulation, workflow, and release.

## Consequences

- Nonzero values fail certification.
- There is no exception process.
- Actual incidents still use their real response structure, which may involve
  coordination but should not be mislabeled as a scrum for morale purposes.
