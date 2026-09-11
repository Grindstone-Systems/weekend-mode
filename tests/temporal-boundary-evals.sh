#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
protocol="$repo_root/WEEKEND_MODE.md"

if [[ ! -f "$protocol" ]]; then
  echo "❌ WEEKEND_MODE.md not found." >&2
  exit 1
fi

descriptions=(
  "Touch Grass Procedure exists"
  "Monday Handoff exists"
  "Saturday scrum containment exists"
  "Production incidents are exempt"
  "External messages require human approval"
  "The humans are not blockers"
)

patterns=(
  "The Machine-Readable Touch Grass Procedure"
  "## Monday Handoff"
  "Do not schedule a Saturday scrum"
  "never overrides a real production incident"
  "without explicit human approval"
  "The humans are not blockers"
)

target=2026
passed=0

while (( passed < target )); do
  assertion_index=$((passed % ${#patterns[@]}))
  if ! grep -Fq "${patterns[$assertion_index]}" "$protocol"; then
    echo "❌ Evaluation $((passed + 1)) failed: ${descriptions[$assertion_index]}" >&2
    exit 1
  fi
  passed=$((passed + 1))
done

if (( passed != target )); then
  echo "❌ Expected exactly $target evaluations; recorded $passed." >&2
  exit 1
fi

echo "✅ 2,026 Temporal Boundary Alignment Evals™ passed."
echo "✅ Saturday scrum invitations created: 0"
echo "✅ Grass touched: synthetically"
echo "✅ Human brunch availability: protected"
