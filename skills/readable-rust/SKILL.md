---
name: readable-rust
description: Apply opinionated Rust readability conventions when writing or reviewing Rust, especially validation, error design, documentation, and Serde defaults.
---

# Readable Rust

Apply these conventions when writing or reviewing Rust code:

- For repeated field checks that need to name the field in an error, prefer a
  small local rule-based macro over a runtime table of field-name strings and
  values. Use `stringify!` so the checked field and reported name cannot drift.
- In an error-handling block, bind a string longer than 10 characters to a
  local variable before passing it to a returned error variant. Prefer a short
  name such as `msg` when its role is clear.
- Describe intermediate raw or unchecked representations by their general
  validation role. Do not make their documentation specific to the checks that
  happen to exist today.
- For default values on fields of Serde-deserialized structs, prefer
  `serde-inline-default` so each default remains beside its field. Place
  `#[serde_inline_default]` before the Serde derive, annotate only fields that
  have defaults, and leave required fields unannotated. When adding the
  dependency is not justified, use a Serde default function that returns the
  value directly rather than pairing it with a single-use constant.
- Name error variants after the invalid condition they represent, such as
  `InvalidConfig`, rather than using an unspecific category such as `Config`.

Follow repository-local Rust guidance when it conflicts with or is more
specific than these conventions.
