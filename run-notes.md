# Full run of exegenius 0.6.0 (LaTeX source)

Branch `full-v0.6-latex-planner-handoff`. Source `sources/paper.tex` (via latexpand). Target: main-theorem. Reader: `[reader] knows` as in exegenius.toml, plus the calculus correction (`exegenius background --redo`, applied once when the reader was first shown). `stop_early = false`, `[simulation] rounds = 0`, 3 audit rounds. Binary: `/workspace/bin/exegenius` (0.6.0). Subagents: `exegenius-planner` for extract/background/argument/extend, `exegenius-task` for the rest, all with the full binary path.

## Final state

`exegenius status` (saved to `run-status.txt`): done. 212 tasks handed out, 212 accepted, 0 pending. Wiki in `docs/` (25 pages, 6 parts, 1 glossary page, 40 symbols on the notation page) with `zensical.toml`. Not pushed.

## What went wrong, and what I did about it

- **Stray shell from a subagent (task 0007).** The 0007 subagent left a background `python3` (pid 641, child of shell pid 639) blocked on stdin after its own submit had already been accepted. I killed both processes. The 0007 answer files were last written before that retry and were not changed by the kill. The subagent reported its background job exited with code 144 and that the answer stayed accepted.
- **Submits run from the wrong directory.** Many subagents ran `exegenius submit` from `exegenius/tasks/` and got a config-path error (`exegenius.toml` not found). These were not answer rejections; each was rerun from the project directory and accepted. They are not counted in the rejection column below.
- **Stray files outside the scratchpad.** Subagents for 0023 and 0065 left scratch files in `/tmp`, against the scratchpad rule. Nothing in the repo depends on them.
- **Rewrite rule vs. audit requests.** The submit check for rewrites (rounds 2, 3, and the post-support rewrites) accepts only letter and citation fixes. Many subagents reported that the audit's requested restructuring or added derivations were rejected for "new claims", so those requests were not applied. This is the main reason the pages still carry open gaps (below).
- **Leftover gaps reported by the process itself.** `exegenius status` after the last audit round: "the last audit round's 100 gaps are left on the pages, since no audit would check rewrites for them; raise `rounds` to have them fixed". I did not change `rounds` (the run was configured for 3). Also: 50 steps were sent back to be cited or cut; 21 letters with two meanings are still unjudged after the last overloads round; citation support marks: 23 supported, 32 partial, 10 unsupported, 0 contradicted.
- **Mathematical gaps flagged by subagents (not fixed; need a human or a further revision):**
  - `recursive-power-saving` (0206, earlier 0189): the leaf bound `O(f^σ d^{β(1−σ)}) ≤ O(f^λ)` does not follow from `d ≤ f^{1/β}`; the source combines the terms as `O(d^{λ'})` with `λ' < 1`.
  - `main-theorem` (0209): the per-level argument (about lg n / d layers at cost V·d^{λ'}) is not spelled out; the rewrite rule kept the previous text. Some letters clash (m, q, d, Φ).
  - `dft-fft` and `fixed-tape-model` letters (m, u, v, A) keep meanings from earlier pages and are noted on the page, not renamed.
- **Symbol clashes.** Several rename requests (audits 0183, 0188, 0189, 0206, 0208) conflicted with later pages' bindings; subagents kept the old letters and noted the changed meaning.

## Interpretations I made

- "Write task" = tasks of kind `write` (the `exegenius-task` type that writes a page). The reporting suffix you asked for was added to every write task prompt (round 1 writes, rewrites in rounds 2 and 3, the post-audit rewrites, and the final round 0200–0209 rewrites). It was not added to planning tasks, audits, outline/overloads, or support tasks (those are not kind `write`). Their replies are just "accepted".
- Under the "write task" prompt, the reply after the submit result was requested as "on new lines ..." in place of "Reply with only accepted or the last error". The condensed replies below keep the rejection counts and the reasons.
- The table reply column is condensed for write tasks (a few words each); audits, planners, and support tasks replied only "accepted".
- The audit prompts keep the standard "Reply with only accepted or the last error" wording, since audits are not write tasks.
- Reader correction: the calculus correction went in once (`exegenius background --redo "..."`) after the reader was first shown, as you asked. The second reader display (after the redo) was run as "done with the reader" without a second redo.
- `exegenius next` printed `done` at the end; no simulated readers or `exegenius/report.md` were produced, because `[simulation] rounds = 0`. That is the configured setting, not a failure.
- Commit message is exactly as requested; per the memory rule about commit style, no Co-Authored-By trailer was added.

## Subagent table

Tokens and durations are as reported when each subagent finished. Rejections = submit rejections as the subagent reported them (not counting wrong-directory config errors). Write-task replies are condensed.

| Task | Subagent type | Total tokens | Duration (s) | Rejections | Reply after "accepted" |
|---|---|---|---|---|---|
| 0001-extract | exegenius-planner | 26918 | 38.9 | 0 | (none; planning reply: "accepted") |
| 0002-background | exegenius-planner | 15531 | 24.5 | 0 | (none) |
| 0003-background (redo) | exegenius-planner | 12147 | 16.5 | 0 | (none) |
| 0004-argument | exegenius-planner | 36424 | 86.3 | 0 | (none) |
| 0005-write-nlogn-conjecture | exegenius-task | 28829 | 66.8 | 3 | three rejections (n used before its definition; prerequisite id; relation) |
| 0006-write-convolution | exegenius-task | 24618 | 49.4 | 0 | no rejections; no new claims |
| 0007-write-radix-digit-reduction | exegenius-task | 52281 | 1014.8 | 2 | two rejections (c_k, h_k, d_k used before definition); background submit hung, killed by me, answer already accepted |
| 0008-write-poly-ring-y-r | exegenius-task | 27172 | 62.6 | 1 | y, r used before definition |
| 0009-write-dft-fft | exegenius-task | 22814 | 55.1 | 0 | no rejections; prerequisite id inferred |
| 0010-write-ss-hh-background | exegenius-task | 25655 | 52.6 | 1 | n used before definition |
| 0011-write-synthetic-transforms | exegenius-task | 23102 | 44.6 | 1 | prerequisite ids with .md |
| 0012-write-bluestein-chirp | exegenius-task | 36040 | 95.2 | 1 | j, k used before definition |
| 0013-write-phase-twist-convolution | exegenius-task | 37272 | 91.8 | 1 | Bluestein relation quote mismatch |
| 0014-write-fixed-point-precision | exegenius-task | 46896 | 109.6 | 1 | b, k_j used before definition |
| 0015-write-signed-packing | exegenius-task | 38339 | 94.4 | 1 | citation sentence needed its claim restated |
| 0016-write-fixed-tape-model | exegenius-task | 18362 | 27.3 | 0 | no rejections; no derivations step list in task |
| 0017-write-address-fields | exegenius-task | 26240 | 59.3 | 1 | relation predicate quote mismatch |
| 0018-write-linear-network-roles | exegenius-task | 32656 | 72.6 | 1 | rewrite 357 words over 350 limit |
| 0019-write-scratch-restoration | exegenius-task | 18907 | 42.6 | 1 | linear-network-roles not a prerequisite id |
| 0020-write-address-shear-factorization | exegenius-task | 53419 | 143.1 | 2 | over word limit twice |
| 0021-write-subset-intersection-construction | exegenius-task | 28135 | 65.2 | 0 | no rejections; read source for W and s |
| 0022-write-recursive-power-saving | exegenius-task | 26000 | 54.5 | 0 | no rejections; derived exponent from paragraph |
| 0023-write-fast-address-interchange | exegenius-task | 39489 | 97.4 | 1 | u, V, tau used before definition |
| 0024-write-fast-butterfly-layers | exegenius-task | 52929 | 133.6 | 0 | no rejections; read source sections |
| 0025-write-crt-address-map | exegenius-task | 29172 | 109.3 | 1 | p_j symbol not in page; then invalid JSON escape |
| 0026-write-gaussian-resampling | exegenius-task | 22926 | 44.8 | 0 | no rejections |
| 0027-write-ring-convolution-retained-order | exegenius-task | 43186 | 112.5 | 2 | over word limit twice |
| 0028-write-main-theorem | exegenius-task | 96039 | 257.5 | 2 | symbols used before definition; 354 over limit |
| 0029-audit-nlogn-conjecture | exegenius-task | 17861 | 31.4 | 0 | (audit) accepted |
| 0030-audit-convolution | exegenius-task | 19998 | 33.6 | 0 | (audit) accepted |
| 0031-audit-radix-digit-reduction | exegenius-task | 23927 | 229.1 | 0 | (audit) accepted |
| 0032-audit-poly-ring-y-r | exegenius-task | 19349 | 31.3 | 0 | (audit) accepted |
| 0033-audit-dft-fft | exegenius-task | 28503 | 65.5 | 0 | (audit) accepted |
| 0034-audit-ss-hh-background | exegenius-task | 21866 | 44.8 | 0 | (audit) accepted |
| 0035-audit-synthetic-transforms | exegenius-task | 18814 | 28.9 | 0 | (audit) accepted |
| 0036-audit-bluestein-chirp | exegenius-task | 25936 | 52.7 | 0 | (audit) accepted |
| 0037-audit-phase-twist-convolution | exegenius-task | 26133 | 56.2 | 0 | (audit) accepted |
| 0038-audit-fixed-point-precision | exegenius-task | 25579 | 61.3 | 0 | (audit) accepted |
| 0039-audit-signed-packing | exegenius-task | 31034 | 85.1 | 0 | (audit) accepted |
| 0040-audit-fixed-tape-model | exegenius-task | 16001 | 19.3 | 0 | (audit) accepted |
| 0041-audit-address-fields | exegenius-task | 19360 | 31.6 | 0 | (audit) accepted |
| 0042-audit-linear-network-roles | exegenius-task | 32002 | 83.4 | 0 | (audit) accepted |
| 0043-audit-scratch-restoration | exegenius-task | 15327 | 16.0 | 0 | (audit) accepted |
| 0044-audit-address-shear-factorization | exegenius-task | 31924 | 87.8 | 0 | (audit) accepted |
| 0045-audit-subset-intersection-construction | exegenius-task | 19222 | 33.6 | 0 | (audit) accepted |
| 0046-audit-recursive-power-saving | exegenius-task | 19203 | 31.3 | 0 | (audit) accepted |
| 0047-audit-fast-address-interchange | exegenius-task | 21522 | 50.7 | 0 | (audit) accepted |
| 0048-audit-fast-butterfly-layers | exegenius-task | 28277 | 60.5 | 0 | (audit) accepted |
| 0049-audit-crt-address-map | exegenius-task | 23206 | 49.1 | 0 | (audit) accepted |
| 0050-audit-gaussian-resampling | exegenius-task | 18736 | 28.7 | 0 | (audit) accepted |
| 0051-audit-ring-convolution-retained-order | exegenius-task | 27793 | 59.4 | 0 | (audit) accepted |
| 0052-audit-main-theorem | exegenius-task | 31645 | 71.9 | 0 | (audit) accepted |
| 0053-extend | exegenius-planner | 14529 | 8.6 | 0 | (none; planning reply: "accepted") |
| 0054-write-nlogn-conjecture | exegenius-task | 37765 | 90.3 | 2 | $\Omega$ unbound; n used before definition; relation id |
| 0055-write-radix-digit-reduction | exegenius-task | 35521 | 94.7 | 1 | new letter K; 366 words over limit |
| 0056-write-poly-ring-y-r | exegenius-task | 38661 | 115.5 | 1 | L unbound; y, r, j, k used before definition |
| 0057-write-fixed-point-precision | exegenius-task | 58660 | 131.1 | 0 | no rejections; read error/carry sections of paper |
| 0058-write-fixed-tape-model | exegenius-task | 30104 | 105.7 | 1 | 430 words over budget |
| 0059-write-address-fields | exegenius-task | 36941 | 72.1 | 1 | 381 words over budget |
| 0060-write-dft-fft | exegenius-task | 84954 | 305.3 | 4 | relation quote with cite markup; m used before binding; prerequisite ids .md |
| 0061-write-ss-hh-background | exegenius-task | 39318 | 329.8 | 0 | no rejections; read paper for chain |
| 0062-write-synthetic-transforms | exegenius-task | 43661 | 98.2 | 1 | relations used .md file names |
| 0063-write-linear-network-roles | exegenius-task | 55084 | 127.2 | 1 | 421 words over 411; t used before definition |
| 0064-write-scratch-restoration | exegenius-task | 31013 | 60.7 | 0 | no rejections; dropped numeric example |
| 0065-write-address-shear-factorization | exegenius-task | 75075 | 248.6 | 2 | q, b, t used before definition; t inside LaTeX commands |
| 0066-write-subset-intersection-construction | exegenius-task | 74855 | 203.4 | 3 | new letters unbound; word count; quote mismatch |
| 0067-write-recursive-power-saving | exegenius-task | 38823 | 83.3 | 3 | O unbound; 283 over 275; quote mismatch |
| 0068-write-fast-address-interchange | exegenius-task | 49692 | 175.4 | 1 | relation predicate over six words |
| 0069-write-fast-butterfly-layers | exegenius-task | 102105 | 303.9 | 1 | Theta unbound; H_0, i used early; predicate length |
| 0070-write-crt-address-map | exegenius-task | 34377 | 64.3 | 0 | no rejections; renamed clashing letters |
| 0071-write-gaussian-resampling | exegenius-task | 51282 | 117.5 | 0 | no rejections; 346 of 361 words |
| 0072-write-bluestein-chirp | exegenius-task | 59895 | 168.0 | 2 | l used early; relation ids; v quote |
| 0073-write-phase-twist-convolution | exegenius-task | 54572 | 141.2 | 1 | j used early; h binding dropped |
| 0074-write-signed-packing | exegenius-task | 77236 | 209.0 | 2 | symbols used early; display names over four words; 394 words |
| 0075-write-ring-convolution-retained-order | exegenius-task | 48882 | 106.5 | 0 | no rejections; renamed u,v to f,g |
| 0076-write-main-theorem | exegenius-task | 67561 | 151.5 | 2 | 530 words over budget; kappa used early |
| 0077-audit-nlogn-conjecture | exegenius-task | 25066 | 55.7 | 0 | (audit) accepted |
| 0078-audit-convolution | exegenius-task | 18408 | 26.2 | 0 | (audit) accepted |
| 0079-audit-radix-digit-reduction | exegenius-task | 30384 | 71.8 | 0 | (audit) accepted |
| 0080-audit-poly-ring-y-r | exegenius-task | 24929 | 53.2 | 0 | (audit) accepted |
| 0081-audit-fixed-point-precision | exegenius-task | 31662 | 74.7 | 0 | (audit) accepted |
| 0082-audit-fixed-tape-model | exegenius-task | 17157 | 23.7 | 0 | (audit) accepted |
| 0083-audit-address-fields | exegenius-task | 18862 | 31.5 | 0 | (audit) accepted |
| 0084-audit-dft-fft | exegenius-task | 30145 | 70.1 | 0 | (audit) accepted |
| 0085-audit-ss-hh-background | exegenius-task | 22895 | 46.3 | 0 | (audit) accepted |
| 0086-audit-synthetic-transforms | exegenius-task | 26095 | 58.2 | 0 | (audit) accepted |
| 0087-audit-linear-network-roles | exegenius-task | 31125 | 70.6 | 0 | (audit) accepted |
| 0088-audit-scratch-restoration | exegenius-task | 16408 | 19.4 | 0 | (audit) accepted |
| 0089-audit-address-shear-factorization | exegenius-task | 41895 | 113.6 | 0 | (audit) accepted |
| 0090-audit-subset-intersection-construction | exegenius-task | 34960 | 88.7 | 0 | (audit) accepted |
| 0091-audit-recursive-power-saving | exegenius-task | 28555 | 67.8 | 0 | (audit) accepted |
| 0092-audit-fast-address-interchange | exegenius-task | 26773 | 57.6 | 0 | (audit) accepted |
| 0093-audit-fast-butterfly-layers | exegenius-task | 41621 | 110.4 | 0 | (audit) accepted |
| 0094-audit-crt-address-map | exegenius-task | 23454 | 45.9 | 0 | (audit) accepted |
| 0095-audit-gaussian-resampling | exegenius-task | 29588 | 62.7 | 0 | (audit) accepted |
| 0096-audit-bluestein-chirp | exegenius-task | 27078 | 53.9 | 0 | (audit) accepted |
| 0097-audit-phase-twist-convolution | exegenius-task | 31646 | 68.6 | 0 | (audit) accepted |
| 0098-audit-signed-packing | exegenius-task | 42472 | 112.4 | 0 | (audit) accepted |
| 0099-audit-ring-convolution-retained-order | exegenius-task | 29385 | 70.3 | 0 | (audit) accepted |
| 0100-audit-main-theorem | exegenius-task | 33886 | 80.2 | 0 | (audit) accepted |
| 0101-extend | exegenius-planner | 15175 | 9.7 | 0 | (none; planning reply: "accepted") |
| 0102-argument | exegenius-planner | 32638 | 27.2 | 0 | (none; planning reply: "accepted") |
| 0103-write-nlogn-conjecture | exegenius-task | 30955 | 62.6 | 1 | ss-hh-background not a prerequisite; wrong-directory rerun |
| 0104-write-radix-digit-reduction | exegenius-task | 36419 | 84.2 | 1 | y used before definition |
| 0105-write-poly-ring-y-r | exegenius-task | 37234 | 86.0 | 1 | dropped j binding; definitions moved to first use |
| 0106-write-fixed-tape-model | exegenius-task | 24900 | 44.2 | 0 | no rejections |
| 0107-write-address-fields | exegenius-task | 32698 | 61.9 | 3 | quotes not found; m used early |
| 0108-write-dft-fft | exegenius-task | 67163 | 207.4 | 3 | m, A used early; wrong-directory rerun |
| 0109-write-ss-hh-background | exegenius-task | 31631 | 67.2 | 0 | no rejections; S bound |
| 0110-write-synthetic-transforms | exegenius-task | 49683 | 127.4 | 1 | L unbound; prerequisite ids .md |
| 0111-write-linear-network-roles | exegenius-task | 41329 | 91.9 | 1 | I no longer bound; wrong-directory rerun |
| 0112-write-scratch-restoration | exegenius-task | 34947 | 68.6 | 1 | prerequisite id .md |
| 0113-write-address-shear-factorization | exegenius-task | 75125 | 210.9 | 1 | symbols used early |
| 0114-write-crt-address-map | exegenius-task | 38604 | 72.7 | 4 | undeclared f; word counts 399 and 379; quote for e |
| 0115-write-gaussian-resampling | exegenius-task | 73934 | 192.9 | 1 | 470 words over 432; .md ids; display names |
| 0116-write-bluestein-chirp | exegenius-task | 59886 | 151.2 | 2 | j,k,l,t,h used early; quote mismatch |
| 0117-write-phase-twist-convolution | exegenius-task | 49058 | 102.9 | 1 | letters used early; .md ids |
| 0118-write-fixed-point-precision | exegenius-task | 77796 | 196.9 | 1 | S used before definition |
| 0119-write-signed-packing | exegenius-task | 69591 | 178.6 | 2 | letters used early; citation not word-for-word |
| 0120-write-ring-convolution-retained-order | exegenius-task | 57072 | 107.8 | 0 | no rejections; letters renamed |
| 0121-write-tensor-product-of-vector-spaces | exegenius-task | 46061 | 88.4 | 1 | display name over four words |
| 0122-write-subset-intersection-construction | exegenius-task | 90223 | 237.5 | 1 | Y unbound; T, U used early |
| 0123-write-recursive-power-saving | exegenius-task | 92620 | 242.6 | 1 | f, K, d, eta used early; quote mismatches |
| 0124-write-fast-address-interchange | exegenius-task | 51376 | 114.8 | 1 | predicate over six words |
| 0125-write-fast-butterfly-layers | exegenius-task | 123625 | 363.4 | 2 | i, sigma used early; third submit accepted |
| 0126-write-main-theorem | exegenius-task | 111761 | 312.4 | 1 | rho used early |
| 0127-audit-nlogn-conjecture | exegenius-task | 20296 | 37.2 | 0 | (audit) accepted |
| 0128-audit-convolution | exegenius-task | 19428 | 30.9 | 0 | (audit) accepted |
| 0129-audit-radix-digit-reduction | exegenius-task | 28021 | 56.5 | 0 | (audit) accepted |
| 0130-audit-poly-ring-y-r | exegenius-task | 20205 | 33.7 | 0 | (audit) accepted |
| 0131-audit-fixed-tape-model | exegenius-task | 19593 | 64.2 | 0 | (audit) accepted |
| 0132-audit-address-fields | exegenius-task | 19102 | 33.5 | 0 | (audit) accepted |
| 0133-audit-dft-fft | exegenius-task | 28492 | 73.0 | 0 | (audit) accepted |
| 0134-audit-ss-hh-background | exegenius-task | 30026 | 74.3 | 0 | (audit) accepted |
| 0135-audit-synthetic-transforms | exegenius-task | 22590 | 45.9 | 0 | (audit) accepted |
| 0136-audit-linear-network-roles | exegenius-task | 27648 | 57.3 | 0 | (audit) accepted |
| 0137-audit-scratch-restoration | exegenius-task | 16491 | 20.0 | 0 | (audit) accepted |
| 0138-audit-address-shear-factorization | exegenius-task | 37742 | 92.3 | 0 | (audit) accepted |
| 0139-audit-crt-address-map | exegenius-task | 27089 | 56.5 | 0 | (audit) accepted |
| 0140-audit-gaussian-resampling | exegenius-task | 47737 | 137.1 | 0 | (audit) accepted |
| 0141-audit-bluestein-chirp | exegenius-task | 29675 | 63.9 | 0 | (audit) accepted |
| 0142-audit-phase-twist-convolution | exegenius-task | 32363 | 72.2 | 0 | (audit) accepted |
| 0143-audit-fixed-point-precision | exegenius-task | 58060 | 175.8 | 0 | (audit) accepted |
| 0144-audit-signed-packing | exegenius-task | 39866 | 101.7 | 0 | (audit) accepted |
| 0145-audit-ring-convolution-retained-order | exegenius-task | 32722 | 95.6 | 0 | (audit) accepted |
| 0146-audit-tensor-product-of-vector-spaces | exegenius-task | 37606 | 97.2 | 0 | (audit) accepted |
| 0147-audit-subset-intersection-construction | exegenius-task | 39262 | 97.1 | 0 | (audit) accepted |
| 0148-audit-recursive-power-saving | exegenius-task | 43253 | 117.8 | 0 | (audit) accepted |
| 0149-audit-fast-address-interchange | exegenius-task | 32389 | 76.3 | 0 | (audit) accepted |
| 0150-audit-fast-butterfly-layers | exegenius-task | 50794 | 137.2 | 0 | (audit) accepted |
| 0151-audit-main-theorem | exegenius-task | 48364 | 130.3 | 0 | (audit) accepted |
| 0152-outline | exegenius-task | 17350 | 25.1 | 0 | accepted (outline) |
| 0153-overloads | exegenius-task | 70948 | 185.6 | 0 | accepted (overloads) |
| 0154-support-nlogn-conjecture | exegenius-task | 11051 | 11.6 | 0 | (support) accepted |
| 0155-support-nlogn-conjecture-second | exegenius-task | 10211 | 8.1 | 0 | (support) accepted |
| 0156-support-radix-digit-reduction | exegenius-task | 9350 | 9.0 | 0 | (support) accepted |
| 0157-support-poly-ring-y-r | exegenius-task | 10239 | 12.5 | 0 | (support) accepted |
| 0158-support-fixed-tape-model | exegenius-task | 9760 | 9.5 | 0 | (support) accepted |
| 0159-support-address-fields | exegenius-task | 9626 | 7.6 | 0 | (support) accepted |
| 0160-support-dft-fft | exegenius-task | 8937 | 9.8 | 0 | (support) accepted |
| 0161-support-ss-hh-background | exegenius-task | 9329 | 7.3 | 0 | (support) accepted |
| 0162-support-linear-network-roles | exegenius-task | 9643 | 6.8 | 0 | (support) accepted |
| 0163-support-scratch-restoration | exegenius-task | 8936 | 7.9 | 0 | (support) accepted |
| 0164-support-address-shear-factorization | exegenius-task | 9718 | 30.4 | 0 | (support) accepted |
| 0165-support-crt-address-map | exegenius-task | 9551 | 18.7 | 0 | (support) accepted |
| 0166-support-gaussian-resampling | exegenius-task | 9322 | 5.9 | 0 | (support) accepted |
| 0167-support-bluestein-chirp | exegenius-task | 9082 | 6.8 | 0 | (support) accepted |
| 0168-support-phase-twist-convolution | exegenius-task | 8939 | 6.6 | 0 | (support) accepted |
| 0169-support-fixed-point-precision | exegenius-task | 12887 | 11.5 | 0 | (support) accepted |
| 0170-support-signed-packing | exegenius-task | 11345 | 9.6 | 0 | (support) accepted |
| 0171-support-ring-convolution-retained-order | exegenius-task | 10210 | 9.3 | 0 | (support) accepted |
| 0172-support-tensor-product-of-vector-spaces | exegenius-task | 8799 | 7.5 | 0 | (support) accepted |
| 0173-support-subset-intersection-construction | exegenius-task | 9860 | 8.2 | 0 | (support) accepted |
| 0174-support-recursive-power-saving | exegenius-task | 8876 | 9.5 | 0 | (support) accepted |
| 0175-support-fast-address-interchange | exegenius-task | 9247 | 11.0 | 0 | (support) accepted |
| 0176-support-fast-butterfly-layers | exegenius-task | 9820 | 14.0 | 0 | (support) accepted |
| 0177-support-main-theorem | exegenius-task | 10449 | 9.7 | 0 | (support) accepted |
| 0178-write-radix-digit-reduction | exegenius-task | 38822 | 87.3 | 1 | b, y, y_j bindings dropped; reverted to previous text |
| 0179-write-poly-ring-y-r | exegenius-task | 49697 | 123.2 | 3 | y, r, j definitions missing; new opener; wrong directory |
| 0180-write-address-fields | exegenius-task | 30326 | 61.2 | 3 | m quote; added sentence; m used early |
| 0181-write-dft-fft | exegenius-task | 44683 | 110.4 | 1 | 350 over 313; f, g early; kept m, u, v |
| 0182-write-scratch-restoration | exegenius-task | 33248 | 67.2 | 1 | new claims; reverted; alpha to theta |
| 0183-write-address-shear-factorization | exegenius-task | 74605 | 200.2 | 2 | D used early; q clash; new claims |
| 0184-write-gaussian-resampling | exegenius-task | 80135 | 217.9 | 5 | .md relation ids; mu, pi, xi used early; uncited sentence |
| 0185-write-bluestein-chirp | exegenius-task | 86744 | 250.0 | 5 | new claims; j,k kept with note |
| 0186-write-phase-twist-convolution | exegenius-task | 45061 | 87.1 | 1 | X used early; xi binding added |
| 0187-write-signed-packing | exegenius-task | 95690 | 418.0 | 3 | symbols used early; .md id; new sentences |
| 0188-write-subset-intersection-construction | exegenius-task | 81313 | 206.6 | 2 | new claims; .md ids; restored wording |
| 0189-write-recursive-power-saving | exegenius-task | 83129 | 225.2 | 3 | g early; bindings for lambda and m dropped; leaf bound gap flagged |
| 0190-write-fast-butterfly-layers | exegenius-task | 97560 | 309.4 | 2 | new sentences; sigma, d bindings dropped; restored characters |
| 0191-write-main-theorem | exegenius-task | 91346 | 230.7 | 1 | new claims; reverted to previous wording |
| 0192-overloads | exegenius-task | 57831 | 73.8 | 0 | accepted (overloads) |
| 0193-support-poly-ring-y-r | exegenius-task | 9751 | 8.6 | 0 | (support) accepted |
| 0194-support-address-shear-factorization | exegenius-task | 9037 | 10.7 | 0 | (support) accepted |
| 0195-support-gaussian-resampling | exegenius-task | 8876 | 12.4 | 0 | (support) accepted |
| 0196-support-bluestein-chirp | exegenius-task | 9038 | 7.4 | 0 | (support) accepted |
| 0197-support-signed-packing | exegenius-task | 9416 | 6.0 | 0 | (support) accepted |
| 0198-support-subset-intersection-construction | exegenius-task | 9007 | 6.0 | 0 | (support) accepted |
| 0199-support-main-theorem | exegenius-task | 9810 | 7.9 | 0 | (support) accepted |
| 0200-write-radix-digit-reduction | exegenius-task | 29950 | 56.4 | 1 | y used early; new claims reverted |
| 0201-write-dft-fft | exegenius-task | 67180 | 201.3 | 3 | m, u kept, not renamed; restored text |
| 0202-write-gaussian-resampling | exegenius-task | 86694 | 239.9 | 4 | display names over four words; f early; .md ids; new sentence |
| 0203-write-bluestein-chirp | exegenius-task | 74032 | 200.0 | 2 | .md ids; display names; j kept, not renamed |
| 0204-write-ring-convolution-retained-order | exegenius-task | 66721 | 177.5 | 3 | new displays; t kept; quotes did not match |
| 0205-write-subset-intersection-construction | exegenius-task | 77738 | 207.7 | 2 | symbols used early; .md ids |
| 0206-write-recursive-power-saving | exegenius-task | 81843 | 201.1 | 3 | lambda, m bindings kept; C binding; leaf bound gap flagged |
| 0207-write-fast-address-interchange | exegenius-task | 66883 | 157.9 | 2 | tau binding kept; predicate over six words |
| 0208-write-fast-butterfly-layers | exegenius-task | 79393 | 207.8 | 1 | new claims; d, sigma bindings kept |
| 0209-write-main-theorem | exegenius-task | 100887 | 239.6 | 2 | n, kappa used early; new opener clause reverted; per-level argument not spelled out |
| 0210-support-radix-digit-reduction | exegenius-task | 9102 | 5.8 | 0 | (support) accepted |
| 0211-support-ring-convolution-retained-order | exegenius-task | 9132 | 14.5 | 0 | (support) accepted |
| 0212-support-fast-butterfly-layers | exegenius-task | 9174 | 11.3 | 0 | (support) accepted |

Notes on the table:
- 0114 is recorded as 4 rejections because its report says "3 times" and then a fourth quote mismatch.
- 0187 and 0125 durations are the wall-clock values from the harness notification.
- 0007 includes the hung background submit that I killed (see above).
