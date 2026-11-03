# Working in a DSG client repository

Read `README.md` for commands and `docs/project-brief.md` for scope and ownership.
This is a reusable template until that brief is completed. Unfilled fields mean
unknown, not permission to invent client names, accounts, infrastructure, or approvals.

## Repository skills

Read the relevant skill when the task calls for its workflow:

- `.agents/skills/dsg-project-kickoff/SKILL.md` — initialize or adapt a client project.
- `.agents/skills/dsg-deployment/SKILL.md` — prepare or perform a deployment.
- `.agents/skills/dsg-handoff/SKILL.md` — prepare delivery and operational handoff.

These files are usable directly by agents without automatic skill discovery.
Routine implementation changes do not require running every workflow.

## Implementation and verification

- Follow the client's chosen stack and existing architecture. The Python CSV
  example is disposable; remove it when real application behavior replaces it.
- Keep setup and test commands in README.md synchronized with CI. For this starter:
  `uv sync --locked` and `uv run --locked python -m unittest discover -s tests -v`.
- Use uv for dependencies and execution. Commit `uv.lock` with dependency or
  project-name changes; regenerate it with `uv lock` rather than editing it by hand.
- Add tests for meaningful changed behavior, including relevant failure paths.
  State exactly what ran and what could not be checked.
- Keep real data, secrets, credentials, and customer identifiers out of fixtures,
  logs, screenshots, commits, and container layers. Use synthetic test data.
- Document changed configuration names in `.env.example`; it contains no real values.
- Update the deployment or handoff record when operational behavior changes.

## Delivery boundaries

Work within the user's authorized scope. Existing authorization carries forward;
local preparation and verification do not require an extra confirmation.
Before an external mutation, establish the intended account, project, environment,
and action from the brief and conversation. Ask only for unresolved decisions or
missing authorization. A deployment request does not by itself authorize making
data public, creating unrelated paid resources, or deleting existing resources.
Never report a successful deployment based only on a build or simulated check.
