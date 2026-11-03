# Distributing the DSG Python template

This document is for template maintainers. Client teams start at the root README
and use the project brief, setup checklist, deployment runbook, and handoff form.
Those blank forms are intentionally completed separately for each client.

## Contents and scope

The template delivers a Python package with a replaceable CSV CLI, application
tests, an unprivileged container, CI, and three repository-local agent skills.
It does not include client infrastructure, credentials, deployment destinations,
or automatic publishing. Keep the existing LICENSE with redistributed copies.

## Publish the repository template

1. Review and commit the intended files, including `.agents/` and `.github/`.
2. Push the reviewed change and confirm the Python and container CI jobs pass.
3. Enable **Template repository** in the repository settings if needed. This is a
   GitHub setting, not a property that files in the repository can enable.
4. Share the repository link with instructions to use **Use this template**.
   Verify the recipient can access it; choose visibility according to the agreed audience.

Do not label container verification complete until its CI job has actually passed.
Tag a reviewed revision if recipients need a stable version to refer to. No
publication, release tag, or repository-setting change is performed by local tests.

## ZIP delivery

A source ZIP is also usable without the GitHub template setting. Include all
maintained source, `uv.lock`, documentation, and hidden configuration/skill files; exclude
`.git/`, virtual environments, caches, build outputs, and local data or secrets.
A Python wheel alone is not a substitute: it omits the repository workflows and
agent skills. Recipients should extract the ZIP, initialize Git if needed, and
follow README.md. Do not distribute a developer's entire working directory.

## Verify a candidate

From a clean extracted copy, run `uv sync --locked`,
`uv run --locked python -m unittest discover -s tests -v`, and
`uv run --locked dsg-project examples/sample.csv`. Expect two records and the columns `name` and
`value`. Follow README.md for the container build and smoke test. Check that all
three `.agents/skills/*/SKILL.md` files are present and linked from AGENTS.md.

Record the verification results and any unavailable checks in the delivery
message. Client acceptance, hosting ownership, and deployment evidence belong in
the client copy, not in this template's blank forms.
