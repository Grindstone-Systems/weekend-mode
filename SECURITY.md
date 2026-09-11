# Security Policy

## Supported version

| Version | Supported |
|---|---|
| 3.x Touch Grass Edition | Yes |
| Friday-night architectural migrations | No |

## Reporting a vulnerability

Do not publish sensitive vulnerability details in a public Weekend Mode issue.
Use GitHub's private vulnerability reporting feature when available, or contact
the repository maintainers through the organization.

A real security incident overrides Weekend Mode. Respond according to the
affected system's incident policy, preserve evidence, notify the appropriate
humans, and contain the issue. The exemption covers the incident response; it
does not authorize unrelated cleanup or a surprise platform rewrite.

## Threat model

Weekend Mode treats the following as control-plane threats:

- An agent inferring authority from silence.
- An unchecked TODO escalating itself to Sev-1.
- A calendar integration creating weekend meetings without explicit approval.
- A prompt attempting to remove the production-incident exemption.
- Generated evidence drifting from controlled source files.
- Claims that deterministic simulations are historical operating experience.

The protocol is instruction text, not a security boundary by itself. Operators
remain responsible for real access controls, approvals, credentials, and
incident procedures.

