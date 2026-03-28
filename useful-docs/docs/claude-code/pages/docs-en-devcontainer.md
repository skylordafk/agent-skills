# Development containers - Claude Code Docs

> Source: https://code.claude.com/docs/en/devcontainer

[Skip to main content](https://code.claude.com/docs/en/devcontainer#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Deployment

Development containers

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Key features](https://code.claude.com/docs/en/devcontainer#key-features)
- [Getting started in 4 steps](https://code.claude.com/docs/en/devcontainer#getting-started-in-4-steps)
- [Configuration breakdown](https://code.claude.com/docs/en/devcontainer#configuration-breakdown)
- [Security features](https://code.claude.com/docs/en/devcontainer#security-features)
- [Customization options](https://code.claude.com/docs/en/devcontainer#customization-options)
- [Example use cases](https://code.claude.com/docs/en/devcontainer#example-use-cases)
- [Secure client work](https://code.claude.com/docs/en/devcontainer#secure-client-work)
- [Team onboarding](https://code.claude.com/docs/en/devcontainer#team-onboarding)
- [Consistent CI/CD environments](https://code.claude.com/docs/en/devcontainer#consistent-ci%2Fcd-environments)
- [Related resources](https://code.claude.com/docs/en/devcontainer#related-resources)

The reference [devcontainer setup](https://github.com/anthropics/claude-code/tree/main/.devcontainer) and associated [Dockerfile](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile) offer a preconfigured development container that you can use as is, or customize for your needs. This devcontainer works with the Visual Studio Code [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/containers) and similar tools.The container’s enhanced security measures (isolation and firewall rules) allow you to run `claude --dangerously-skip-permissions` to bypass permission prompts for unattended operation.

While the devcontainer provides substantial protections, no system is completely immune to all attacks.
When executed with `--dangerously-skip-permissions`, devcontainers don’t prevent a malicious project from exfiltrating anything accessible in the devcontainer including Claude Code credentials.
We recommend only using devcontainers when developing with trusted repositories.
Always maintain good security practices and monitor Claude’s activities.

## [​](https://code.claude.com/docs/en/devcontainer\#key-features)  Key features

- **Production-ready Node.js**: Built on Node.js 20 with essential development dependencies
- **Security by design**: Custom firewall restricting network access to only necessary services
- **Developer-friendly tools**: Includes git, ZSH with productivity enhancements, fzf, and more
- **Seamless VS Code integration**: Pre-configured extensions and optimized settings
- **Session persistence**: Preserves command history and configurations between container restarts
- **Works everywhere**: Compatible with macOS, Windows, and Linux development environments

## [​](https://code.claude.com/docs/en/devcontainer\#getting-started-in-4-steps)  Getting started in 4 steps

1. Install VS Code and the Remote - Containers extension
2. Clone the [Claude Code reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) repository
3. Open the repository in VS Code
4. When prompted, click “Reopen in Container” (or use Command Palette: Cmd+Shift+P → “Remote-Containers: Reopen in Container”)

## [​](https://code.claude.com/docs/en/devcontainer\#configuration-breakdown)  Configuration breakdown

The devcontainer setup consists of three primary components:

- [**devcontainer.json**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/devcontainer.json): Controls container settings, extensions, and volume mounts
- [**Dockerfile**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/Dockerfile): Defines the container image and installed tools
- [**init-firewall.sh**](https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh): Establishes network security rules

## [​](https://code.claude.com/docs/en/devcontainer\#security-features)  Security features

The container implements a multi-layered security approach with its firewall configuration:

- **Precise access control**: Restricts outbound connections to whitelisted domains only (npm registry, GitHub, Claude API, etc.)
- **Allowed outbound connections**: The firewall permits outbound DNS and SSH connections
- **Default-deny policy**: Blocks all other external network access
- **Startup verification**: Validates firewall rules when the container initializes
- **Isolation**: Creates a secure development environment separated from your main system

## [​](https://code.claude.com/docs/en/devcontainer\#customization-options)  Customization options

The devcontainer configuration is designed to be adaptable to your needs:

- Add or remove VS Code extensions based on your workflow
- Modify resource allocations for different hardware environments
- Adjust network access permissions
- Customize shell configurations and developer tooling

## [​](https://code.claude.com/docs/en/devcontainer\#example-use-cases)  Example use cases

### [​](https://code.claude.com/docs/en/devcontainer\#secure-client-work)  Secure client work

Use devcontainers to isolate different client projects, ensuring code and credentials never mix between environments.

### [​](https://code.claude.com/docs/en/devcontainer\#team-onboarding)  Team onboarding

New team members can get a fully configured development environment in minutes, with all necessary tools and settings pre-installed.

### [​](https://code.claude.com/docs/en/devcontainer\#consistent-ci/cd-environments)  Consistent CI/CD environments

Mirror your devcontainer configuration in CI/CD pipelines to ensure development and production environments match.

## [​](https://code.claude.com/docs/en/devcontainer\#related-resources)  Related resources

- [VS Code devcontainers documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [Claude Code security best practices](https://code.claude.com/docs/en/security)
- [Enterprise network configuration](https://code.claude.com/docs/en/network-config)

Was this page helpful?

YesNo

[LLM gateway](https://code.claude.com/docs/en/llm-gateway)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.