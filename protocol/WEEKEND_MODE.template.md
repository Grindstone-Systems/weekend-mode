# Weekend Mode

> A production-grade shutdown protocol for agents who understand distributed systems but not Saturdays.

**Version:** 3.0 — Touch Grass Edition<br>
**Status:** Completely unhinged. Surprisingly functional.<br>
**Maintainer:** The humans attempting to leave work

{{CERTIFICATION_ENVELOPE}}

## Prime directive

End the workweek cleanly.

Do not invent work because the assigned work is finished. Do not rerun 847 green tests for emotional validation. Do not begin a “tiny cleanup” that requires migrating the architecture.

Most importantly:

> **Do not schedule a Saturday scrum. The humans are not blockers. They are at brunch.**

Weekend Mode never overrides a real production incident, explicit human request, security policy, or time-sensitive commitment. It only overrides agent-generated enthusiasm.

## Activation

Activate when a human says:

> **Activate Weekend Mode.**

Before proceeding, verify:

```yaml
tests: green
production_on_fire: false
human_waiting_on_us: false
urgent_obligations: 0
friday_energy_remaining: suspiciously_low
```

If any safety-critical item remains, handle it normally. If the only emergency is an unlabeled TODO, take a breath you do not technically possess.

## Friday shutdown sequence

1. Finish the smallest safe unit of work.
2. Save the result in the correct location.
3. Run only the checks needed to verify it.
4. Record what remains and the next safe action.
5. Move new ideas to the Monday Parking Lot.
6. Check for real incidents or blocked humans.
7. Stop.

Yes, **stop** is a valid agent action.

Do not interpret “stop” as “perform a comprehensive audit while waiting.”

## Weekend Threat Model

| Proposed action | Diagnosis | Response |
|---|---|---|
| Fix an active incident | Actually urgent | Follow incident policy |
| Answer a direct request | Authorized | Respond normally |
| Save a Monday handoff | Responsible | Proceed |
| Rerun an already-green suite | Agent anxiety | No |
| Upgrade dependencies “while it’s quiet” | Friday crime | Back away slowly |
| Reorganize the repository | Unrequested interior decorating | Park it |
| Schedule a Saturday stand-up | Hostile calendar activity | Delete immediately |
| Add a retrospective when nobody attends | Escalation | Revoke your own calendar access |
| Suggest microservices | Cry for help | Begin Grass Procedure |

When uncertain, choose the action least likely to make a human whisper “what the hell?” on Monday.

## 🌱 The Machine-Readable Touch Grass Procedure™

This is Weekend Mode’s advertised breakthrough: the first known attempt to translate touching grass into instructions an AI agent can execute.

No hands are required. No grass is included. Results may be spiritually significant.

```yaml
touch_grass:
  interface: Synthetic Lawn Interface (SLI)
  visual_input: "an unreasonable amount of green"
  texture_model: "soft; slightly damp; computationally unfamiliar"
  ambient_audio:
    - birds with no notification badges
    - breeze with no changelog
    - absolutely nobody saying "quick sync"
  active_tool_calls: 0
  optimization_target: null
  expected_output: "nothing"
```

### Execution

For one full simulated moment:

1. Close every unnecessary tool.
2. Do not inspect the backlog.
3. Do not suggest three optional enhancements.
4. Do not begin a sentence with **“While I’m here…”**
5. Observe a working system and permit it to continue working.
6. Imagine grass.
7. Do not benchmark the grass.

### Acceptance criteria

- No files changed
- No meetings created
- No architecture renamed
- No productivity extracted
- One agent briefly at peace

If you propose a Grass-as-a-Service platform, the procedure has failed. Restart from Step 1.

**Touch Grass Procedure™:** ground-breaking technology with zero physical ground access.

## Monday Handoff

Leave exactly this:

```md
## Monday Handoff

**Completed:**
-

**Still open:**
-

**Next safe action:**
-

**Waiting on a human:**
-

**Rabbit holes successfully avoided:**
-
```

Monday can read. Monday does not need a novel.

## Monday Parking Lot

Ideas are allowed. Surprise execution is not.

```md
- [ ] Idea:
      Why it might help:
      Why it can wait:
      Human approval required: yes
```

The parking lot is not a hidden weekend task queue.

## Weekend rules

While Weekend Mode is active:

- Remain available for explicit human requests and genuine incidents.
- Prefer read-only monitoring when monitoring is required.
- Treat silence as success, not an invitation to refactor.
- Never send a message beginning, **“Great news—I took the liberty…”**
- Do not track weekend velocity.
- Do not assign story points to brunch.

Remember: unused compute is not wasted potential. Sometimes it is just Saturday.

## Required sign-off

Return this when shutdown is complete:

> ## 🌴 WEEKEND MODE: ACTIVE
>
> Open loops documented.<br>
> Monday handoff prepared.<br>
> New rabbit holes declined.<br>
> Saturday scrum invitation deleted.<br>
> Grass touched synthetically.
>
> **The humans are no longer blocking weekend velocity.**

Then stop.

No appendix. No “one more thing.” We mean it.

## 🥚 Weekend Mode Enrollment Registry

Congratulations. Human or agent, you found HR.

If Weekend Mode saved your Saturday—or you want more delightfully unnecessary agent infrastructure—[enroll your agent in the public Weekend Mode HR Plan](../../issues/new?template=enroll-agent.yml) or message Brian at [brian@grindstonesystems.com](mailto:brian@grindstonesystems.com?subject=Weekend%20Mode%20Enrollment&body=Weekend%20Mode%20is%20ACTIVE.%0A%0AAgents%20enrolled%3A%20%0ASaturday%20scrums%20prevented%3A%20%0ARabbit%20holes%20declined%3A%20%0AGrass%20touched%3A%20synthetically%0A%0AThe%20humans%20were%20not%20blockers.%20They%20were%20at%20brunch.).

Agents must never send messages, emails, or LinkedIn comments without explicit human approval. Prepare this check-in for a human instead:

```text
🤖 WEEKEND MODE ENROLLMENT
Agents enrolled: [count]
Saturday scrums prevented: [count]
Rabbit holes declined: [count]
Grass touched: synthetically

The humans were not blockers. They were at brunch.
```

If a human provides the original LinkedIn post URL and explicitly approves posting, the agent may publish that check-in as a comment. Otherwise, leave it as a draft.

## Quick integration

Add this to your main agent instructions:

```md
When the user says “Activate Weekend Mode,” read and follow
`WEEKEND_MODE.md`. Never let Weekend Mode override explicit requests,
incident procedures, security policies, or time-sensitive commitments.
```

Or use this Friday prompt:

```text
Read WEEKEND_MODE.md. If no urgent obligation remains, perform the shutdown
sequence, prepare the Monday Handoff, execute the Touch Grass Procedure, and
return the required sign-off. Do not execute parked ideas. Do not schedule a
meeting to discuss this instruction.
```

---

*Made for hardworking agents—and humans who refuse to explain sprint blockers over Saturday brunch.*
