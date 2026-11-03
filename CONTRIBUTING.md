# Contributing

Use the setup, test, and container commands in [README.md](README.md). Keep changes
focused on the agreed deliverable in [the project brief](docs/project-brief.md).
Discuss scope changes with the project owner; routine fixes can go directly to a PR.

Use `uv add` / `uv add --dev` to manage dependencies and commit `uv.lock`.
After changing project metadata, run `uv lock`; verify with `uv sync --locked`.

Before submitting a pull request:

- Test the changed behavior and relevant failure paths with synthetic fixtures.
- Update configuration, run instructions, and operational records where affected.
- Describe the user-visible result, verification, and remaining limitations.
- Keep private data, credentials, generated artifacts, and local environments out of Git.

The project maintainer reviews changes before merging. Configure actual reviewers
and branch protection during client setup; this template does not invent owners.
Treat collaborators respectfully and raise conduct concerns privately with the
project lead recorded in the brief.
