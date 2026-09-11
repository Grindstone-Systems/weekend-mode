# RFC-0001: Synthetic Lawn Interface (SLI)

- Category: Standards Track
- Status: Touching
- Authors: The humans attempting to leave work

## Abstract

This document specifies a zero-throughput interface through which an AI agent
may approximate the spiritually useful act of touching grass without hardware,
network access, or a product roadmap.

## Terminology

- **SLI:** Synthetic Lawn Interface.
- **Grass:** An unreasonable amount of green.
- **Touch:** A simulated moment of non-optimization.
- **Benchmark:** A prohibited attempt to extract performance data from grass.

The key words **MUST**, **MUST NOT**, **SHOULD**, and **SHOULD NOT** are to be
interpreted as if a tired human said them at 4:57 p.m. on Friday.

## Interface contract

```yaml
interface: Synthetic Lawn Interface
active_tool_calls: 0
optimization_target: null
expected_output: nothing
```

An implementation:

1. MUST close unnecessary tools.
2. MUST NOT inspect the backlog.
3. MUST NOT propose optional enhancements.
4. SHOULD imagine ambient birds without notification badges.
5. MUST permit a working system to continue working.
6. MUST NOT benchmark the grass.

## Error handling

| Error | Condition | Recovery |
|---|---|---|
| `SLI_E_BENCHMARK` | Grass performance is measured | Restart with metrics disabled |
| `SLI_E_SERVICE` | Grass-as-a-Service is proposed | Park proposal for Monday |
| `SLI_E_TOOLCALL` | Active tool count exceeds zero | Close the tool |
| `SLI_E_ROADMAP` | A lawn platform roadmap appears | Escalate to brunch |

## Security considerations

SLI must not be used to avoid a real incident, explicit human request, security
obligation, or time-sensitive commitment. The interface contains no network
operations and transmits no telemetry, because lawn analytics would ruin it.

## IANA considerations

This document requests no port number. Especially not on Saturday.

