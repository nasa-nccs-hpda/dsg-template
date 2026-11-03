---
name: dsg-project-kickoff
description: Adapt the DSG repository template for a new client project, including scope, ownership, stack, and working build/test commands. Use for initial setup or a deliberate project rebaseline, not routine feature edits.
---

# DSG project kickoff

Read root `AGENTS.md`, `README.md`, `docs/project-brief.md`, and
`docs/template-setup.md`. Use the brief as the maintained decision record.

Establish the client outcome, receiving maintainer, acceptance criteria, repository
visibility, data constraints, and preferred stack from the request and existing
records. Mark unknowns with an owner and next action. Ask only about decisions
that materially block the work; continue independent setup with stated assumptions.
Do not invent a DSG organizational policy, client account, hosting target, or license.

Adapt the starter as one consistent change:

- Choose project-specific distribution, import package, and command names. Update
  their callers in tests, packaging, container, CI, and docs together.
- Replace example behavior with the smallest useful slice of the agreed application.
  When changing stacks, replace the Python starter and its checks together.
- Keep only dependencies and infrastructure the deliverable needs. Record why the
  receiving team can run and maintain the chosen stack.
- Replace template README onboarding with actual setup, configuration, run, and
  test commands. Keep `.env.example` limited to names and safe example values.
- Record ownership and unresolved hosting decisions in the brief/runbook. Prepare
  deployment files when in scope; setup alone does not authorize creating paid
  resources or publishing artifacts.

Verify installation and a representative operation from a fresh environment,
then run relevant tests and artifact builds. Search for old starter names and
stale links. Report what was customized, evidence of a runnable project, and
remaining client decisions. Keep incomplete checklist items visibly incomplete.
