# Week 3 Pipeline Decisions — ScholarHelp

## Engineering Decisions
- **Topic 2 Requirement ID(s):** O1 (RAG Assistant), FR3 (Source Citations), NFR4 (Maintainability).
- **Selected Sources:** 5 documents (JPA TXT, MARA PDF, Yayasan Pahang PDF, UTM PDF, PNB TXT).
- **Part B Comparison & Evidence:** Compared fixed-size chunking vs. paragraph-aware chunking. Paragraph-aware was chosen because scholarship eligibility lists and benefits are usually bulleted; fixed-size chunking cuts sentences in half, destroying context.
- **Chosen Preparation Configuration:** Paragraph-aware chunking (size: 500 characters).
- **Accepted Limitation:** The basic splitter does not preserve exact page numbers, so citations will refer to the document name rather than the specific page.
- **ETL/ELT Decision:** ETL (Extract text, transform into chunks, load to JSONL for the vector database).
- **Batch/Streaming Rationale:** Batch processing. Scholarships update annually, so live streaming data ingestion is unnecessary. 
- **Output Location:** `data/processed/prepared_text.jsonl` and `data/pipeline_v1/documents/`.
- **Provenance Caveat:** If the JPA website updates their policies, the PDFs and text files must be re-downloaded and the pipeline re-run.

## Stage Contracts & Failure Responses

| Stage | Contract / Evidence | Failure Response |
| :--- | :--- | :--- |
| **Ingest** | Chosen source files exist in the local directory and are readable. | Pipeline stops and throws a `FileNotFoundError`. |
| **Inspect** | Source files are readable and `PdfReader` successfully extracts text. | Pipeline skips empty files (e.g., scanned images) and logs a warning. |
| **Prepare** | Paragraph-aware chunking successfully creates text chunks. | Stop or report transformation failure. |
| **Validate** | Output `prepared_text.jsonl` exists, is non-empty, and SHA-256 fingerprints match. | Pipeline stops and raises a `ValueError` to prevent saving empty data. |
| **Record Lineage** | `week3_manifest.json` correctly links source documents to prepared chunks. | Stop/report missing mapping. |