---
name: dsg-handoff
description: Prepare a DSG client delivery for another team to own and operate, with acceptance evidence, reproducible setup, operational ownership, and known limitations. Use when preparing handoff or reviewing delivery readiness.
---

# DSG client handoff

Read root `AGENTS.md`, `docs/project-brief.md`, `README.md`, `docs/deployment.md`,
and `docs/handoff.md`. Update the existing handoff record.

Compare agreed deliverables and acceptance criteria against the application and
release evidence. Distinguish implemented, verified, accepted, and unresolved:
passing tests does not imply client acceptance.

Verify the receiving team's path from checkout to a representative run. Where
possible, use a fresh environment and synthetic data. Check documented commands,
configuration names, required access, runtime versions, and artifact locations.
Report missing tooling or inaccessible targets as verification limits.

For an operated deployment, inspect the actual release and rollback record,
monitoring/support ownership, persistent data and backup requirements, recurring
cost owner, and migration constraints. For a source-only delivery, explicitly
mark deployment-specific items not applicable with a reason.

Record who owns the repository, hosting, registry, domains, data, and maintenance
after delivery. Link to access-controlled records for sensitive information.
Document how access should be transferred; do not change account ownership, send
messages, or distribute credentials merely because a handoff was requested.
Perform those external actions only when explicitly authorized.

Provide the receiving maintainer with verified commands, acceptance evidence,
known limitations, open issues with owners, and support-period expectations.
Leave missing client acceptance and untested operational steps visible. Finish
with an evidence-based readiness assessment and the specific remaining items
that prevent the agreed handoff.
