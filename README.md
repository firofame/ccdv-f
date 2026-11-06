# Anthropic Claude Certified Developer - Foundations (CCDV-F) Portal

> **Interactive Certification Player, 117 Video Topics, 28 Follow-Along Labs, Domain Progress Tracking & Timestamped Markdown Notes.**

🚀 **Live Deployment:** [https://firofame.github.io/ccdv-f/](https://firofame.github.io/ccdv-f/)

A distraction-free, workplace-ready study portal built for engineers preparing for the **Anthropic Claude Certified Developer – Foundations (CCDV-F)** certification exam.

Based on the official exam curriculum presented by **Andrew Brown (ExamPro)** on **freeCodeCamp** (Video ID: `C_1QKZAcJjk`, total duration: 7h 47m).

---

## Table of Contents
1. [Quick Start & Local Development](#quick-start--local-development)
2. [Why Run a Local Server? (YouTube Error 153)](#why-run-a-local-server-youtube-error-153)
3. [CCDV-F Exam Overview & Blueprint](#ccdv-f-exam-overview--blueprint)
4. [Domain-by-Domain Curriculum (21 Domains, 117 Topics)](#domain-by-domain-curriculum)
5. [The 28 Follow-Along Hands-On Labs Checklist](#the-28-follow-along-hands-on-labs-checklist)
6. [Core Architectural & Engineering Cheatsheet](#core-architectural--engineering-cheatsheet)
7. [Portal Capabilities & Features](#portal-capabilities--features)
8. [Keyboard Shortcuts](#keyboard-shortcuts)

---

## Quick Start & Local Development

### 1. Launch with Python 3 (Recommended)
Run a local HTTP static server in this repository folder:
```bash
python3 -m http.server 8000
```
Open your browser to:
```
http://localhost:8000
```

### 2. Alternative Static Servers
- **Node.js (npx):**
  ```bash
  npx serve .
  ```
- **Bun:**
  ```bash
  bun x serve .
  ```
- **VS Code:** Install the **Live Server** extension (by Ritwick Dey), right-click `index.html`, and select *Open with Live Server*.
- **Docker:**
  ```bash
  docker run --rm -p 8000:80 -v "$PWD":/usr/share/nginx/html:ro nginx:alpine
  ```

---

## Why Run a Local Server? (YouTube Error 153)

> [!WARNING] **YouTube Embed Error 153 Explained**
> If you double-click `index.html` directly from your file manager, it loads with the `file://` protocol (`file:///.../index.html`).
>
> Modern browser security and YouTube's iframe embed policy require a valid `http://` or `https://` origin header to establish iframe communication, prevent clickjacking, and enable the YouTube Player JavaScript API (`enablejsapi=1`). When loaded over `file://`, YouTube blocks playback and renders **Error 153** ("Video player configuration error").
>
> Serving via `python3 -m http.server 8000` provides an `http://localhost:8000` origin, resolving the issue instantly.

---

## CCDV-F Exam Overview & Blueprint

The **Anthropic Claude Certified Developer – Foundations (CCDV-F)** credential is designed for software engineers, AI developers, and technical architects building and operating applications powered by Claude models.

Unlike purely theoretical multiple-choice tests, CCDV-F focuses heavily on **practical engineering judgment**, **agent loop mechanics**, **tool calling schemas**, **Model Context Protocol (MCP)** integrations, **prompt caching economics**, and **Claude Code CLI** operations.

### Key Exam Specifications:
* **Target Audience:** Developers building AI agents, API integrations, and developer tooling.
* **Format:** Hands-on code analysis, architecture scenario decisions, tool schema evaluation, and practical configuration exercises.

---

## Domain-by-Domain Curriculum

The certification course covers **21 structured domains** containing **117 discrete topics**:

| Code | Domain Title | Topics | Follow-Along Labs | Primary Focus |
|:---:|:---|:---:|:---:|:---|
| **000** | **Orientation & Introduction** | 2 | 0 | Course roadmapping & official exam blueprint analysis |
| **010** | **Agent Architecture** | 4 | 0 | Single vs multi-agent patterns, workflows, subagents |
| **020** | **Agent Construction with Claude** | 6 | 3 | Agent SDK, code harnesses, `PreToolUse` & `PostToolUse` hooks |
| **030** | **Agent Patterns and Frameworks** | 2 | 0 | The Agentic Loop, state machines, tool iteration |
| **040** | **Claude API Mechanics** | 12 | 2 | Messages API, system prompts, streaming, image reasoning, batch processing, prompt caching |
| **050** | **Software Engineering Foundations** | 5 | 0 | Semi-structured JSON, VCS hygiene, code review, simplify commands |
| **060** | **Claude Application Design** | 4 | 0 | Surfaces, content boundaries, session hygiene, plugins |
| **070** | **Configuration Management** | 5 | 0 | `CLAUDE.md` syntax, settings scopes, model version pinning |
| **080** | **Claude Code Operations** | 24 | 10 | Rules, skills, `/resume`, `/fork`, `/rewind`, subagents, auto-memory, headless execution |
| **090** | **Debugging and Error Handling** | 2 | 1 | Debug mode, error stack diagnosis, tool recovery |
| **100** | **LLM Fundamentals** | 10 | 2 | Tokens, context window limits, sampling parameters, temperature, `/fast` mode, `/effort` tuning |
| **110** | **Model Selection and Tradeoffs** | 3 | 0 | Agentic loop model trade-offs, adaptive thinking vs extended thinking |
| **120** | **Cost and Token Management** | 3 | 0 | Token Count API, cost modeling, prompt caching unit economics |
| **130** | **Context Engineering** | 3 | 1 | Tool output pruning, context window reclamation, `/compact` & `/clear` |
| **140** | **Prompt Engineering** | 5 | 1 | Explicit criteria, few-shot prompting, structured JSON schema enforcement, refinement loops |
| **160** | **AI Application Security** | 2 | 0 | Prompt injection mitigation, data leakage prevention, PII masking |
| **170** | **Guardrails and Safe Deployment** | 6 | 3 | Permission rules, process sandboxing, security hooks |
| **180** | **Identity, Secrets & Key Management**| 4 | 1 | API key lifecycle, permission modes, authentication vs authorization |
| **190** | **Tool Implementation** | 5 | 1 | Tool definitions, descriptions, error handling, agent tools |
| **200** | **MCP Server Deployment** | 5 | 1 | Model Context Protocol, Resources vs Tools vs Prompts, AWS setup |
| **210** | **Agent Customization** | 5 | 2 | Built-in tools, custom tool authoring, dynamic MCP discovery |
| **TOTAL** | **21 Domains** | **117 Topics** | **28 Labs** | **Comprehensive Full-Spectrum Mastery** |

---

## The 28 Follow-Along Hands-On Labs Checklist

Every lab is equipped with instant seeking in the portal and can be tracked individually:

1. `[020]` **01:11:47** — **Agent SDK Follow Along** (Setting up the core SDK client and agent scaffold)
2. `[020]` **01:19:17** — **PreToolUse and PostToolUse Hooks Follow Along** (Intercepting and sanitizing tool payloads)
3. `[020]` **01:23:28** — **Claude Managed Agents Follow Along** (Configuring managed autonomous workflows)
4. `[040]` **02:01:14** — **Claude Code Image Reasoning Follow Along** (Multimodal inputs & visual debugging)
5. `[040]` **02:09:40** — **Batch Processing Follow Along** (Asynchronous bulk message evaluation at 50% discount)
6. `[080]` **03:06:51** — **Claude Rules Follow Along** (Configuring rule files for deterministic coding behavior)
7. `[080]` **03:21:49** — **Skills Follow Along** (Authoring and invoking custom reusable agent skills)
8. `[080]` **03:33:30** — **Resume Command Follow Along** (Restoring and continuing past session states)
9. `[080]` **03:38:20** — **Fork Session Follow Along** (Branching conversation states to test alternative approaches)
10. `[080]` **03:43:14** — **Rename and Rewind Follow Along** (Navigating history points and rolling back mutations)
11. `[080]` **03:51:25** — **Sub agents Follow Along** (Spawning specialized subagents for isolated task execution)
12. `[080]` **04:02:13** — **Claude Auto Memory Follow Along** (Persistent project memory across multiple runs)
13. `[080]` **04:09:06** — **Headless Tasks Follow Along** (Running automated background workflows without UI interaction)
14. `[080]` **04:17:51** — **Enable Auto Mode Follow Along** (Autonomous tool permission elevation)
15. `[080]` **04:24:17** — **Claude files Follow Along** (Project-level configuration file hierarchies)
16. `[090]` **04:39:25** — **Debug Mode Follow Along** (Tracing raw message payloads, token counts, and API errors)
17. `[100]` **04:53:12** — **Fast Mode Follow Along** (Optimizing for low latency in rapid iterations)
18. `[100]` **04:58:42** — **Effort Follow Along** (Balancing reasoning compute against response velocity)
19. `[130]` **05:22:05** — **Compact and Clear Follow Along** (Context compression and session state resetting)
20. `[140]` **05:33:58** — **Refinement Loop Follow Along** (Iterative self-correction with structured test evaluation)
21. `[170]` **05:55:31** — **Permission Rules Follow Along** (Enforcing granular allow/deny filters on system calls)
22. `[170]` **06:12:03** — **Sandbox Follow Along** (Containerizing agent code execution for untrusted tasks)
23. `[170]` **06:21:33** — **Security Hook Follow Along** (Enforcing strict DLP and credential exposure checks)
24. `[180]` **07:01:33** — **Permission Modes Follow Along** (Configuring Plan Mode vs Execution Mode)
25. `[190]` **07:14:22** — **Agent Tool Follow Along** (Creating robust tool definitions with JSON schema validation)
26. `[200]` **07:29:12** — **MCP Resources vs Tools Follow Along** (Building and testing Model Context Protocol primitives)
27. `[210]` **07:41:06** — **Built In Tools Follow Along** (Harnessing Claude Code's native filesystem and command tools)
28. `[210]` **07:46:06** — **MCP Discovery Follow Along** (Configuring dynamic server discovery and capability negotiation)

---

## Core Architectural & Engineering Cheatsheet

### 1. The Agentic Loop
```
User Prompt / Task
        │
        ▼
   Claude Model  ────────► Generates tool_use block (e.g. name, input JSON)
        ▲
        │
   [PreToolUse Hook]     ── (Policy checks, schema verification, security approval)
        │
        ▼
   Code Harness          ── (Executes bash command, reads file, calls API)
        │
        ▼
   [PostToolUse Hook]    ── (Sanitizes PII, trims oversized output, handles exceptions)
        │
        ▼
   tool_result block     ── Appended back into conversation messages
        │
        └─────────────────► Model evaluates result & either produces final text or next tool_use
```

### 2. Prompt Caching Economics
* **Cache Lifetime:** 5-minute sliding TTL. Every cache hit refreshes the TTL for an additional 5 minutes.
* **Minimum Token Threshold:** Meets model-specific prompt caching threshold requirements for prefix caching.
* **Financial Impact:** Cached tokens enjoy up to a **90% discount** compared to standard base input token pricing.
* **Implementation:** Designate static prefixes (system instructions, tool definitions, documentation reference blocks) with:
  ```json
  "cache_control": { "type": "ephemeral" }
  ```

### 3. Model Context Protocol (MCP) Triad
* **Resources:** Static or dynamic URI-addressable data (e.g. `file:///schema.sql`, `postgres://db/table`). Read-only contexts provided to the LLM.
* **Tools:** Executable endpoints with input schemas (`call_tool`) that execute side effects or live lookups.
* **Prompts:** Reusable, parameterized interaction templates registered on the server.
* **Supported Transports:** `stdio` (local subprocess standard streams) and `streamable-http` (Streamable HTTP).

### 4. Claude Code CLI Commands
* `/compact` — Compress earlier conversation turns to avoid context overflow while preserving critical task context.
* `/clear` — Erase current session state and scratchpad memory for a fresh start.
* `/resume` — Reopen and continue a previous session by session ID.
* `/fork` — Create an isolated copy of current state to explore speculative changes.
* `/rewind` — Rollback previous file edits or agent state transitions.
* `/context` — Display visual token consumption breakdown across tools, messages, and memory.
* `/fast` & `/effort` — Dynamically tune the thinking budget and speed/quality trade-off.

---

## Portal Capabilities & Features

1. **Instant Seeking Across All 117 Topics & 28 Labs:**
   * Powered by the YouTube IFrame API (`seekTo(seconds, true)`).
   * Fallback message dispatching ensures zero broken links even during slow network conditions.
2. **Domain-by-Domain Progress Tracking:**
   * Interactive checkboxes for every topic.
   * Per-domain progress counters (`completed/total` + progress bar) and global readiness indicator.
   * State automatically persisted in browser `localStorage`.
3. **Real-Time Search & Lab Filter:**
   * Instant search across topic titles, domain titles, and domain codes.
   * One-click **"Follow-Along Labs Only"** toggle to isolate hands-on exercises.
   * Auto-expansion of matching domains during searches.
4. **Interactive Timestamped Markdown Notes:**
   * Autosaved scratchpad with dual **Edit** and **Preview** modes.
   * **Insert Current Timestamp:** One-click button (or <kbd>Alt + T</kbd>) captures exact playback time (e.g. `[02:01:14]`).
   * **Clickable Deep-Links:** All timestamps in notes render as clickable chips (`▶ 02:01:14`) that jump directly to that point in the lecture!
   * **Export to .md:** Downloads your notes formatted with timestamp metadata and progress tracking.
5. **Exam Quick Reference Cheatsheet:**
   * Built-in reference cards for prompt caching, Agent SDK hooks, MCP architecture, CLI commands, guardrails, and model selection.
6. **Theater & Theme Modes:**
   * Theater mode (<kbd>T</kbd>) expands the video player to full screen width.
   * Dark / Light theme toggle (<kbd>D</kbd>) with high-contrast accessibility.

---

## Keyboard Shortcuts

| Shortcut | Action | Context |
|:---:|:---|:---|
| <kbd>T</kbd> | Toggle Theater Mode | Global (when not typing in notes) |
| <kbd>D</kbd> | Toggle Light / Dark Mode | Global (when not typing in notes) |
| <kbd>Alt + T</kbd> | Insert Current Video Timestamp (`[hh:mm:ss]`) | Everywhere |
| <kbd>Space</kbd> / <kbd>K</kbd> | Play / Pause Video | Player active |
| <kbd>J</kbd> | Rewind 10 seconds | Global |
| <kbd>L</kbd> | Fast-forward 10 seconds | Global |
| <kbd>F</kbd> | Toggle Fullscreen | YouTube Player active |

---

*Anthropic Claude Certified Developer - Foundations (CCDV-F) Interactive Study Portal. Developed with zero external runtime dependencies.*
