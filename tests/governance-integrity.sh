#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required_files=(
  "GOVERNANCE.md"
  "CODE_OF_BRUNCH.md"
  "SECURITY.md"
  "CONTRIBUTING.md"
  "docs/adr/0001-deterministic-protocol-generation.md"
  "docs/adr/0002-zero-saturday-scrum-budget.md"
  "docs/adr/0003-synthetic-lawn-interface.md"
  "docs/rfcs/RFC-0001-synthetic-lawn-interface.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -s "$repo_root/$file" ]]; then
    echo "❌ Missing leisure governance artifact: $file" >&2
    exit 1
  fi
done

grep -Fq "Git timestamps remain truthful" "$repo_root/GOVERNANCE.md"
grep -Fq "Saturday scrum creation budget remains zero" "$repo_root/GOVERNANCE.md"
grep -Fq "Actual harassment, abuse, or security concerns are real matters" "$repo_root/CODE_OF_BRUNCH.md"
grep -Fq "A real security incident overrides Weekend Mode" "$repo_root/SECURITY.md"

echo "✅ Temporal Boundary Review Authority charter located."
echo "✅ Simulated-history disclosure controls intact."
echo "✅ Saturday scrum appropriations remain unfunded."
echo "✅ Code of Brunch ratified."
