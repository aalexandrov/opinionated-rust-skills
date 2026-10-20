---
name: implement-issue-incrementally
description: Implement an issue on the current branch, one description-list item per commit, stopping before each commit for review. Use when asked for this incremental issue workflow with brief documentation and concise progress updates.
---

# Implement Issue Incrementally

Input: `<issue>` is the issue URL or identifier supplied by the user. For example:
`Use $implement-issue-incrementally <issue>`.

Read the supplied issue and work on top of the current branch. Treat each
implementation item in its description list as one coherent commit containing
its code, relevant tests, and required documentation.

- Inspect the current branch, existing changes, repository guidance, and relevant
  coverage before implementing. Preserve unrelated work.
- Work on one issue item at a time, following the list order unless dependencies
  require a different order. Do not mix items in one commit or accumulate later
  items in the diff awaiting review.
- Complete the item and its proportionate validation before stopping for review.
  Report briefly what changed and what passed, then wait before committing.
- Address review feedback within that item's diff. Commit only after the user
  approves that commit; approval for one item does not approve subsequent commits.
  After committing, continue with the next item unless the user directs otherwise.
- Keep `./docs` changes brief while satisfying repository documentation requirements.
  Keep progress and handoff messages concise and focused on outcomes and validation;
  discuss implementation details only when requested or needed for a decision.

If the issue cannot be read or has no clear implementation list, ask for the
missing description or item boundaries. If one item needs multiple commits to
meet an explicit issue or repository constraint, agree on that split before
changing the requested commit structure. Do not infer permission to push or open
a pull request from this workflow.
