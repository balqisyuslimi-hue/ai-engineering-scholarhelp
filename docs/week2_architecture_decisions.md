# Architecture Decisions & Traceability - ScholarHelp

## 1. Architecture Decision Records (ADR)

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
| :--- | :--- | :--- | :--- | :--- |
| **Include Knowledge Access (RAG)** | Answers must be grounded in approved Malaysian scholarship documents (NFR2, FR3). | Base model only; static search; dynamic knowledge access. | **Dynamic Knowledge-Access Component (RAG)** | Increased system complexity and latency, but ensures up-to-date grounding and traceability. |
| **Include Scope Control** | Out-of-scope queries must be refused to maintain trust and safety (RAI1). | Prompt instruction only; explicit scope-control component. | **Explicit Scope/Safety Control Node** | Additional processing step (classifier or prompt check) which may cause occasional false refusals, but prevents harmful hallucinations. |
| **Local Vector Database** | Inference cost must remain within student budget (NFR3) and data updates must be fast (NFR4). | Cloud-hosted enterprise DB; Local open-source vector DB. | **Local open-source vector database** | Less scalable for enterprise loads, but zero hosting costs and fast local re-indexing. |

## 2. Requirements Traceability Matrix

| Objective | Requirement | Evaluation Criterion | Architecture Element | Later Evidence |
| :--- | :--- | :--- | :--- | :--- |
| **O1** | FR1, FR2 | Answer Correctness | Knowledge Source (PDFs) → Retriever → LLM Service | Test results from 100 QA pairs showing correct criteria extraction. |
| **O3** | FR3, RAI2 | Source Citation and Support | Application Interface (Output Formatter) | 100% citation presence in test outputs; manual validation of source match. |
| **O2** | RAI1 | Out-of-Scope Refusal | Scope / Safety Control node before output | Test results showing 95%+ refusal rate for out-of-scope queries. |