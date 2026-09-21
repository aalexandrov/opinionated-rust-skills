#!/bin/sh

set -eu

script_dir=$(CDPATH= cd "$(dirname "$0")" && pwd)
repository_root=$(dirname "$script_dir")
skills_root="$repository_root/skills"

: "${HOME:?HOME must be set}"
destination_root=${AGENTS_SKILLS_DIR:-"$HOME/.agents/skills"}

skill_count=0
conflict_count=0

# Check every destination before creating anything so a conflict cannot leave a
# partially linked installation.
for source_dir in "$skills_root"/*; do
    [ -d "$source_dir" ] || continue
    [ -f "$source_dir/SKILL.md" ] || continue

    skill_count=$((skill_count + 1))
    skill_name=${source_dir##*/}
    destination="$destination_root/$skill_name"

    if [ -L "$destination" ] && [ "$destination" -ef "$source_dir" ]; then
        continue
    fi

    if [ -e "$destination" ] || [ -L "$destination" ]; then
        printf 'error: %s already exists and does not link to %s\n' \
            "$destination" "$source_dir" >&2
        conflict_count=$((conflict_count + 1))
    fi
done

if [ "$skill_count" -eq 0 ]; then
    printf 'error: no skills found under %s\n' "$skills_root" >&2
    exit 1
fi

if [ "$conflict_count" -ne 0 ]; then
    printf 'Move or remove the conflicting paths, then run this script again.\n' >&2
    exit 1
fi

mkdir -p "$destination_root"

for source_dir in "$skills_root"/*; do
    [ -d "$source_dir" ] || continue
    [ -f "$source_dir/SKILL.md" ] || continue

    skill_name=${source_dir##*/}
    destination="$destination_root/$skill_name"

    if [ -L "$destination" ] && [ "$destination" -ef "$source_dir" ]; then
        printf 'Already linked: %s -> %s\n' "$destination" "$source_dir"
        continue
    fi

    ln -s "$source_dir" "$destination"
    printf 'Linked: %s -> %s\n' "$destination" "$source_dir"
done
