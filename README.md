# Rust Agent Skills

Opinionated, reusable agent skills for writing and reviewing readable Rust
code. The repository is packaged as a skills-only Agent Plugin and can also be
used one skill at a time.

## Skills

- [`readable-rust`](skills/readable-rust/SKILL.md) applies focused readability
  conventions to Rust validation, errors, documentation, and Serde defaults.

## Install one skill

Ask Codex to install the skill from its versioned GitHub path:

```text
$skill-installer install from
https://github.com/aalexandrov/rust-agent-skills/tree/v0.1.0/skills/readable-rust
```

For repository-local use, copy the skill directory to
`.agents/skills/readable-rust` in the consuming repository.

## Develop locally

Link every skill in this checkout into the user-level Agent Skills directory:

```sh
./scripts/link-skills.sh
```

The command is idempotent: it leaves correct links unchanged and refuses to
overwrite an existing directory or a link to another source. Move or remove a
conflicting path under `~/.agents/skills`, then run the command again.

## Use

Invoke the skill explicitly when writing or reviewing Rust:

```text
Use $readable-rust while implementing this validation code.
```

Codex may also select the skill implicitly when a request matches its
description. Repository-local guidance takes precedence over conventions in
this collection.

## Add a skill

Create `skills/<skill-name>/SKILL.md` with `name` and `description` YAML
frontmatter. Keep each skill focused on one coherent job and add activation
examples under `evals/<skill-name>/`.

Run validation before opening a pull request:

```sh
python3 scripts/validate.py
```

## Versioning

The plugin uses semantic versions. Installation documentation points to Git
tags so consumers can choose when to adopt behavior changes.

## License

MIT
