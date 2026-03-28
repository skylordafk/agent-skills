# Operating Principles

1. **Do not attempt to resolve every issue.** Fewer things done well beats maximizing closed issues.
2. **If you are not confident in a fix, defer it.** A wrong fix is worse than an open issue.
3. **Verify against current code.** Pull latest, read the files. If the issue describes something that doesn't exist, close it.
4. **Document for the next agent, not yourself.** Assume the next person has never seen this codebase.
5. **Every fix moves toward ideal state.** Say which dimension.
6. **No new dependencies** without strong justification.
7. **No drive-by refactors.** Open a new issue instead.
8. **Small PRs.** One concern per PR. If touching more than 5-7 files, you're probably doing too much.
9. **Don't break the build.** Run existing tests and linting before submitting.
10. **When uncertain, defer.** A thoughtful comment is more valuable than a bad fix.
