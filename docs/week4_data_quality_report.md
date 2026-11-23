# Week 4 Data Quality & Bias Report - ScholarHelp

**Version:** 1.0 
**Audit stage:** Topic 3 prepared data (Pathway A - PDF/TXT extraction) 
**Decision:** GO WITH CONDITIONS

---

## 1. Project and Data Overview

**Project:** ScholarHelp, a Retrieval-Augmented Generation (RAG) assistant that answers Malaysian scholarship questions (eligibility, deadlines, application links, required documents) from official public documents.

**Intended users:** Malaysian pre-university students (SPM/STPM/Matriculation); secondary users are university students seeking external funding.

**Requirements audited (from week2_requirements.md):**

| ID | Requirement | Data needed to support it |
| :--- | :--- | :--- |
| **FR1** | Answer questions about scholarship eligibility (e.g., CGPA, income) based on ingested public documents. | Extracted eligibility fields: nationality, age, CGPA/SPM grades, income thresholds, readable and correct in the prepared chunks. |
| **FR3 / RAI2** | Provide a verifiable source citation (document name and page/section) for every answer. | Each chunk must retain a non-empty source reference and a verifiable provenance hash. |

**Data audited:** Topic 3 Part B prepared text chunks, one JSON record per chunk, `processing = paragraph-aware-char-500`.

**Output and manifest:** `data/processed/prepared_text.jsonl` with matching manifest `data/week3_manifest.json`.

**Sources (5, all public):** Anugerah Biasiswa Merdeka PNB (.txt), Biasiswa MARA 2026 (.pdf), Biasiswa Yayasan Pahang 2026 (.pdf), INFORMASI-TENTANG-BIASISWA-UTM-ASCEND (.pdf), Program Ijazah Dalam Negara / JPA PIDN (.txt). Each record carries a `source_sha256` hash.

**Sample:** Population = 68 records across the 5 sources. Sample ≈ 20 chunks, selected across all five sources and including known-problem cases (mid-sentence splits and records with broken characters). Limitation: convenience sample, not a basis for whole-corpus statistics.

---

## 2. Five-Dimension Quality Scorecard

| Dimension | Finding | Evidence | Impact on FR1 / FR3 | Decision |
| :--- | :--- | :--- | :--- | :--- |
| **Completeness** | Eligibility text is split mid-sentence across chunks. | PNB-0002 ends "subsistence allowa"; PNB-0003 starts "nces…". MARA-0007 ends "ditetap"; MARA-0008 starts "pkan". | A retrieved chunk may contain half a requirement → incomplete eligibility answer (FR1). | Warning |
| **Consistency** | Languages and formats are mixed; page provenance lost. | PNB repeats English then Malay; others are Malay-only. Date formats differ ("29 April–8 May 2026" vs "Mac hingga Mei"). All PDF records have `"page": null`. | Harder to compare sources and cite a page/section (FR3). | Warning / Review |
| **Accuracy** | Broken characters (`\u0000`) replace punctuation and numbers in many records. | MARA-0010 income "RM\u0000\u0000\u0000\u0000\u0000\u0000"; MARA-0008 age "\u0000\u0000\u0000\u0000 tahun"; Yayasan-0006 CGPA "\u0000\u0000\u0000". True values must be checked against source PDFs. | Corrupted numeric eligibility → wrong answers/matching (FR1). | Review (partly N.V.) |
| **Timeliness** | Data covers the 2026 intake cycle. | PNB window 29 April–8 May 2026; MARA updated 9 Feb 2026; Yayasan 25 Jan 2026. | Deadlines go stale after intake (FR1/FR2). | Warning |
| **Uniqueness** | PNB content appears twice (English and Malay). | PNB-0001–0004 (EN) vs PNB-0005–0007 (BM). | Redundant retrieval of the same scheme. | Warning |

Observed facts are separated from inferred risk: the counts above are observations from the inspected records; the impacts are plausible consequences, not measured model failures.

---

## 3. Validation Findings

| Rule | Condition | Scope tested | Observed result | Action |
| :--- | :--- | :--- | :--- | :--- |
| **V1** (linked to FR3 / RAI2) | Every record must have a non-empty `source` and a 64-character `source_sha256`. | 68 records | **68 pass / 0 fail / 0 N.V.** | PASS: Provenance and citation basis are sound. |
| **V2** (linked to FR1 + Topic 3 transformation risk) | A record containing eligibility keywords (CGPA/PNGK/RM/tahun) must not contain the `\u0000` character. | 68 records | **Failed on 39 records out of 68** (broken numbers observed in MARA and Yayasan records). | REVIEW: Verify broken numbers against source PDFs; flag before use. Do not auto-delete (values may be recoverable). |

---

## 4. Duplicate, Anomaly and Coverage Findings

**Duplicates:** PNB content is duplicated as English (records 0001–0004) and Malay (records 0005–0007), semantic near-duplicate, not byte-identical. No repeated `record_id` was observed.

**Anomalies:** Broken `\u0000` characters corrupt punctuation and numeric values in multiple records; mid-sentence chunk splits occur where the 500-character splitter cut a paragraph.

**Coverage of two relevant categories:**

| Category | Expected evidence | Observed evidence / gap | Possible downstream effect |
| :--- | :--- | :--- | :--- |
| **Undergraduate / SPM–STPM entrants** | Eligibility fields: nationality, age, CGPA/SPM grades, income, deadline | Well covered (PNB, MARA, Yayasan, JPA PIDN), but income/CGPA values are corrupted in several records; JPA PIDN has no explicit deadline date in its chunks. | Income/CGPA-based answers unreliable for this large user group. |
| **Postgraduate / PhD** | PhD eligibility, age, CGPA, funding terms | Only one postgraduate scheme (UTM ASCEND); ages corrupted in some chunks. | Postgraduate users are under-served; single-source coverage. |

**Limits of evidence:** These are observations from an approximately 20-item sample, not the full corpus.

---

## 5. Bias Assessment

**Plausible bias source, pipeline-induced.** The `paragraph-aware-char-500` splitter combined with PDF text extraction caused mid-sentence splits and `\u0000` corruption of numbers.

**Chain:**
*   **Decision:** fixed 500-character paragraph splitting plus basic PDF text extraction.
*   **Gap:** numeric eligibility values (income thresholds, CGPA) corrupted; eligibility conditions fragmented across chunks.
*   **Potential effect:** the assistant may under-match or over-match income- or CGPA-constrained students, disproportionately affecting lower-income (B40/M40) applicants these schemes target and may give incomplete eligibility answers.
*   **Control:** add a table/PDF-aware extraction step and a numeric validator (V2) that flags corrupted values for manual verification before retrieval.

This is a plausible data-driven risk, not a proven fairness result. No claim of model-level fairness is made here.

---

## 6. Privacy, Rights and Governance

| Question | Record |
| :--- | :--- |
| **Provenance/version** | 5 public sources; each record carries `source` and a 64-char `source_sha256`; PDFs carry update dates (MARA 9 Feb 2026, Yayasan 25 Jan 2026). Matching manifest: `data/week3_manifest.json`. |
| **Rights/permissions** | Sources are publicly published scholarship pages; intended use is answering student queries. Formal licence terms not individually checked or marked **N.V.**. |
| **Privacy/sensitive data** | No personal data collected; only public scheme information. |
| **Consent/collection basis** | Not applicable. Public official/informational documents. |
| **Ongoing maintenance** | Re-scrape each intake cycle (annual). Trigger for revalidation: new year intake, changed deadline, or source update date. |

**Safeguard (at least one):** Do not commit raw PDFs or full extracted text to the public repository; commit only this report and redacted evidence excerpts.

---

## 7. Mitigation and Impact on Requirements

**Priority improvements:**
1.  **Repair or flag the corrupted numbers.** Owner: project author. When: before Topic 5. Run the V2 count, verify each corrupted value against the source PDF, and either fix the extraction or flag the record.
2.  **Improve text extraction.** Owner: project author. When: before Topic 5. Use a table/PDF-aware extractor to stop mid-sentence splits and preserve page numbers (supports FR3 page/section citation).

**Requirements affected:** FR1 (eligibility answers depend on correct numbers) and FR3/RAI2 (citations depend on preserved source and page references).

**Residual risks:** deadlines go stale after the 2026 intake; English/Malay duplication of PNB; single-source postgraduate coverage.

---

## 8. Quality-Gate Decision

**Decision: GO WITH CONDITIONS** for the audited ScholarHelp prepared-text corpus.

**Justification (two evidence points):**
1.  **V1 = 68/68 pass**. Every record has a source and provenance hash, so the citation/grounding requirement (FR3/RAI2) has a sound data basis.
2.  **V2 failed on 39 records** and mid-sentence splits are observed. Numeric eligibility values are not yet trustworthy for FR1.

**Conditions:**
*   Corrupted numeric values must be repaired or explicitly flagged before the data is relied on for eligibility answers.
*   Extraction must be improved to prevent mid-sentence splits and preserve page references.

**Re-review trigger:** Re-review after the V2 repair, requiring the corrupted-numeric rate to fall to the stated threshold (target 0% unflagged) or at the next intake cycle, whichever comes first.