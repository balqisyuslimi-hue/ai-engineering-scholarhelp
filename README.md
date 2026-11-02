# ScholarHelp

> An AI-powered scholarship Q&A assistant that helps Malaysian students find and understand public scholarship opportunities through cited, natural-language answers.

## Problem Statement
Students in Malaysia face severe information asymmetry and search fatigue when seeking financial aid for higher education. Eligibility criteria are scattered across government portals and university PDFs, making it difficult for students to know what they qualify for. Simple keyword search cannot answer complex, cross-document questions (e.g., matching a student's specific background to nuanced income and CGPA requirements), which is why an AI engineering solution using Retrieval-Augmented Generation (RAG) is necessary to synthesize accurate, cited answers.

## Evidence of the Problem
- **Evidence 1:** A qualitative study found that despite hundreds of qualified students in a Malaysian school, only five applied for scholarships because counselors lacked scholarship literacy and students lacked role models. *(Source: Stratsea, "Are Scholarships Out of Reach?" 2026)*
- **Evidence 2:** Surveys show that 3 in 4 undergraduates have given up on scholarships due to exhaustion, and 79% have not applied for a scholarship they were eligible for because the process didn't feel worth the effort. *(Source: Sallie, "The Scholarship Search Fatigue Report," 2026)*
 
## Initial Related Work / Existing Approaches
- **PUENYAI Bot** *(Ramli, Krathu, & Bramantoro, 2025 - ACIIS Conference)* + **Key limitation:** Designed for a single institution's internal sources; does not aggregate or address external, nationwide scholarship databases.
- **Knowledge-Grounded Conversational AI for Scholarship Discovery** *(Roumani & Liang, 2026 - ACR'26 Proceedings)* + **Key limitation:** While using a RAG architecture for scholarships, the implementation specifically targets universities in Kuwait and lacks grounding in Malaysian public documents.
- **EduAdvisor** *(EduAdvisor, 2026)* + **Key limitation:** A commercial, human-driven lead-generation platform tied to partner institutions. It functions as a sales funnel for specific universities rather than an independent, open-domain AI grounded in official government policies.
 
## Project Objectives
- **O1:** To develop a RAG-based AI assistant that accurately extracts and synthesizes scholarship eligibility, deadlines, and benefits from Malaysian public documents.
- **O2:** To evaluate the system's performance against a manually constructed QA dataset focusing on Answer Accuracy, Retrieval Recall, and Hallucination Rate.
- **O3:** To provide a transparent user interface that cites the source document for every answer, mitigating trust issues and fear of scams.

## Target Users
Malaysian pre-university students (SPM/STPM/Matriculation) and their parents who lack access to dedicated school counselors, as well as university students seeking external funding for their studies.

## Data Sources
- Source 1: JPA Official Sponsorship Portal (Program Ijazah Dalam Negara) — `https://penajaan.jpa.gov.my/`
- Source 2: MARA Scholarship Guidelines — `https://www.mara.gov.my/`
- Source 3: Yayasan Pahang Scholarship — `https://www.yayasanpahang.gov.my/`
- Source 4: UTM Scholarship and Financial Aid (UTM ASCEND) — `https://admission.utm.my/scholarship-and-financial-aid/`
- Source 5: Anugerah Biasiswa Merdeka PNB — `https://www.pnb.com.my/`

---

## Weekly Progress

### Week 1: System Map & Project Scope
- [x] Initial repository structure
- [x] Project scope and observation sheets
- [x] V1 System Map

### Week 2: Requirements & Architecture
- [x] Functional (FR), Non-Functional (NFR), and Responsible AI (RAI) requirements
- [x] Evaluation criteria defined
- [x] V1 Architecture Diagram and Decisions (ADR)

### Week 3: Data Pipeline (V1)
- [x] **Data Inventory:** [docs/week3_data_inventory.md](docs/week3_data_inventory.md)
- [x] **Pipeline Decisions & Stage Contracts:** [docs/week3_pipeline_decisions.md](docs/week3_pipeline_decisions.md)
- [x] **Pipeline Diagram:** [docs/week3_pipeline_diagram.png](docs/week3_pipeline_diagram.png)
- [x] **Executable Pipeline Notebook:** [notebooks/week3_pipeline.ipynb](notebooks/week3_pipeline.ipynb)
- [x] **Prepared Outputs:** [data/pipeline_v1/documents/prepared_text.jsonl](data/pipeline_v1/documents/prepared_text.jsonl)
- [x] **Lineage Manifest:** [data/week3_manifest.json](data/week3_manifest.json)

**Week 3 Reflection & Limitations:**
During the data preparation pipeline execution, we ingested 5 distinct scholarship documents (PDFs and TXT files) from JPA, MARA, Yayasan Pahang, UTM, and PNB. The comparison between fixed-sized and paragraph-aware chunking was done, and we selected paragraph-aware (chunk size of 500) since the criteria for scholarships have a very well-defined structure and use bullet points, hence fixed-sized chunking was ruining the context. One of the limitations is that our basic PDF parser cannot track exact page numbers, which means our RAG references will use the document name and not the specific page. In addition to that, scanned PDFs without text layers (OCR) will not pass through the ingestion phase.