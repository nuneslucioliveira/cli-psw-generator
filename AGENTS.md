# AGENTS.md

## Overview

This scaffold applies SDD to CLI Password Generator.

## Hardware Topology & Causal Disentanglement

### Node A (RTX 3090, 24GB)

Hosts deterministic role execution via strict privilege separation.

- **@architect** is isolated to Executive Intelligence (EI) for the Plan phase.
- **@coder** is isolated to Executive Execution (EEX) for the Implement phase.

### Node B (RTX 3060, 12GB)

Reserved for **@companion**. Low-latency AIP Gate, enforcing schema conformance, format forcing, and orchestration logic.

## Blocking Rules & FSM Isolation

1. **Status Transition Blocker:** Do not move to the next SDD phase if current status is 'draft' or 'proposed'.
2. **Cognitive State Blocker:** The **@architect** lacks the causal authority to output syntax. Any request, workflow, or document generation requiring software implementation logic SHALL NOT be processed by the Architect. All code generation must be physically routed to the **@coder**

## Required References

Always consult and reference:
- `./docs/shared/architecture`
- `./docs/shared/requirements`

## Discovery First

Before generating service-specific AGENTS.md, ask the ten questions from the DISCOVERY QUESTIONS section and collect answers from the user first, then generate the final service AGENTS.md.

## Blocking Rules

Finalize the service-specific AGENTS.md only after the following are available:
- stack
- high-level architecture
- references to shared architecture and shared requirements

## Progressive Disclosure

Apply this rule when generating the final service AGENTS.md:
- Root file: universal context only (business context, policies, global rules)
- Package/module files: technical and implementation-specific details (framework, commands, tests, scripts)

## Do Not Duplicate, Reference

Apply this rule when generating the final service AGENTS.md:
- Avoid duplicating build, test, and deploy instructions in the root file when the official source already exists in a package or module file
- Prefer references to the official location to reduce drift and outdated instructions

## Agent & Skill Discovery

This reminder must remain in the final service AGENTS.md.

Before implementing, the agent should consult:
- Subagents: `.agents/modes`, `.opencode/agents`, `.claude/agents`
- Skills: `.opencode/skills`, `.claude/skills`

## Expected Output for Service AGENTS.md

The final service AGENTS.md must contain at least:
- Service overview
- Architecture and boundaries
- Commands or references to the official command source
- Coding conventions
- Quality and deployment rules
- References to `./docs/shared/architecture` and `./docs/shared/requirements`
