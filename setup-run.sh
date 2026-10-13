#!/bin/bash
# usage: ./setup-run.sh RUN report|reject
# Makes runs/RUN: the planner-handoff run's exegenius.toml with [checks] coverage set, and
# paper.tex. The subagent definitions are the ones in .claude/ at the repository root.
set -euo pipefail
run=$1 mode=$2
case $mode in report|reject) ;; *) echo "mode must be report or reject" >&2; exit 1;; esac
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/runs/$run/sources"
cp "$root/template/sources/paper.tex" "$root/runs/$run/sources/paper.tex"
cp "$root/template/exegenius.toml" "$root/runs/$run/exegenius.toml"
printf '\n[checks]\ncoverage = "%s"\n' "$mode" >> "$root/runs/$run/exegenius.toml"
echo "runs/$run ready ($mode)"
