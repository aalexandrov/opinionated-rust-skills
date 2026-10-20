---
name: document-flow
description: Document the high-level execution blocks of a Rust method or function with concise inline comments and single blank lines. Use when asked to annotate execution flow or separate its logical stages.
---

# Document Flow

Document the high-level blocks in the execution flow of the selected method or
function and separate blocks by a single blank line.

- Place a concise `//` comment immediately above each logical stage, explaining
  its purpose rather than narrating individual statements.
- Keep related statements together; use the actual control flow to choose block
  boundaries.
- Revise existing block comments where needed instead of duplicating them.
- Preserve behavior and limit edits to comments and whitespace in the selected
  code. Follow the repository's formatting conventions.
