---
name: dsg-deployment
description: Prepare or execute deployment of a DSG client project with an identified target, artifact, smoke checks, and recovery procedure. Use for release and deployment work, not ordinary local development.
---

# DSG deployment

Read root `AGENTS.md`, `docs/project-brief.md`, `docs/deployment.md`, and the current
build/workflow files. Check runbook commands against the actual implementation.

Identify whether the deliverable is a service, batch job, package, or static
artifact. Follow the client's chosen platform; do not add a default cloud provider
or reuse a template maintainer's registry/account. Confirm target identity from
available configuration without displaying credentials.

Prepare a concrete release before requesting any missing authorization:

- Run relevant tests and build the intended commit. Record an immutable artifact
  identifier and the dependency/base-image pinning strategy.
- Document configuration names, runtime identity, data storage, and network needs.
  Keep secrets in the chosen secret store; exclude client data from build contexts.
- Resolve applicable migration, backup, and rollback requirements. Include exact
  project commands and observable success/failure conditions.
- Implement deployment automation only for the identified target. Keep CI checks
  usable without production credentials and scope release credentials to their job.

Use authorization already supplied in the conversation. If the target or authority
is missing, stop before the affected external mutation and ask for the specific
missing decision, presenting the prepared artifact and procedure. Continue local
verification where useful. Do not add a confirmation loop to an authorized release.

After an authorized deployment, check the actual runtime using synthetic input or
an agreed safe smoke check. Record commit, artifact, target, time, and observations
in the runbook. If it fails, preserve diagnostic evidence without secrets and
follow the documented recovery procedure within authorization. Do not repeatedly
retry external mutations without understanding the failure; stop when recovery
requires a new decision or exceeds the agreed scope.

Report local build, staging, and production evidence separately. A successful
image build is not evidence of a successful deployment. Mark untested recovery
steps explicitly and carry remaining operational issues into `docs/handoff.md`.
