#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text().splitlines()
    if not lines or lines[0] != "---":
        fail(f"{path.relative_to(ROOT)} has no YAML frontmatter")

    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(f"{path.relative_to(ROOT)} has unterminated YAML frontmatter")

    values: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()
    return values


def validate_manifest() -> None:
    manifest = json.loads((ROOT / "plugin.json").read_text())
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("plugin.json does not declare the Agent Plugins 1.0.0 schema")
    if manifest.get("name") != ROOT.name:
        fail("plugin name must match the repository directory")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")):
        fail("plugin version must use semantic versioning")

    compatibility = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
    for field in ("name", "version", "description"):
        if compatibility.get(field) != manifest.get(field):
            fail(f"compatibility manifest has a different {field}")


def validate_skills() -> None:
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_files:
        fail("no skills found")

    for skill_file in skill_files:
        metadata = frontmatter(skill_file)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not NAME_PATTERN.fullmatch(name):
            fail(f"{skill_file.relative_to(ROOT)} has an invalid name")
        if skill_file.parent.name != name:
            fail(f"{skill_file.relative_to(ROOT)} name does not match its directory")
        if not description:
            fail(f"{skill_file.relative_to(ROOT)} has no description")


def main() -> None:
    validate_manifest()
    validate_skills()
    print("Plugin and skills are valid.")


if __name__ == "__main__":
    main()
