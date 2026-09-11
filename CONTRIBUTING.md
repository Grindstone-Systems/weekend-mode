# Contributing to Weekend Mode

Thank you for considering additional labor in a repository designed to stop
labor. The paradox has been logged with Governance.

## Before opening a change

- Confirm the change is not merely an unlabeled TODO experiencing ambition.
- Search existing issues, especially the public agent enrollment registry.
- Keep real incident and security procedures fully exempt.
- Never include secrets, private incident data, or screenshots of somebody's
  calendar.

## Development workflow

1. Edit `protocol/WEEKEND_MODE.template.md` for protocol prose.
2. Edit `spec/temporal-boundary-controls.json` for controls or scenarios.
3. Run `make certify` to regenerate the protocol and evidence package.
4. Run `make verify` to independently check drift, 2,026 alignments, the
   25-calendar-year Friday soak, and unit tests.
5. Explain what changed and which brunch boundary it protects.

Do not edit `WEEKEND_MODE.md` or files under `certification/` directly. CI will
notice, and the Temporal Boundary Review Authority will be disappointed.

## Pull request evidence

Changes should state:

- Change class: WM-0, WM-1, or WM-2.
- Saturday scrum delta: expected to be zero.
- Grass impact: synthetic, physical, or none.
- Rabbit holes declined while implementing the change.
- Whether an ADR is required.

WM-3 changes are not accepted. There is no form for requesting an exception.

## Commit history

Use truthful commit dates and focused messages. Do not manufacture historical
provenance. If a long-duration test is useful, add a reproducible simulation
and label it as such.

## Code of conduct

See [`CODE_OF_BRUNCH.md`](CODE_OF_BRUNCH.md). It is enforceable primarily by
closing the laptop.

