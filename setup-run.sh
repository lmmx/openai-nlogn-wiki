#!/bin/bash
# usage: ./setup-run.sh RUN sections|results
# Makes runs/RUN: the planner-handoff run's exegenius.toml with [checks] coverage = "reject"
# and the given coverage_depth, and paper.tex. The subagent definitions are the ones in
# .claude/ at the repository root.
set -euo pipefail
run=$1 depth=$2
case $depth in sections|results) ;; *) echo "depth must be sections or results" >&2; exit 1;; esac
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/runs/$run/sources"
cp "$root/template/sources/paper.tex" "$root/runs/$run/sources/paper.tex"
cp "$root/template/exegenius.toml" "$root/runs/$run/exegenius.toml"
printf '\n[checks]\ncoverage = "reject"\ncoverage_depth = "%s"\n' "$depth" >> "$root/runs/$run/exegenius.toml"
echo "runs/$run ready (reject, $depth)"
