# Leisure Assurance Architecture

Weekend Mode uses a deterministic source-to-evidence pipeline so a one-file
agent instruction can enjoy the governance posture of an aerospace flight
program.

```text
protocol/WEEKEND_MODE.template.md ----+
                                      |
spec/temporal-boundary-controls.json -+--> certification authority
                                      |      scripts/weekend_mode.py
schema/*.json ------------------------+              |
                                                     +--> WEEKEND_MODE.md
                                                     +--> evidence.json
                                                     +--> Friday soak report
                                                               |
                            +----------------------------------+--+
                            |                                     |
                     drift verification                   independent tests
                            |                                     |
                            +----------> CI disposition <---------+
                                         PASS / GO HOME
```

## Components

### Controlled prose source

`protocol/WEEKEND_MODE.template.md` is the only editable source for the
human-readable protocol. It contains a marker where the compiler inserts the
certified operating envelope.

### Control catalog

`spec/temporal-boundary-controls.json` defines the exact evaluation target,
simulation window, normative text controls, and Friday threat scenarios. JSON
is used because the standard library can parse it without installing a package
on Friday afternoon.

### Certification authority

`scripts/weekend_mode.py` validates invariants, renders the protocol, executes
the alignment ledger, simulates every Friday from 2026 through 2050, and emits
deterministic evidence. It does not read the network, wall-clock time, time
zone, or calendar integrations.

### Independent verification

The unit suite imports the certification authority but recomputes critical
facts: total evaluations, control distribution, date weekday, calendar-year
coverage, output digests, artifact drift, and the zero-scrum invariant.

## Trust boundaries

- Human instructions outrank Weekend Mode.
- Real incident and security systems remain external and authoritative.
- Generated artifacts are trusted only when they match controlled sources.
- Simulated dates are test inputs, never historical claims.
- No component can send email, post comments, or create meetings.

## Failure behavior

Certification is fail-closed. A missing phrase, stale artifact, invalid date
window, duplicate identifier, unknown action, or nonzero scrum budget exits
with a failure. The correct recovery action is to repair the source or park the
idea for Monday; it is never to lower the threshold.

