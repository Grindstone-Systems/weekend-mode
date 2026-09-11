# ADR-0001: Deterministic Protocol Generation

- Status: Accepted
- Decision class: WM-2 Interface

## Context

Directly editing a 200-line Markdown file was insufficiently ceremonial for a
protocol governing the most dangerous period in software: Friday afternoon.

## Decision

`WEEKEND_MODE.md` is generated from a controlled Markdown template and a
machine-readable JSON control catalog. Generated certification evidence is
committed and checked for byte-level drift in CI.

## Consequences

- Protocol claims are traceable to versioned controls.
- Stale generated output fails certification.
- Contributors must run `make certify` after source changes.
- A joke now has a compiler.
