# Client repository setup

- [ ] Record the client, DSG lead, receiving maintainer, scope, and acceptance criteria in [the brief](project-brief.md).
- [ ] Confirm the repository owner and visibility match the client agreement.
- [ ] Review the existing LICENSE and required attribution with the project owner.
- [ ] Replace this README's template onboarding with the client's purpose and quickstart.
- [ ] Rename `dsg-project-starter` (distribution), `src/dsg_project` (import package), and `dsg-project` (command) in pyproject.toml, imports/tests, Dockerfile, CI, and documentation.
- [ ] Replace the CSV example and fixtures with real application behavior and synthetic tests. Add data/notebook folders only if needed.
- [ ] For another stack, replace Python packaging, application, tests, container, and CI together; update AGENTS.md commands.
- [ ] Document actual configuration names in `.env.example` and how configuration is loaded.
- [ ] Keep `uv.lock` committed. Run `uv lock` after renaming the project; use `uv add` for dependencies and `uv lock --upgrade` for reviewed updates.
- [ ] Choose supported Python versions in `.python-version`, pyproject.toml, Dockerfile, and CI. Keep the uv version in CI and Dockerfile aligned when updating tooling. The build backend and container base require separate production pinning decisions.
- [ ] Configure maintainer access, reviewers/branch protection, and security reporting contact. Add CODEOWNERS only with real team/user handles.
- [ ] Verify a fresh environment can install, run tests, and build the artifact.
- [ ] Complete the deployment runbook before enabling publishing or deployment automation.
- [ ] Complete the handoff record before delivery; mark inapplicable sections with a reason for local or source-only tools.
- [ ] Remove `docs/template-release.md` from the client copy; it is for maintainers of this template.

Search for `dsg-project-starter`, `dsg_project`, and `dsg-project` to find starter
identifiers. Keep DSG workflow/skill names if useful. Remove this checklist once
its decisions are recorded in the project's maintained documentation.
