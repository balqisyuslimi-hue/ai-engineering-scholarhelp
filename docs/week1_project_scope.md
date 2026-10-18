Project Name	ScholarHelp
Domain	Higher Education
Problem Statement	Students in Malaysia suffer from serious information inequality and search fatigue while trying to find scholarship opportunities. The high-value scholarships have a huge number of applicants, while other deserving students do not even know about less-known but equally valuable scholarship opportunities.
Evidence of the Problem	Evidence 1: For Malaysian students, the biggest challenge in getting a scholarship is neither the lack of talent nor meritocracy but awareness. A study showed that in a Sabah school, there were hundreds of students who had the eligibility to get a scholarship, but only five applied.

Source / citation: Stratsea, "Are Scholarships Out of Reach?" (2026)

Evidence 2: There is a lot of "scholarship fatigue" experienced by students. Surveys indicate that 3 out of 4 undergraduate students have abandoned scholarships because of fatigue, and 79% did not apply for a scholarship for which they were eligible because of lack of motivation. Furthermore, 53% mentioned the fear of being scammed as a reason.

Source / citation: Sallie, "The Scholarship Search Fatigue Report" (2026).
Initial Related Work (at least 3)	Study / solution 1: PUENYAI Bot. A locally hosted RAG chatbot for university services including scholarships.

Source / citation: Ramli, A. A. R. B., Krathu, W., & Bramantoro, A. (2025). PUENYAI Bot: A Retrieval-Augmented LLM Chatbot for University Information Services. 2025 7th International Conference on Applied Computational Intelligence in Information Systems (ACIIS), 1-6.

Key limitation: Concentrates on internal sources of one organization only and does not consolidate external or national scholarships.

Study / solution 2: Knowledge-Grounded Conversational AI for Scholarship Discovery. An AI chatbot using NLP and RAG to answer scholarship queries.

Source / citation: Roumani, A. M., & Liang, D. (2026). Knowledge-Grounded Conversational AI for Scholarship Discovery. In K. Daimi & A. Alsadoon (Eds.), Proceedings of the Fourth International Conference on Advances in Computing Research, ACR’26 (pp. 93-107). Springer. 

Key limitation: Implemented for universities in Kuwait and not adapted for the Malaysian scholarship landscape or local public documents.

Study / solution 3: EduAdvisor (Malaysia). A commercial platform that matches students to universities and scholarships based on results.

Source / citation: EduAdvisor. (2026). About Us. Retrieved from https://eduadvisor.my/about-us

Key limitation: It is an AI lead generation system which is connected to the partner institutions. It is not an independent AI assistant which responds to policy questions and helps understand eligibility criteria.
Engineering Gap / Limitation	What practical or technical limitation remains unresolved?
Gap / Limitation: The current solutions are either institutionally siloed which is one bot per university, geographically confined such as in Kuwait, or commercially inclined towards the partner universities. There exists a gap for an independent, open-domain AI assistant which is based upon the Malaysian public research documents such as JPA, MARA and state institutions that can synthesize eligibility rules and provide cited answers to reduce student search fatigue.
Initial Project Objectives (2–3)	O1: To develop a Retrieval-Augmented Generation (RAG) assistant that is able to extract and compile scholarship eligibility, deadlines, and benefits in the case of Malaysian public documents such as JPA and financial aid books of universities.

O2: To evaluate the system's performance against a manually constructed QA dataset (100-200 pairs) focusing on Answer Accuracy, Retrieval Recall, and Hallucination Rate (refusal on unknown queries).

O3 (if applicable): To provide an interface that is open in mentioning the source of each piece of information, thereby solving the problem of trust in social media scholar advice.
Target Users	Primary: Malaysian pre-university students such as SPM, STPM or Matriculation and their parents who lack access to school counselors.
Secondary: University students seeking external funding for their undergraduate or postgraduate studies.
Data Sources (at least 2)	Source 1: JPA Official Sponsorship Portal (Portal Penajaan JPA) 
— URL: https://penajaan.jpa.gov.my/

Source 2: Ministry of Higher Education (KPT) Scholarship Portal
— URL: https://biasiswa.mohe.gov.my/

Source 3 (if any): UTM Scholarship and Financial Aid (Admission Portal)
— URL: https://admission.utm.my/scholarship-and-financial-aid/

Similar to EduAdvisor	It solves the same problem of assisting students to find financial aid suitable for their profile without going through the tedious process of visiting several different sites manually.
Different from EduAdvisor	EduAdvisor is a business-oriented counseling system which makes money by placing students into universities. ScholarHelp is an AI-powered Q&A bot which is not limited to any particular institution. It does not encourage students to enroll into certain partner universities, but provides them with exact answers to their natural-language questions such as "What is the income cap for JPA PIDN?".
Responsible AI Risks (at least 2) 	Risk 1: Hallucination of Deadlines or Criteria. LLM can hallucinate wrong deadlines or criteria if not anchored correctly. 

Risk 2: Outdated Information. Scholarship Policies are updated each year. 

Risk 3 (if any): Bias towards popular scholarships. The algorithm could prefer famous scholarships such as PETRONAS or Maybank since they tend to be mentioned more often.

