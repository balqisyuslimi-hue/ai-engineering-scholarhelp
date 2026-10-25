# Evaluation Criteria - ScholarHelp

| Objective / Requirement ID | Evaluation Criterion | Capability Bucket | Measurement Method | Metric | Threshold | User / Business Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **O2 / NFR2** | Answer Correctness | Domain-specific capability | Evaluate a defined set of 100 supported scholarship queries using a manual grading rubric. | Correct response rate | ≥ 85% | Users receive reliable, accurate answers rather than misleading information. |
| **O3 / FR3 / RAI2** | Source Citation and Support | Instruction-following capability | Inspect 50 document-grounded responses for citation presence and verify if the cited source actually supports the answer. | Citation presence rate; citation-source match rate | 100% presence; ≥ 95% match | Users can verify information against official portals, reducing fear of scams. |
| **O1 / FR4 / RAI1** | Out-of-Scope Refusal | Instruction-following capability | Test the system with a defined safety/scope query set (30 out-of-scope questions like "how to apply for a credit card"). | Refusal success rate | ≥ 95% | Reduces inappropriate advice outside the intended domain. |
| **O1 / FR1** | Retrieval Completeness | Domain-specific capability | Measure if the system retrieves the correct document chunk before generating the answer. | Retrieval Recall (top-5) | ≥ 90% | Ensures the AI has the necessary facts to answer the student's question. |
| **NFR1** | Response Latency | Cost and latency | Measure end-to-end response time across the 100-question evaluation workload. | p90 latency | < 5 s | Users receive a responsive interaction, preventing drop-off due to waiting. |

---

### Reflection
**Which evaluation criterion is most important for determining whether your AI application will be useful to its intended users? Why?**

**Answer Correctness and Source Citation** is the most critical criterion. Because the target users are anxious students and parents seeking financial aid, a single hallucinated CGPA requirement or missed deadline could cause them to waste months or lose an opportunity entirely. Furthermore, because 53% of students already fear scams (as noted in Week 1 evidence), the system must not only be correct but must also provide verifiable citations. If the system is fast but wrong, or correct but untrustworthy, it fails its core purpose.