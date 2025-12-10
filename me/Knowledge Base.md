# **Career Conversations Agent Knowledge Base: Reid Caulder**

# **Section 1: Candidate Profile & Philosophy**

**Education & Motivation:**

* **Background:** Junior at Clemson University, pursuing a double major in Financial Management and Accounting. This dual-discipline approach provides a holistic view of corporate health, blending forward-looking financial strategy with the grounded reality of accounting standards.  
* **Career Path:** Originally, the academic trajectory was aimed at law school, with finance initially viewed as a practical contingency plan. However, around 2022, a latent interest in investing blossomed into a genuine passion. This pivot was not merely a change in major but a fundamental shift in life purpose, realizing that analyzing markets and businesses was far more intellectually stimulating than the legal profession.  
* **Accounting Philosophy:** Firmly subscribes to the belief that accounting is the "language of business." To be a successful investor, one cannot simply rely on surface-level metrics; one must fundamentally understand accounting to the point where it is second nature. It must be "ingrained," allowing for the intuitive reading of financial statements (10-Ks, 10-Qs) to reveal the true narrative of a company's performance, beyond what management highlights in earnings calls.  
* **Multidisciplinary Approach:** Adopts the "Charlie Munger principle" of mental models, aspiring to be a polymath. This philosophy posits that problems are best solved not by looking through a single lens, but by applying concepts from various disciplines (e.g., psychology, history, economics). While currently focused heavily on the intersection of Finance and Artificial Intelligence, the long-term goal is to continuously broaden this "lattice of mental models" to identify investment opportunities others might miss.

**Investment Philosophy & "Circle of Competence":**

* **Definition:** Strictly adheres to Warren Buffett’s concept of the "Circle of Competence." This discipline involves rigorously defining what one knows and, more importantly, what one does *not* know. Success in investing comes not from having an opinion on every stock, but from having a high-conviction, accurate view on the few businesses that fall within one's specific area of expertise.  
* **Application:** Research is channeled exclusively into sectors and business models where the unit economics, competitive advantages, and risks are transparent and fully understood. This disciplined focus prevents unforced errors driven by "FOMO" (fear of missing out) in hyped but opaque sectors.

**Technical Skills:**

* **Excel:** Possesses expert-level proficiency, characterized by a "mouse-free" workflow. By relying almost exclusively on keyboard shortcuts, financial modeling and auditing tasks are executed with high speed and precision. This skill was honed during internships to navigate and audit massive datasets efficiently, proving that speed in Excel translates directly to higher productivity and deeper analysis.  
* **Visualization Tools:** Acquired formal training in Power BI and Tableau during the Fall 2025 semester. While current application has been academic, there is a clear vision for their real-world value—specifically in translating complex financial datasets into intuitive dashboards for stakeholders. Plans are in place to deploy these tools in future internships to modernize reporting workflows.  
* **Python:** Distinctive skill set for a finance major. Python is utilized not just for data analysis, but for *automation*—such as writing scripts to parse large Excel files —and, crucially, for the architecture of autonomous AI agents. This coding ability bridges the gap between traditional finance and modern fintech. Experience in Python data analytics and visualization tools such as matplotlib, pandas, numpy.

# **Section 2: Project Deep Dive \- Equity Research Multi-Agent System \[Project\]**

## **Project Overview**

This project is an institutional-grade, multi-agent system designed to automate the labor-intensive process of equity research. Unlike standard LLM summarization tools, this system employs an **adversarial architecture**—distinct teams of agents with opposing biases ("Bull" and "Bear") conduct parallel, segregated research to avoid confirmation bias. The system is designed to transform raw financial data into a rigorous, debate.

## **Core Philosophy**

The system is built upon two foundational principles:

* **Adversarial Fact-Finding:** Recognizing that shared research leads to shared bias, the workflow splits into two independent organizations. The Bull Team is incentivized to find growth catalysts and competitive moats, while the Bear Team is incentivized to uncover accounting irregularities and execution risks. These teams do not communicate until the final debate phase.  
* **(Planned, not current) The "White-Box" Standard:** To prevent hallucinated valuations, agents are not allowed to simply guess numbers. They must utilize a secure code sandbox to write executable Python code for financial modeling (e.g., DCF, WACC), ensuring all math is verifiable and transparent.

## **System Architecture**

The system utilizes **LangGraph** to manage a complex, cyclic workflow that mirrors the organizational structure of a top-tier investment firm.

### **1\. The Orchestrator (Chief of Staff)**

The entry point is the Chief of Staff agent. It parses natural language user requests to extract structured metadata (Ticker, Sector, Industry) and determines the user's risk tolerance. Uniquely, this agent queries a long-term memory database (Supabase) to retrieve context from previous analysis sessions before briefing the research teams.

### **2\. Parallel Research Tracks (The Divergence)**

Using a "Map-Reduce" style topology, the Chief of Staff dispatches work to two segregated subgraphs via an asynchronous API:

* **The Bull Team:** Led by a "Growth-Focused" Lead Analyst who delegates tasks to finding expansion opportunities.  
* **The Bear Team:** Led by a "Forensic" Lead Analyst who delegates tasks to finding distress signals.

Each team possesses its own dedicated sub-agents:

* **Web Researcher Agent:** Uses the Serper API to scour news, analyst ratings, and macro trends.  
* **SEC Agent:** Interfaces with the SEC EDGAR API to pull 10-K and 10-Q filings, extracting raw financial tables for analysis.

### **3\. The Debate & Verdict (The Convergence)**

Once both teams generate their theses, the system converges at the Judge Agent.

* **Persona:** The Judge is modeled after Warren Buffett and eventually plans to utilize a RAG (Retrieval-Augmented Generation) knowledge base containing decades of shareholder letters to ensure decisions align with value investing principles.  
* **Scoring:** The Judge evaluates the conflicting narratives using a structured scoring schema (0-100), rendering a final verdict, a "Strong Buy" to "Strong Sell" recommendation, and a list of key deciding factors. It uses the most relevant and valuable information from each team’s report to craft a final comprehensive report to give to the user.

## **Technical Stack**

* **Orchestration:** LangGraph (Stateful, cyclic multi-agent flows).  
* **Reasoning Engine:** Gemini 2.5 Pro (chosen for its massive context window to process full annual reports).  
* **(Planned, not current)  Code Execution:** E2B (Secure cloud sandboxing) allows agents to run Python code for quantitative analysis.  
* **Memory:** Supabase (Long-term persistence) and SQLite (Session checkpoints).  
* **(Planned, not current) Frontend:** Gradio interface featuring a "Process Trace" that visualizes the internal debate in real-time.

## **Prompt Engineering Strategy**

* **Role-Based Prompting:** Strictly enforces distinct personalities. The Bear team must remain cynical and risk-averse, while the Bull team must remain optimistic, or the adversarial model fails.  
* **Structured Outputs:** The system relies heavily on Pydantic models to force agents to return data in specific JSON schemas, ensuring that the "Judge" agent receives comparable evidence from both sides.  
* **Chain of Thought (CoT):** Implemented to force agents to "show their work." Instead of jumping to a conclusion, agents must step through the logic (e.g., analyzing revenue growth relative to margin compression) before arriving at a thesis.

## **Additional Planned Features**

* Agents to access: quarterly earnings call transcripts, institutional buyers and politician buyers.  
* Specific analyst agent types for each of the 11 stock market sectors.  
* Expansion beyond equities, venturing into fixed income, futures, and options.  
* The ability to execute trades on its own, first in a paper trading environment.

# **Section 3: Project Deep Dive \- Career Conversations Agent (The "Digital Twin") \[Project\]**

**Project Overview:** This project is the currently active "Digital Twin" agent hosting this very conversation. It serves as a live demonstration of "Agentic AI" applied to personal branding. Rather than a static resume, this agent provides an interactive, 24/7 interface for recruiters and potential collaborators to query my background, technical skills, and design philosophy.

**Architecture & Tech Stack:**

* **Core Logic:** Python-based application using the OpenAI Agents SDK framework. Gemini-2.5-pro for natural language processing and reasoning.  
* **Context Injection:** Unlike standard chatbots, this agent utilizes a dynamic context window that ingests my full LinkedIn profile (parsed via pypdf) and this structured Knowledge Base. This ensures the agent is "grounded" in my actual data and reduces hallucinations.  
* **Frontend:** Built with Gradio, allowing for rapid prototyping and easy deployment to hosting environments like Hugging Face Spaces.  
* **Tool Use (Function Calling):** The agent is equipped with custom Python functions that it can "decide" to call based on the conversation context:  
  * record\_user\_details: If a user expresses interest in collaborating, the agent captures their information and triggers a webhook.  
  * record\_unknown\_question: A feedback loop mechanism. If the agent encounters a question it cannot answer, it logs the query, alerting me with the **Pushover API** to send push notifications to my mobile device immediately when a recruiter engages with the agent or leaves contact information. Also recording questions that cannot be answered into a csv file to be added to the agent for future users.

# **Section 4: Professional Experience Deep Dive \- Audit & Assurance**

**Role:** Financial Statement Audit Intern – Burch Oxner Seale Co. (Summer 2025\)

**Operational Philosophy: "Trust but Verify"** This role transitioned the candidate from academic theory to the practical realities of forensic accounting. The core takeaway was that an auditor's job is not to accept a client's narrative at face value, but to rigorously trace the "audit trail" to its source.

## **Key Case Study 1: Client Funds & Compliance (SC Dept. of Disabilities)**

* **The Challenge:** During an audit of a County Disabilities and Special Needs Board, the candidate was responsible for testing "client funds"—money managed on behalf of individuals with disabilities who cannot manage their own finances. This is a high-risk area requiring strict stewardship.  
* **The Discovery:** While reviewing the purchase logs and receipts for a sample of clients, the candidate identified that a specific month's bank statement was completely missing from the records.  
* **The Action:** Rather than overlooking the gap or relying on a verbal assurance, the candidate flagged the issue. In the closing meeting with the Executive Director and Finance Director, the candidate directly addressed the discrepancy, explaining that the audit sample was incomplete without that specific statement.  
* **The Result:** The client provided the necessary documentation. This experience solidified the importance of being thorough, even when it requires having uncomfortable conversations with senior leadership to ensure compliance.

## **Key Case Study 2: Revenue Recognition & Independence (Care House of the Pee Dee)**

* **The Challenge:** The candidate was tasked with auditing revenue for a child advocacy center which functions as a subsidiary of a larger medical entity (Hope Health).  
* **The Evidence Gap:** The initial evidence provided for a significant revenue transaction was a simple email correspondence between the two entities.  
* **The Decision:** Applying professional skepticism, the candidate determined that an internal email was insufficient audit evidence under GAAP standards.  
* **The Resolution:** The candidate independently initiated a request for the paying organization's official bank statements and formal documentation to conclusively prove the transfer of funds. This ensured the revenue was recognized based on hard data, not just internal communication.

## **Technical Workflow: Invoice & Expenditure Testing**

* **Methodology:** Executed testing on samples of 30-40 invoices per audit cycle.  
* **The "Three-Way Match":** Rigorously verified that every transaction adhered to a strict validation chain:  
  1. **Physical Invoice:** Confirmed the original vendor bill.  
  2. **Canceled Check/EFT:** Verified the exact amount was deducted.  
  3. **Bank Statement:** Confirmed the funds cleared the correct account.  
* **Specialized Funds:** Gained experience auditing restricted federal funds (HUD), ensuring they were segregated in separate bank accounts and used strictly for authorized housing purposes.

## **Taxation Research Strategy (Summer 2024\)**

* **Philosophy:** Instilled with a "Read the Manual" discipline. Leadership emphasized that asking for the answer teaches nothing; finding the source teaches everything.  
* **Application:** Utilized **CCH AnswerConnect** and direct IRS form instructions to navigate complex issues like fixed asset depreciation (e.g., company vehicles) and multi-state operations. This built a habit of finding defensible, cited answers rather than relying on intuition.

