# DSG Python project template

A starting point for DSG teams building, deploying, and handing over Python
applications, command-line tools, and data pipelines to other people. It includes a runnable Python example, portable CI and container
builds, project records, and repository-local agent skills. Hosting, client
accounts, and publishing destinations are deliberately configured per project.

## Start a client repository

1. Choose **Use this template → Create a new repository** on GitHub, with the
   intended owner and visibility. If that button is unavailable, ask a maintainer
   to follow [the template release instructions](docs/template-release.md), or
   extract the supplied ZIP and initialize a new Git repository. Preserve hidden
   files: `.agents/`, `.github/`, `.gitignore`, `.dockerignore`, and `.env.example`.
2. Complete [the project brief](docs/project-brief.md): client, DSG lead, receiving
   maintainer, deliverable, acceptance criteria, data constraints, and hosting owner.
3. Follow [the setup checklist](docs/template-setup.md). Rename the starter, replace
   its example with the application, and keep the run and test commands accurate.
4. Run the checks below. Before the first deployment, complete
   [the deployment runbook](docs/deployment.md); finish with [the handoff](docs/handoff.md).

This is the Python starter, not a universal application scaffold. The project
records and agent skills can also be reused with another stack; replace `src/`,
`tests/`, `pyproject.toml`, `uv.lock`, `.python-version`, `Dockerfile`, and CI together in that case. Add `infra/`
or `deploy/` only when there is actual infrastructure or deployment code to maintain.

## Run locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first.
Python 3.12 is the default in `.python-version`; CI also checks 3.11 and 3.13.
uv manages the project environment and can download Python when needed. Initial
setup needs network access for Python and build dependencies. From the repository root:

```bash
uv sync --locked
uv run --locked dsg-project examples/sample.csv
uv run --locked python -m unittest discover -s tests -v
```

No manual environment creation or activation is needed. Commit `uv.lock` alongside
`pyproject.toml`. Use `uv add <package>` for runtime dependencies and
`uv add --dev <package>` for development tools. After renaming the project or
editing dependencies directly, run `uv lock` and commit the updated lockfile.
Use `uv lock --upgrade` for an intentional dependency refresh, then rerun tests.
CI and container builds use `--locked` so stale lockfiles fail instead of changing.
The lockfile tracks project dependencies; the build backend and Python base image
have separate version constraints and are not fully pinned by `uv.lock`.

The sample returns `{"columns": ["name", "value"], "rows": 2}`. It reads UTF-8 CSV,
checks header names and record widths, and outputs metadata without row values.
It is a replaceable example, not a complete client data-validation system.
It requires no credentials, environment variables, or service accounts.

## Build a container

```bash
docker build -t dsg-project:local .
docker run --rm dsg-project:local --help
docker run --rm --mount type=bind,source="$PWD/examples",target=/data,readonly dsg-project:local /data/sample.csv
```

The image runs as an unprivileged user. Mount input files at runtime; data and
secrets are excluded from the build context. CI tests the installed Python package
and builds and smoke-tests the container. No workflow publishes or deploys anything.
For production, choose an owned registry, record dependency and image versions,
and add the platform-specific deployment workflow using the runbook.

## Client data and optional folders

Create `data/` or `notebooks/` only when the project needs them. Local `data/` contents
are ignored by Git. Use `examples/` or `tests/fixtures/` for small synthetic fixtures.
Clear sensitive notebook outputs before committing, and keep reusable application
logic in `src/`. Record data access and retention decisions in the project brief.

## Work with an agent

Start with [AGENTS.md](AGENTS.md). Skills live in `.agents/skills/`, the
[repository skill location supported by Codex](https://learn.chatgpt.com/docs/build-skills).
Other agents can read the linked `SKILL.md` files directly if they do not discover them.

- [dsg-project-kickoff](.agents/skills/dsg-project-kickoff/SKILL.md): adapt this template to a client's scope and stack.
- [dsg-deployment](.agents/skills/dsg-deployment/SKILL.md): prepare, verify, and carry out an authorized deployment.
- [dsg-handoff](.agents/skills/dsg-handoff/SKILL.md): make the result maintainable by the receiving team.

Give the agent the client outcome and ownership information you already know:

```text
Read AGENTS.md and use dsg-project-kickoff to initialize this project.
Project name: <name>
Client and receiving maintainer: <organization / maintainer>
Required outcome: <what users should be able to do>
Acceptance criteria: <observable results>
Deployment target: <platform and account, or undecided>
Data constraints: <access, sensitivity, retention>
Replace the sample with the first useful application behavior. Update the brief,
README, tests, and CI together. Record unresolved decisions instead of inventing them.
```

The records in `docs/` are blank forms for each future client project, not claims
that this template has been deployed or accepted by a client. For a small local
tool, mark irrelevant operational sections not applicable with a brief reason.

## Layout

| Path | Purpose |
| --- | --- |
| `src/dsg_project/` | Replaceable Python application |
| `tests/` | Application and CLI tests |
| `examples/` | Small synthetic fixtures safe to share |
| `docs/` | Project brief, setup, deployment, and handoff records |
| `.agents/skills/`, `AGENTS.md` | Agent workflows and repository instructions |
| `.github/` | CI, issues, and pull request template |

See [CONTRIBUTING.md](CONTRIBUTING.md) for development expectations. The existing
[Apache-2.0 license](LICENSE) is retained; record the agreed client licensing and
attribution requirements during setup.
