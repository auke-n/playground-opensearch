# Repository Instructions

## Language

- Communicate with the user in Ukrainian.
- Write source code, configuration, documentation intended for project users, commit messages, and code comments in English.

## Context-driven development

- Treat `docs/context/` as the durable project context.
- Before material implementation work, read the applicable context documents, requirements, architecture decisions, and backlog items.
- After a material decision, scope change, assumption, risk discovery, or implementation milestone, update the relevant document in `docs/context/` in the same change.
- Record irreversible or consequential technical decisions as an ADR in `docs/adr/` using the next sequential identifier.
- Keep `docs/backlog.md` current: move completed items, add discovered work, and link work to requirements and ADRs where applicable.
- Do not duplicate volatile operational status in this file; keep it in `docs/context/project-state.md`.

## Engineering practices

- Prefer small, reviewable changes with verification appropriate to the risk.
- Keep infrastructure reproducible and minimize cloud cost by default.
- Never commit credentials, private keys, state files, or other secrets. Provide `.example` files and document required inputs instead.
- Update documentation alongside user-visible behavior, architecture, and operational changes.
