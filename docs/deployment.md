# Deployment runbook

Status: Not configured. This template builds locally and in CI; it has no remote
deployment or publishing workflow. The CSV example is a batch CLI, not a web service.
Replace the prompts below with verified commands for the chosen platform.

## Target and ownership

Record the deployment operator, account/project ID, environment, region, registry,
billing owner, runtime identity, and any domain ownership. Separate staging and
production. Link to the authorization or agreed release process.

## Build and configuration

Record the source commit/tag, artifact name and immutable version/digest, supported
runtime, committed `uv.lock`, and exact build command. Use `uv sync --locked`
for installation and `uv run --locked` for project commands. For this
starter the local build is `docker build -t dsg-project:local .`.

List required variable names, purpose, secret-store locations, and the identity that
can read them. Record storage mounts, network access, and database migrations if
applicable. Do not record secret values. Pin production base images and dependencies
and define how updates are reviewed before treating a build as reproducible.

## Release procedure

1. Verify tests and artifact build for the intended commit.
2. Verify the target account/environment and required access.
3. Record any backup/migration prerequisites and the previous working artifact.
4. Run the platform-specific deployment command or workflow documented here.
5. Perform a smoke check of the actual deployed workload with synthetic input.
6. Record artifact, target, timestamp, operator, and observed result.

Replace this sequence with exact project commands and expected results. If GitHub
Actions is used, scope permissions and credentials to the selected target; use
protected environments for production according to the owner's release policy.
Do not inherit a registry namespace or deploy target from the template maintainers.

## Verification and operation

Record the job/endpoint to check, expected result, logs/metrics location, alert
recipient, failure thresholds, and how to stop or retry a failed job. For a service,
include health/readiness checks; for a batch job, include completion and output checks.
Document persistence, backup/restore, retention, and recurring costs where applicable.

## Rollback

Record exact commands to restore the previous artifact and configuration, who can
run them, when to roll back, and how recovery is verified. Explain migration/data
compatibility; redeploying an old image does not undo a database migration.
Record a rehearsal result or explicitly mark rollback as unverified.

## Release evidence

No release has been performed. Replace this with verified deployment and recovery
evidence; distinguish local tests, staging checks, and production checks.
