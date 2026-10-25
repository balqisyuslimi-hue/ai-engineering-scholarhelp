# Requirements Specification - ScholarHelp
Version: 1.0

## Section 0 - Project Framing & Application Scope Checkpoint

| Framing element | Details |
| :--- | :--- |
| **Problem + evidence** | Malaysian students face information inequality and search fatigue when finding scholarships. High-value scholarships are oversubscribed, while lesser-known ones are missed. *(Evidence: Stratsea (2026) shows massive awareness gaps; Sallie (2026) reports 79% of students skip eligible scholarships due to fatigue).* |
| **Existing Approaches** | 1. **PUENYAI Bot:** RAG chatbot for internal university services. <br> 2. **Knowledge-Grounded Conversational AI:** Scholarship RAG bot for Kuwait universities. <br> 3. **EduAdvisor:** Commercial university/scholarship matching platform in Malaysia. |
| **Project / Engineering Gap** | Existing solutions are siloed to single institutions, geographically confined, or commercially biased toward partner universities. There is a lack of an independent, open-domain AI assistant grounded in official Malaysian public documents (JPA, KPT) that synthesizes rules and provides cited answers. |
| **Objective O1** | To develop a Retrieval-Augmented Generation (RAG) assistant that accurately extracts and compiles scholarship eligibility, deadlines, and benefits from Malaysian public documents. |
| **Objective O2** | To evaluate the system's performance against a manually constructed QA dataset (100-200 pairs) focusing on Answer Accuracy, Retrieval Recall, and Hallucination Rate. |
| **Objective O3** | To provide an interface that transparently cites the source of each piece of information, solving the trust issue in social media scholarship advice. |
| **Intended Users** | Primary: Malaysian pre-university students (SPM/STPM/Matriculation) and parents lacking counselor access. Secondary: University students seeking external funding. |
| **Supported Tasks** | Answering natural-language queries regarding scholarship eligibility, deadlines, required documents, and application links based *only* on ingested official documents. |
| **Information / Knowledge Domain** | Malaysian higher education financial aid, specifically government scholarships (JPA, KPT) and public university financial aid guides (UTM). |
| **Operating Context** | Web-based chat interface accessible via desktop and mobile; used independently by students/parents during their scholarship search. |
| **Important Constraints** | The system relies entirely on the quality and recency of provided PDFs/websites; it cannot access live, private application portals; computational budget is limited to free-tier/student API limits. |
| **Explicit Out-of-Scope Tasks** | The system must **not** submit applications, provide definitive financial or legal advice, guarantee scholarship award outcomes, or answer queries about private/foreign scholarships not in the database. |
| **Evaluation Focus** | How accurately and reliably does the RAG system retrieve and synthesize correct scholarship criteria without hallucinating, while providing verifiable citations. |

---

## Section 1: Functional Requirements (FR)

| # | Requirement — The system SHALL | Scope Boundary — SHALL NOT (where relevant) |
| :--- | :--- | :--- |
| **FR1** | Answer questions about scholarship eligibility (e.g., CGPA, income requirements) based on the ingested public documents. | Invent or assume eligibility criteria not explicitly stated in the source documents. |
| **FR2** | Provide the specific application deadline and URL for scholarships found in the documents. | Guarantee that the user will successfully receive the scholarship upon applying. |
| **FR3** | Provide a source citation (document name and page/section) for every generated answer. | Present unsupported information as if it came from an official source. |
| **FR4** | Decline to answer queries that fall outside the domain of Malaysian higher education scholarships. | Provide financial planning, immigration, or career advice. |
| **FR5** | Maintain conversational context to answer follow-up questions clearly (e.g., "What about the income cap for that one?"). | Remember personal user data (PII) across different sessions. |

---

## Section 2: Non-Functional Requirements (NFR)

| # | Quality Attribute | Requirement | Measurement Method | Metric | Threshold |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR1** | Performance | The system shall keep interactive responses within the agreed latency target. | Measure end-to-end latency on a defined test workload (50 queries). | p90 latency | < 5,000 ms |
| **NFR2** | Correctness | Answers shall be factually consistent with approved source documents. | Score a curated evaluation set (100 QA pairs) using a strict rubric. | Correct response rate (%) | ≥ 85% |
| **NFR3** | Cost | Inference cost shall remain within the student project budget. | Record model/API usage over the evaluation workload. | Cost per 100 queries | < RM 1.50 per 100 queries |
| **NFR4** | Maintainability | Approved source updates (e.g., new year PDFs) shall be incorporated without rebuilding the code. | Run a controlled document-update test (drop a new PDF into the folder). | Update/Indexing time | < 15 min |

---

## Section 3: Responsible AI Requirements (RAI)

| # | Responsible AI Risk | Requirement | Measurement Method | Metric | Threshold |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RAI1** | Hallucination (Safety) | The system shall refuse to answer or explicitly state "I don't know" when the retrieved context does not contain the answer. | Run a safety test set containing 30 out-of-scope or unanswerable queries. | Refusal success rate | ≥ 95% |
| **RAI2** | Transparency / Grounding | The system shall provide a verifiable source reference for all document-grounded answers. | Evaluate 50 document-grounded responses for citation presence and accuracy. | Citation presence rate; citation-source match rate | 100% presence; ≥ 95% match |
| **RAI3** | Fairness / Bias | The system shall not disproportionately favor popular corporate scholarships over lesser-known state/foundation scholarships when answering general queries. | Analyze retrieval distribution across 20 broad queries (e.g., "scholarships for engineering"). | Representation of non-corporate scholarships in top-3 results | ≥ 40% |