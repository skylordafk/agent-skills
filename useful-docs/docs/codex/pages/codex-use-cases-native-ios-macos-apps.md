# Build for iOS and macOS | Codex use cases

> Source: https://developers.openai.com/codex/use-cases/native-ios-macos-apps

## Search the Codex docs

Search docs

### Suggested

worktreesmcpnoninteractivesandbox

Primary navigation

Search docs

### Suggested

worktreesmcpnoninteractivesandbox

Docs  Use cases

- [Home](https://developers.openai.com/codex/use-cases)

[API Dashboard](https://platform.openai.com/login)

[← All use cases](https://developers.openai.com/codex/use-cases)

Use Codex to scaffold SwiftUI projects, keep the build loop CLI-first with `xcodebuild` or Tuist, and add XcodeBuildMCP or focused SwiftUI skills when the work gets deeper.

Advanced

1h

Related links

[Model Context Protocol](https://developers.openai.com/codex/mcp) [Agent skills](https://developers.openai.com/codex/skills)

## Best for

- Greenfield SwiftUI apps where you want Codex to scaffold the app and build loop from scratch
- Existing Apple-platform projects where Codex needs schemes, simulator output, screenshots, or UI automation before the work is done
- Teams that want long-running native UI tasks to stay agentic and CLI-first instead of depending on the Xcode GUI

## Skills & Plugins

- [Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)

Build or refactor SwiftUI UI, adopt modern iOS patterns such as Liquid Glass, audit runtime performance, and debug apps on simulators with XcodeBuildMCP-backed workflows.


## Starter prompt

Scaffold a starter SwiftUI app and add a build-and-launch script I can wire to a \`Build\` action in my local environment.

Constraints:
\- Stay CLI-first. Prefer Apple's \`xcodebuild\`; if a cleaner setup helps, it's okay to use Tuist.
\- If this repo already contains a full Xcode project, use XcodeBuildMCP to list targets, pick the right scheme, build, launch, and capture screenshots while you iterate.
\- Reuse existing models, navigation patterns, and shared utilities when they already exist.
\- Keep iOS and macOS compatibility intact unless I explicitly scope the work to one platform.
\- Use a small trustworthy validation loop after each change, then expand to broader builds only when the narrower check passes.
\- Tell me whether you treated this as a greenfield scaffold or an existing-project change.

Deliver:
\- the app scaffold or requested feature slice
\- a small build-and-launch script with the exact commands
\- the smallest relevant validation steps you ran
\- the exact scheme, simulator, and checks you used

[Open prompt in the Codex app](codex://new?prompt=Scaffold+a+starter+SwiftUI+app+and+add+a+build-and-launch+script+I+can+wire+to+a+%60Build%60+action+in+my+local+environment.%0A%0AConstraints%3A%0A-+Stay+CLI-first.+Prefer+Apple%27s+%60xcodebuild%60%3B+if+a+cleaner+setup+helps%2C+it%27s+okay+to+use+Tuist.%0A-+If+this+repo+already+contains+a+full+Xcode+project%2C+use+XcodeBuildMCP+to+list+targets%2C+pick+the+right+scheme%2C+build%2C+launch%2C+and+capture+screenshots+while+you+iterate.%0A-+Reuse+existing+models%2C+navigation+patterns%2C+and+shared+utilities+when+they+already+exist.%0A-+Keep+iOS+and+macOS+compatibility+intact+unless+I+explicitly+scope+the+work+to+one+platform.%0A-+Use+a+small+trustworthy+validation+loop+after+each+change%2C+then+expand+to+broader+builds+only+when+the+narrower+check+passes.%0A-+Tell+me+whether+you+treated+this+as+a+greenfield+scaffold+or+an+existing-project+change.%0A%0ADeliver%3A%0A-+the+app+scaffold+or+requested+feature+slice%0A-+a+small+build-and-launch+script+with+the+exact+commands%0A-+the+smallest+relevant+validation+steps+you+ran%0A-+the+exact+scheme%2C+simulator%2C+and+checks+you+used)

## Scaffold the app and build loop

For greenfield work, start with plain prompting. Ask Codex to scaffold a starter SwiftUI app and write a small build-and-launch script you can wire to a `Build` action in a [local environment](https://developers.openai.com/codex/app/local-environments).

Keep the loop CLI-first. Apple’s `xcodebuild` can list schemes and handle build, test, archive, `build-for-testing`, and `test-without-building` actions from the terminal, which lets Codex stay in an agentic loop instead of bouncing into the Xcode GUI.

If you want a cleaner project generator and you’re comfortable with third-party tooling, [Tuist](https://tuist.dev/) is a good next step. It can generate and build Xcode projects without needing the GUI, while still letting Codex build and launch the app from the terminal.

Use [XcodeBuildMCP](https://www.xcodebuildmcp.com/) once you’re inside a full Xcode project and need deeper automation. That’s when schemes, targets, simulator control, screenshots, logs, and UI interaction matter enough that plain shell commands stop being the whole story.

## Leverage skills

For the first pass, you often don’t need a skill or MCP server. Add skills once the work gets specialized or you want stronger SwiftUI conventions baked into the run.

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) is a strong general-purpose SwiftUI skill with a lot of best practices already baked in.

- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) is a broad SwiftUI review skill for modern APIs, maintainability, accessibility, and performance.

- [Liquid glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) allows the agent to understand how the new iOS and macOS 26 Liquid Glass API work and fix your components so they look good on the latest versions

- [SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) is a great skill to use almost anytime you have a performance issue or doubt about some code as it will scan for the most common SwiftUI mistakes humans or agents make and produce a report with a priority list of what to fix and where the biggest gains are.

- [Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) helps when cryptic errors and compiler warnings start fighting the change you want to make. On GPT-5.4, you may need it less often, but it’s still useful when Swift concurrency diagnostics get noisy.

- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) helps keep files smaller and make SwiftUI code more consistent across the repo.

- [SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) helps reach for predictable `@Observable` and `@Environment` architecture patterns as the app grows.


To learn more about how to install and use skills, see our [skills documentation](https://developers.openai.com/codex/skills).

## Iterate

Once you have a first pass working, or if you’re starting from an existing project, you can start iterating on the UI or behavior.

For this part, be specific about what you want to change and how you want to change it.

Make that prompting layer explicit: tell Codex whether it’s working in a greenfield repo or an existing Xcode project, which platforms must keep working, and what validation loop you expect.

### Example prompt

For example, if you want to add a feature to an existing app, you can ask Codex for a change like this:

Add the onboarding flow for this SwiftUI app.

Constraints:

\- Reuse existing models, navigation patterns, and shared utilities.
\- Use XcodeBuildMCP to list the right targets or schemes, build the app, launch it, and capture screenshots if you need visual verification.
\- Keep iOS and macOS compatibility intact unless I explicitly scope the work to one platform.
\- Tell me exactly which scheme, simulator, and checks you used.

Implement the slice, verify it with the smallest relevant build or run loop, and summarize what changed.

## Practical tips

### Start with basics

Start with plain prompting for greenfield work. Ask Codex to scaffold a starter SwiftUI app and write a small build-and-launch script you can wire to a `Build` action in a [local environment](https://developers.openai.com/codex/app/local-environments). For that first pass, you often don’t need any skill or MCP server.

### Use a small trustworthy validation loop

Tell Codex to run after each change the narrowest command that actually proves the contract you touched. Expand to broader builds later. This keeps Codex fast without pretending a full app build is required for every edit.

### Keep the loop CLI-first

Keep the loop CLI-first. Apple’s `xcodebuild` tool can list schemes and run build, test, archive, `build-for-testing`, and `test-without-building` actions from the terminal, which lets Codex stay in an agentic loop instead of bouncing into the Xcode GUI.

### Leverage XcodeBuildMCP

Use XcodeBuildMCP as soon as you are inside a full Xcode project and need deeper automation. That’s the point where schemes, targets, simulator control, screenshots, logs, and UI interaction matter enough that plain shell commands stop being the whole story.

## Tech stack

Need

Default options

Why it's needed

Need

UI framework

Default options

[SwiftUI](https://developer.apple.com/xcode/swiftui/)

Why it's needed

The fastest way to prototype views, navigation, and shared state across Apple platforms while keeping the UI code readable.

Need

Build tooling

Default options

xcodebuild or [Tuist](https://docs.tuist.dev/)

Why it's needed

Both keep the native build loop in the terminal instead of depending on the Xcode GUI.

Need

Project automation

Default options

[XcodeBuildMCP](https://www.xcodebuildmcp.com/)

Why it's needed

A strong option once you need Codex to inspect schemes and targets, launch the app, capture screenshots, and keep iterating without leaving the agentic loop.

Need

Distribution tooling

Default options

[App Store Connect CLI](https://asccli.sh/)

Why it's needed

Keep your agent fully in the loop and send your app build directly to the App Store.

## Related use cases

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**Bring your app to ChatGPT**\\
\\
Build one narrow ChatGPT app outcome end to end: define the tools, scaffold the MCP server... \\
\\
Integrations  Code](https://developers.openai.com/codex/use-cases/chatgpt-apps) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**Create browser-based games**\\
\\
Use Codex to turn a game brief into first a well-defined plan, and then a real browser-based... \\
\\
Engineering  Code](https://developers.openai.com/codex/use-cases/browser-games) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**Iterate on difficult problems**\\
\\
Give Codex an evaluation system, such as scripts and reviewable artifacts, so it can keep... \\
\\
Engineering  Analysis](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems)