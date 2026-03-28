# Enterprise network configuration - Claude Code Docs

> Source: https://code.claude.com/docs/en/network-config

[Skip to main content](https://code.claude.com/docs/en/network-config#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Deployment

Enterprise network configuration

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Proxy configuration](https://code.claude.com/docs/en/network-config#proxy-configuration)
- [Environment variables](https://code.claude.com/docs/en/network-config#environment-variables)
- [Basic authentication](https://code.claude.com/docs/en/network-config#basic-authentication)
- [Custom CA certificates](https://code.claude.com/docs/en/network-config#custom-ca-certificates)
- [mTLS authentication](https://code.claude.com/docs/en/network-config#mtls-authentication)
- [Network access requirements](https://code.claude.com/docs/en/network-config#network-access-requirements)
- [Additional resources](https://code.claude.com/docs/en/network-config#additional-resources)

Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.

All environment variables shown on this page can also be configured in [`settings.json`](https://code.claude.com/docs/en/settings).

## [​](https://code.claude.com/docs/en/network-config\#proxy-configuration)  Proxy configuration

### [​](https://code.claude.com/docs/en/network-config\#environment-variables)  Environment variables

Claude Code respects standard proxy environment variables:

```
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

Claude Code does not support SOCKS proxies.

### [​](https://code.claude.com/docs/en/network-config\#basic-authentication)  Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.

## [​](https://code.claude.com/docs/en/network-config\#custom-ca-certificates)  Custom CA certificates

If your enterprise environment uses custom CAs for HTTPS connections (whether through a proxy or direct API access), configure Claude Code to trust them:

```
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

## [​](https://code.claude.com/docs/en/network-config\#mtls-authentication)  mTLS authentication

For enterprise environments requiring client certificate authentication:

```
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```

## [​](https://code.claude.com/docs/en/network-config\#network-access-requirements)  Network access requirements

Claude Code requires access to the following URLs:

- `api.anthropic.com`: Claude API endpoints
- `claude.ai`: authentication for claude.ai accounts
- `platform.claude.com`: authentication for Anthropic Console accounts

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.The native installer and update checks also require the following URLs. If you install Claude Code through npm or manage your own binary distribution, end users may not need access:

- `downloads.claude.ai`: CDN hosting the install script, version pointers, manifests, and executables
- `storage.googleapis.com`: legacy download bucket, deprecation in progress

[Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) and [Code Review](https://code.claude.com/docs/en/code-review) connect to your repositories from Anthropic-managed infrastructure. If your GitHub Enterprise Cloud organization restricts access by IP address, enable [IP allow list inheritance for installed GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps). The Claude GitHub App registers its IP ranges, so enabling this setting allows access without manual configuration. To [add the ranges to your allow list manually](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address) instead, or to configure other firewalls, see the [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses).

## [​](https://code.claude.com/docs/en/network-config\#additional-resources)  Additional resources

- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Environment variables reference](https://code.claude.com/docs/en/env-vars)
- [Troubleshooting guide](https://code.claude.com/docs/en/troubleshooting)

Was this page helpful?

YesNo

[Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry) [LLM gateway](https://code.claude.com/docs/en/llm-gateway)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.