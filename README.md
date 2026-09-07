# Arindam Choudhury

**Agentic AI & Copilot Studio Architect @ Capgemini** · Production agents for regulated Financial Services

[![LinkedIn](https://img.shields.io/badge/LinkedIn-arindam--choudhury-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arindam-choudhury)
[![Newsletter](https://img.shields.io/badge/Newsletter-Grounded%3A%20AI%20%26%20Architecture-5B2C87?style=flat-square)](https://www.linkedin.com/newsletters/grounded-ai-architecture-7448180546180042752/)

Seventeen years in enterprise delivery, the last several spent getting AI agents past the pilot stage on the Microsoft stack. My working bias, in short: orchestration over prompting, evaluation in the pipeline rather than after it, and human-in-the-loop placed where the risk actually sits instead of wherever the UI had room for a button.

Most of what I build is client work and stays with the client. What I can publish goes to the Microsoft guidance repos and to the newsletter, both below.

---

## What I work on

| Area | In practice |
|---|---|
| **Agentic AI** | Multi-agent orchestration, tool and connector design, failure and recovery paths, idempotency under retry |
| **Copilot Studio & Microsoft Foundry** | Where the boundary between them falls, and when an engagement genuinely needs both |
| **Power Platform & Dataverse** | Solution architecture, ALM, schema design at migration scale |
| **Legacy modernisation** | Lotus Notes to Dataverse: AI-assisted schema and flow generation at migration scale |
| **Responsible AI** | Evaluation harnesses, guardrails, and the governance regulated clients are actually asked to evidence |
| **MCP** | Server design, spec churn, and what it means for enterprise integration |

---

## Reference architectures

Submitted to [microsoft/PowerPnPGuidanceHub](https://github.com/microsoft/PowerPnPGuidanceHub):

**[Audit, eDiscovery and Regulator-Ready Evidence for Copilot Studio Agents (Purview-first)](https://github.com/microsoft/PowerPnPGuidanceHub/issues/26)**
A Purview-first evidence pattern for financial services, where auditability is a primary requirement rather than an afterthought. Separates agent execution from compliance operations: audit events from Copilot Studio, Power Automate and Dataverse flow into Microsoft Purview Audit, with optional SIEM/SOC integration, while Purview eDiscovery handles investigations, holds and regulatory production. Covers policy enforcement, approval workflows, least-privilege access, environment governance and evidence retention, aligned to the Power Platform Well-Architected Framework.

**[Agent Operations Center for Copilot Studio and Power Platform](https://github.com/microsoft/PowerPnPGuidanceHub/issues/114)**
An operations-first pattern for production agents that take real business actions — the part that gets skipped between a working demo and something a support team can run. Separates agent runtime from operational support: Copilot Studio for orchestration, Power Automate for execution, Dataverse for state, a model-driven app as the operations surface, Application Insights and Log Analytics for observability, Power BI for reporting, Teams for human escalation. Covers monitoring, recovery, retry handling, escalation and SLA tracking.

---

## Writing

**[Grounded: AI & Architecture](https://www.linkedin.com/newsletters/grounded-ai-architecture-7448180546180042752/)** — *Real delivery. Real trade-offs.*

A LinkedIn newsletter on enterprise AI architecture. No vendor keynote summaries; each issue takes one decision I have had to make on a real engagement and shows the trade-off, including where I got it wrong.

Seven issues so far, newest first:

- **07 · [Copilot Studio Changed. Still Need Foundry?](https://www.linkedin.com/pulse/copilot-studio-changed-still-need-foundry-arindam-choudhury-3y0je)** — whether the Copilot Studio/Foundry boundary still holds now the GitHub Copilot harness has gone GA. Three architecture choices, five questions for your next review.
- **06 · [The MCP Spec Changes on 28 July](https://www.linkedin.com/pulse/mcp-spec-changes-28-july-arindam-choudhury-cin6e)** — the largest revision since launch, and what it breaks for anyone already in production. A 15-minute architecture review to run before approving an MCP server.
- **05 · [The Day the Agent Asked the Wrong Question](https://www.linkedin.com/pulse/day-agent-asked-wrong-question-arindam-choudhury-bn1le)** — why reliable enterprise AI depends on context engineering rather than better prompts. The problem was not the answer; it was the context behind the question.
- **04 · [Human-in-the-Loop Is Not a Button. It's a Design Decision](https://www.linkedin.com/pulse/human-in-the-loop-button-its-design-decision-arindam-choudhury-m7tze)** — an approval step by default versus oversight by design: decision boundaries per action type, defined exception paths, escalation as a first-class pattern.
- **03 · [Capable by Design. Provable by Design.](https://www.linkedin.com/pulse/capable-design-provable-question-changed-architecture-choudhury-rfihe)** — the question that changed the architecture. Copilot Studio got us started; Foundry made it provable — step-level trace, evaluation pipelines, per-domain risk tiering.
- **02 · [Copilot Needed Orchestration, Not Just Prompts](https://www.linkedin.com/pulse/copilot-needed-orchestration-just-prompts-when-alone-choudhury-8zbye)** — when prompting alone failed and the architecture had to evolve: multi-step agent flows, tool-use optimisation, real validation and audit.
- **01 · [From Canvas Apps to Code Apps](https://www.linkedin.com/pulse/from-canvas-apps-code-eight-seconds-changed-my-arindam-choudhury-r6lte)** — the eight seconds that changed my architecture decisions. Delegation limits, business logic trapped in the UI layer, and what replaced them.

---

## What's here

Practical guidance for teams putting Copilot Studio and Power Platform agents into production — checklists, decision criteria and configuration patterns, with client detail stripped out.

In progress, in this order:

1. **Pre-production review gate for Copilot agents** — the checks to clear before an agent goes live: decision boundaries per action type, defined exception paths, recovery and idempotency under retry, evidence and retention. The criteria behind each check, and what actually satisfies it.
2. **MCP server review checklist** — what to establish before approving a third-party MCP server in an enterprise: capability surface, permission scope, data exposure, auth hardening, lifecycle and spec-version compatibility.
3. **AI Act Article 50 transparency pack** — mapping the EU AI Act's disclosure and AI-content-labelling duties onto concrete Copilot Studio and Power Platform configuration.
4. **Lotus Notes DXL extractor** — parses Domino XML exports of NSF databases into structured, inspectable output: forms, views, fields, computed formulas and document data. The extraction layer only, so a migration team can see what is actually in a database before deciding what to do with it.

---

## Credentials

**Expert** — Agentic AI Business Solutions Architect · Azure Solutions Architect · Power Platform Solutions Architect

**Associate** — Azure AI Engineer · AI Agent Builder · Power Platform Developer · Power Automate RPA Developer · Fabric Analytics Engineer · Power BI Data Analyst · Teams Application Developer

**Specialty** — Azure IoT Developer

**Other** — Frontier Transformation Engineer - TITAN (Microsoft) · AI Transformation Leader (Microsoft) · Claude Certified Developer, Certified Associate and Code Partner (Anthropic) · GitHub Copilot Core Skills · Four Copilot Dev Camp badges including MCP Integrator

---

Reach me on [LinkedIn](https://www.linkedin.com/in/arindam-choudhury) — happy to talk through anything above.
