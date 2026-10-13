#!/bin/bash
# usage: ./setup-run.sh RUN
# Makes runs/RUN: a copy of the planner-and-handoff run's project as it ended (exegenius.toml,
# sources/, exegenius/ state, docs/), with `rounds = 4`, so `exegenius next` hands out the
# rewrites for round 3's notes, which the run itself dropped.
set -euo pipefail
run=$1
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/runs/$run"
cp -r "$root/exegenius" "$root/sources" "$root/docs" "$root/zensical.toml" "$root/runs/$run/"
sed 's/^rounds = 3$/rounds = 4/' "$root/exegenius.toml" > "$root/runs/$run/exegenius.toml"
grep -q '^rounds = 4$' "$root/runs/$run/exegenius.toml"
echo "runs/$run ready (rounds = 4)"
