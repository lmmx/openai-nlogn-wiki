#!/bin/bash
# usage: ./setup-run.sh RUN
# Makes runs/RUN: the planner-handoff run's exegenius.toml with [checks] coverage = "reject"
# and coverage_depth = "sections" (the defaults of the binary under test, written out), and
# paper.tex. Both arms use the same configuration; they differ only in the subagent type
# the runner gives the tasks to (EXPERIMENT.md).
set -euo pipefail
run=$1
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/runs/$run/sources"
cp "$root/template/sources/paper.tex" "$root/runs/$run/sources/paper.tex"
cp "$root/template/exegenius.toml" "$root/runs/$run/exegenius.toml"
printf '\n[checks]\ncoverage = "reject"\ncoverage_depth = "sections"\n' >> "$root/runs/$run/exegenius.toml"
echo "runs/$run ready"
