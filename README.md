# 🎓 AI Maturity Assessment Tool
### *A self-assessment platform for UK Higher and Further Education institutions*

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat&logo=openai&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24-3F4F75?style=flat&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

> **Built as a portfolio project demonstrating applied AI skills for the Jisc AI Specialist role and similar positions in UK higher education.**  
> Grounded in the Alan Turing Institute AI Maturity Model, UNESCO's AI Competency Framework for Teachers, and Jisc's Digital Capability Framework.

---

## Table of Contents

- [What It Does](#what-it-does)
- [Live Demo](#live-demo)
- [The Five Dimensions](#the-five-dimensions-and-their-theoretical-grounding)
- [Quick Start](#quick-start)
- [How Report Generation Works](#how-report-generation-works)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Evaluation and Testing](#evaluation-and-testing)
- [Responsible AI Notes](#responsible-ai-notes)
- [Limitations and Future Work](#limitations-and-future-work)
- [Contributing](#contributing)

---

## What It Does

Most UK universities and colleges are under pressure to "do something with AI" — but few have a clear, honest picture of where they actually stand. Without that baseline, strategy becomes guesswork and deployment becomes risk.

The **AI Maturity Assessment Tool** gives institutions a structured, evidence-grounded way to answer the question: *where are we, and what should we do next?*

A user (typically a Deputy Vice-Chancellor, Director of Digital, or equivalent) completes **25 questions** across five dimensions. The application then generates:

- 📊 **An interactive radar chart** showing the institution's maturity profile across all five dimensions at a glance — immediately usable in board presentations
- 📝 **A GPT-4o-mini generated narrative report** tailored to the institution's specific score combination — not generic AI adoption advice, but analysis of their particular strengths and gaps
- ⚡ **A prioritised action plan** with quick wins (0–3 months) and strategic goals (6–18 months)
- 📄 **A downloadable PDF report** suitable for governors, senior leadership teams, or funding applications

**Who is this for?**

| Audience | How they use it |
|---|---|
| Senior leadership teams | Half-day facilitated workshop to establish a shared baseline |
| Directors of Digital / IT | Individual completion to scope a strategy workplan |
| Governors and trustees | Review the PDF output as part of digital governance |
| Sector bodies (e.g. Jisc) | Aggregate anonymised data to benchmark sector progress |
| Researchers and policymakers | Understand where the sector is relative to AI adoption frameworks |

---

## Live Demo

> 🚀 **[Try the live application on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/ai-maturity-tool)**

*(Replace the link above with your actual Hugging Face Spaces URL after deployment. See [Quick Start](#quick-start) for deployment instructions.)*

**No API key required to explore the demo** — a read-only preview mode is available showing a pre-generated sample report for a fictional institution.

---

## The Five Dimensions (and their theoretical grounding)

The five dimensions were not chosen arbitrarily. Each is grounded in established frameworks and designed to be **independently measurable, non-redundant, and collectively sufficient** to describe an institution's AI maturity.

> **Design principle:** No single dimension is sufficient. An institution scoring 5/5 on Use-Case Adoption but 1/5 on Ethics & Governance is in a *more dangerous* position than one scoring 2/5 across all dimensions. The radar chart format makes dangerous imbalances visible at a glance.

---

### 1. 🎯 Strategy & Leadership
*What it measures: Organisational vision, senior buy-in, dedicated roles, and AI roadmap*

**Theoretical grounding:**
Research on technology adoption in public sector organisations consistently shows that senior executive sponsorship is the single strongest predictor of successful, sustained deployment. The ATI's AI Maturity Model (2021) identifies "Strategy and Leadership" as a prerequisite for all other dimensions — you cannot build infrastructure, train staff, or govern AI without an institutional commitment at the top.

| Level | Description |
|---|---|
| 1 — Unaware | No documented AI strategy. AI discussed informally but not resourced |
| 2 — Exploring | Aspirational strategy exists. A senior owner identified. Budget limited |
| 3 — Developing | Strategy approved. Named leadership. Budget allocated |
| 4 — Established | AI embedded in institutional strategy with KPIs and annual review |
| 5 — Leading | AI strategy co-designed with staff, students, and sector partners |

---

### 2. 🏗️ Infrastructure & Data
*What it measures: Cloud readiness, data governance, integration maturity*

**Theoretical grounding:**
The ATI (2021) and the Cabinet Office's AI in Public Sector guidance (2021) both identify data quality and infrastructure maturity as the most common causes of AI project failure. An institution may have strong leadership intent and skilled staff — but if data is siloed, ungoverned, or inaccessible via APIs, AI deployment will fail at the implementation stage.

| Level | Description |
|---|---|
| 1 — Unaware | No cloud infrastructure relevant to AI. Data in silos. No governance policy |
| 2 — Exploring | Some cloud infrastructure. Data governance in draft |
| 3 — Developing | Cloud infrastructure exists but not AI-optimised. Governance partially implemented |
| 4 — Established | Mature cloud infrastructure. Comprehensive data governance. API integration layer |
| 5 — Leading | Purpose-built AI infrastructure. Real-time data pipelines. Sector-leading governance |

---

### 3. 🧠 Skills & Capacity
*What it measures: AI literacy across all staff groups — IT, teaching, leadership*

**Theoretical grounding:**
UNESCO's AI Competency Framework for Teachers (2023) structures AI skill into five progressive levels and explicitly distinguishes between *technical skill* and *critical evaluation capability* — an institution may have highly capable developers but leadership unable to make informed AI procurement decisions. The framework also introduces *student AI literacy* as an institutional responsibility, not merely an individual teacher concern.

| Level | Description |
|---|---|
| 1 — Unaware | No AI training. Staff use tools individually without institutional framework |
| 2 — Exploring | Ad hoc training. Some confident individuals. No structured CPD |
| 3 — Developing | Structured CPD exists for some staff groups. Student AI literacy not addressed |
| 4 — Established | Role-appropriate CPD for all staff groups. Students receive AI literacy education |
| 5 — Leading | AI literacy embedded in induction, appraisal, and curriculum design |

---

### 4. ⚖️ Ethics & Governance
*What it measures: Responsible AI frameworks, bias mitigation, accountability*

**Theoretical grounding:**
Jisc's Responsible and Ethical Use of AI in Higher Education (2024) identifies ethics governance as the dimension most likely to be underdeveloped relative to adoption — institutions under pressure to deploy quickly often do so before governance is in place. The Office for Students' emerging expectations around AI and academic integrity also create a compliance dimension absent from most technical maturity frameworks.

| Level | Description |
|---|---|
| 1 — Unaware | No AI ethics policy. Tools procured without review. No complaints mechanism |
| 2 — Exploring | Ethics framework in development. Some tools reviewed informally |
| 3 — Developing | Published ethics policy. Formal review process for new tools. Complaints route exists |
| 4 — Established | Systematic bias review. Clear accountability. Environmental impact considered |
| 5 — Leading | Ethics framework co-designed with students. Sector contribution. Public reporting |

---

### 5. 🚀 Use-Case Adoption
*What it measures: Active AI deployments and their operational maturity*

**Theoretical grounding:**
Use-Case Adoption is the dimension most visible externally and most frequently cited in institutional press coverage — but it is the *least meaningful in isolation*. High adoption without the other four dimensions is the operational definition of irresponsible AI deployment. This dimension is absent from the ATI's forward-looking framework and was added specifically to measure real-world deployment maturity.

| Level | Description |
|---|---|
| 1 — Unaware | No institutional AI use beyond individual staff use of consumer tools |
| 2 — Exploring | 1–2 informal pilots. No systematic evaluation |
| 3 — Developing | Active pilots with some evaluation. Learning not consistently shared |
| 4 — Established | Multiple deployments evaluated against KPIs. Learning shared institutionally |
| 5 — Leading | AI deployments subject to continuous improvement. Active sector contribution |

---

### Framework Sources

| Framework | Contribution to This Tool |
|---|---|
| [Alan Turing Institute — AI Maturity Model (2021)](https://www.turing.ac.uk/) | Five-level scale; Infrastructure/Data as distinct dimension; governance as parallel track |
| [UNESCO — AI Competency Framework for Teachers (2023)](https://www.unesco.org/en/digital-education/ai-competency-framework-teachers) | Skills dimension structure; student AI literacy as institutional indicator |
| [Jisc — Responsible and Ethical Use of AI in HE (2024)](https://www.jisc.ac.uk/ai) | Ethics dimension; sector-specific framing; UK HE/FE context throughout |
| [Cabinet Office — AI in the Public Sector (2021)](https://www.gov.uk/guidance/ai-in-the-public-sector) | Infrastructure and data governance indicators |

---

## Quick Start

### Prerequisites

- Python 3.11 or later
- An OpenAI API key ([platform.openai.com](https://platform.openai.com)) — approximately £2–4 credit covers extensive testing
- Git

### 1. Clone and Install

```bash
git clone https://github.com/YOUR_USERNAME/ai-maturity-tool.git
cd ai-maturity-tool

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the example env file
cp .env.example .env

# Open .env and add your key
# OPENAI_API_KEY=sk-your-key-here
```

> ⚠️ **Never commit your `.env` file.** It is listed in `.gitignore` by default.

### 3. Run Locally

```bash
streamlit run app.py
# Opens at http://localhost:8501
```

### 4. Deploy to Hugging Face Spaces (Free)

```bash
# 1. Create a new Space at huggingface.co/spaces
#    SDK: Streamlit | Visibility: Public

# 2. Add your API key as a Secret in Space Settings:
#    Key: OPENAI_API_KEY  |  Value: sk-your-key

# 3. Push your code
git remote add space https://huggingface.co/spaces/YOUR_USERNAME/ai-maturity-tool
git push space main

# Live at: https://huggingface.co/spaces/YOUR_USERNAME/ai-maturity-tool
```

### Dependencies

```
streamlit==1.38.0
plotly==5.24.0
openai>=1.52.0        # Must be >=1.52.0 to avoid httpx 'proxies' conflict
httpx>=0.27.0
fpdf2==2.7.9
python-dotenv==1.0.1
pandas==2.2.2
```

> 💡 **If you see `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`**, run:
> ```bash
> pip install --upgrade openai httpx
> ```
> This is caused by an incompatibility between `openai<1.52` and `httpx>=0.28`. Upgrading both resolves it.

---

## How Report Generation Works

Understanding this section matters for interviews — it demonstrates applied LLM knowledge beyond "I called the API".

### Architecture Overview

```
User completes 25 questions
          │
          ▼
  Scores averaged per dimension
  (5 questions × 5 dimensions = 25 total)
          │
          ▼
  radar_chart.py → Plotly radar chart
          │
          ▼
  report_generator.py ──────────────────────────────────┐
          │                                              │
    Scores + rubric + institution context                │
    assembled into structured prompt                     │
          │                                              │
          ▼                                              │
    OpenAI GPT-4o-mini (temperature=0.4)                │
          │                                              │
          ▼                                              │
    Markdown report: Executive Summary,                  │
    Strengths, Gaps, Action Plan, Sector Context         │
          │                                              │
          ▼                                         pdf_generator.py
    Displayed in Streamlit tab                           │
                                                    Downloadable PDF
```

### Prompt Engineering Strategy

The key design decision is **providing the full scoring rubric alongside the scores**. This allows GPT-4o-mini to reason about the *gap* between where the institution is and what "the next level" looks like — rather than producing generic AI adoption advice.

```python
# From report_generator.py
prompt = f"""
Institution: {institution_name} ({institution_type})
Overall Average Score: {avg:.1f}/5
Strongest Dimension: {strongest} ({scores[strongest]:.1f}/5)
Weakest Dimension:   {weakest} ({scores[weakest]:.1f}/5)

MATURITY SCORES:
{score_summary}

SCORING RUBRIC:
1 = Unaware:     No formal AI activity whatsoever
2 = Exploring:   Initial discussions, no coordinated approach
3 = Developing:  Active pilots with some governance, patchy skills
4 = Established: Embedded practices, clear ownership and policy
5 = Leading:     Sector-leading, systematic evaluation, external influence

IMPORTANT CONTEXT:
- An institution scoring high on Use-Case Adoption but low on
  Ethics & Governance is in a RISK position — flag this explicitly
- FE colleges face greater resource constraints — recommendations
  should be proportionate
...
"""
```

**Why `temperature=0.4` and not `0`?**

Unlike a factual Q&A system (where `temperature=0` is appropriate), a strategy recommendations engine benefits from slight variation — two institutions with identical scores should receive reports that feel distinct and relevant, not templated. `0.4` produces differentiated but grounded outputs.

### The Risk Pattern Detection

The prompt explicitly instructs GPT-4o-mini to flag the most common dangerous profile in HE AI adoption — high Use-Case Adoption paired with low Ethics & Governance:

> *"An institution scoring high on Use-Case Adoption but low on Ethics & Governance is in a RISK position — deploying AI without safeguards. Flag this explicitly."*

This is a deliberate design choice grounded in the ATI's observation that governance failures are the most common cause of reputational damage in public sector AI deployments.

### Why the Client Initialises Inside the Function

```python
def generate_maturity_report(scores, institution_name, institution_type):
    # Client created HERE — not at module level
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    ...
```

The OpenAI client is instantiated *inside* the function rather than at module level. This is both a bug fix (prevents `httpx` version conflicts on import) and good practice — the app gracefully handles missing API keys with a user-facing error rather than crashing at startup.

---

## Sample Output

### Radar Chart

The radar chart below shows a typical "grassroots-ahead-of-governance" profile — common in institutions that have responded to external pressure to deploy AI before building the strategic and ethical foundations.

```
        Strategy & Leadership
                5
               /|\
              / | \
             /  |  \
            4   |   4
           /    |    \
          /     |     \
Infrastructure  3  Use-Case
& Data    ─────────────  Adoption
          \     |     /
           \    |    /
            1   |   2
             \  |  /
              \ | /
               \|/
        Skills    Ethics &
        & Capacity  Governance
```

*A balanced profile should form a regular pentagon. The narrow Ethics & Governance spike in the above profile indicates a risk that requires urgent governance development before adoption scales further.*

### Sample Report Excerpt

The following is an excerpt from a GPT-4o-mini generated report for a fictional FE college with the profile above:

---

**Executive Summary**

Northbridge College of Further Education presents an *Exploring* maturity profile with an overall score of 2.28/5. The college demonstrates genuine deployment energy — particularly in Use-Case Adoption (3.0) — but this activity is running significantly ahead of the governance, data infrastructure, and skills foundations needed to sustain it responsibly. The priority is not to slow adoption, but to build the frameworks that make current activity safe and future growth credible.

**Priority Areas for Development**

Ethics & Governance (1.6) represents the most urgent gap and the highest risk. Deploying AI tools — including beneficial ones like formative feedback assistants — without a published ethics policy, bias review process, or student complaints mechanism exposes the college to reputational and regulatory risk under emerging OfS expectations. This gap should be addressed before any new AI tool is deployed...

---

> 📄 **[Download the full sample PDF report](docs/sample_output_northbridge_cfe.pdf)** *(add to your repo after first run)*

---

## Project Structure

```
ai-maturity-tool/
│
├── app.py                    # Main Streamlit application
│                             # Handles UI, session state, tab layout
│
├── questions.py              # The 25 assessment questions
│                             # Organised by dimension with metadata
│
├── radar_chart.py            # Plotly radar chart generator
│                             # Includes benchmark comparison trace
│
├── report_generator.py       # GPT-4o-mini report generation
│                             # Client instantiated inside function (important)
│
├── pdf_generator.py          # FPDF2 PDF report creation
│                             # Score bar visualisation + narrative
│
├── docs/
│   ├── methodology.md        # Full methodology document
│   └── sample_output_northbridge_cfe.pdf
│
├── .env.example              # Template — copy to .env and add API key
├── .gitignore                # Excludes .env, venv/, __pycache__/
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Component | Technology | Version | Rationale |
|---|---|---|---|
| Web UI | Streamlit | 1.38 | Rapid prototyping; no HTML/CSS required; ideal for data apps |
| Visualisation | Plotly | 5.24 | Interactive radar charts; exportable; clean defaults |
| LLM | OpenAI GPT-4o-mini | Latest | Cost-effective (~£0.0002/report); strong instruction-following |
| PDF | FPDF2 | 2.7.9 | Pure Python; no external dependencies; score bar rendering |
| Env management | python-dotenv | 1.0.1 | Keeps API keys out of source code |
| Deployment | Hugging Face Spaces | — | Free tier; widely used in AI community; Streamlit native support |

**Why Streamlit over React/FastAPI?**

The target users for this tool are non-technical senior leaders in HE. Streamlit's constraint (no complex client-side state, linear UI flow) is actually an advantage here — it forces a clean, guided experience that matches how institutional assessments are typically conducted. A React frontend would add complexity without improving the user experience for this audience.

---

## Evaluation and Testing

### Testing the Report Quality

Run the standalone test to verify report generation without launching the UI:

```bash
python report_generator.py
```

This runs a test with a pre-defined score profile for a fictional FE college and prints the full report to the terminal. Verify that:

- The Executive Summary names the correct maturity level
- The risk pattern (high Adoption, low Ethics) is flagged
- The action plan contains exactly 3 quick wins and 3 strategic goals
- Recommendations reference UK sector context (Jisc, OfS, ATI)

### Score Profile Test Cases

Test these profiles to verify the report responds correctly to different patterns:

| Profile | Expected Report Focus |
|---|---|
| All scores = 2.0 | Foundational actions across all dimensions |
| All scores = 4.5 | Sector leadership and external contribution |
| Adoption=5, Ethics=1 | Explicit risk warning and urgent governance actions |
| Strategy=5, Skills=1 | Implementation gap — intent without execution capability |
| Uniform score = 3.0 | Balanced Developing profile with scaling recommendations |

### PDF Validation

```bash
# After generating a report in the UI, verify the PDF:
# 1. Check all five dimension bars render correctly
# 2. Verify the report text is fully visible (no clipping)
# 3. Test with a long institution name (>40 characters)
# 4. Confirm the download button works in deployed environment
```

---

## Responsible AI Notes

This tool is itself an AI application and should be evaluated with the same rigour it asks institutions to apply.

### Mitigations Built In

- **Grounded recommendations:** The LLM is constrained to reason from the provided rubric, not generate unconstrained advice
- **Explicit uncertainty:** The report prompt instructs GPT-4o-mini to distinguish between what the scores show and what they do not tell us
- **Human review recommended:** The tool explicitly recommends that all reports are reviewed by a human before being presented to leadership or governing bodies
- **No personal data stored:** The tool does not persist any institution names, scores, or generated reports — all state is session-only
- **Disclaimer on self-assessment bias:** The methodology document notes that single-respondent self-assessment is subject to social desirability bias and recommends group completion

### Known Limitations

- GPT-4o-mini may occasionally produce recommendations that are sector-appropriate in general but impractical for a specific institution's context (e.g. recommending a dedicated AI Lead role to a college of 200 staff)
- The benchmark comparison in the radar chart is estimated, not based on a validated dataset — this is clearly labelled in the UI
- The tool cannot verify the accuracy of self-reported scores

### Data Handling

```
What is stored:    Nothing persisted beyond the user's browser session
What is sent to OpenAI:  Institution name, institution type, dimension scores
What is NOT sent:  Any student data, staff data, or personally identifiable information
OpenAI data policy:  API calls are not used for model training by default (see OpenAI API Terms)
```

---

## Limitations and Future Work

### Current Limitations

**Self-assessment bias.** The tool measures *perceived* maturity, not verified maturity. An institution may believe its data governance is at Level 4 when an external audit would rate it at Level 2. Group facilitation (multiple senior stakeholders completing the assessment together) significantly reduces this bias — solo completion is a known limitation.

**No validated benchmarks.** The sector benchmark line on the radar chart is based on estimated averages, not real data. Until a sufficient number of institutions complete the assessment to generate genuine norms, this comparison should be treated as indicative only.

**Single-language, single-context.** The tool is designed for UK English and UK regulatory context (OfS, Jisc, HEFCE). It is not suitable for use outside the UK HE/FE sector without significant adaptation of the questions, rubrics, and report prompts.

**No longitudinal tracking.** Each completion is independent. Institutions cannot currently compare their current profile with a previous assessment to track progress over time.

### Roadmap

**Short term (next 3 months)**
- [ ] Add a "preview mode" that shows a sample report without requiring an API key — lowers the barrier for demonstration
- [ ] Add input validation and a progress indicator showing questions answered vs. remaining
- [ ] Improve PDF formatting — add radar chart image to the PDF report

**Medium term (3–12 months)**
- [ ] **Validated sector benchmarks:** Partner with 10–20 institutions to collect anonymised baseline data and replace estimated benchmarks with real ones
- [ ] **Longitudinal tracking:** Allow institutions to save an anonymised token and reload their previous scores for comparison
- [ ] **Facilitated workshop mode:** A projector-friendly version with discussion prompts for each dimension, designed for half-day SLT workshops

**Long term (12+ months)**
- [ ] **Jisc integration:** Map dimensions to Jisc's Digital Maturity Index for cross-tool benchmarking
- [ ] **Multi-respondent mode:** Allow multiple stakeholders to complete the assessment independently, then show the aggregate and the *variance* — the disagreements are often the most valuable output
- [ ] **Evidence upload:** Allow institutions to upload supporting documents (strategy PDFs, policy documents) for an LLM-assisted verification layer

---

## Contributing

Contributions are welcome, particularly from people working in UK HE/FE who can improve the accuracy and relevance of the assessment questions and rubrics.

### How to Contribute

```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/improve-ethics-dimension

# 3. Make your changes
# 4. Write a clear commit message
git commit -m "Improve Ethics & Governance rubric — add OfS reference at Level 3"

# 5. Push and open a Pull Request
git push origin feature/improve-ethics-dimension
```

### Contribution Guidelines

- **Question changes:** Any changes to the 25 assessment questions must be accompanied by a rationale in the PR description explaining the framework grounding for the change
- **Rubric changes:** Level descriptor changes should reference at least one published framework or sector guidance document
- **Code changes:** Follow the existing structure — keep each module single-purpose and document the *why*, not just the *what*
- **No breaking changes to the scoring logic** without a version bump and migration note

### Good First Issues

- Improve the radar chart colour accessibility (current palette may not be sufficient for colour-blind users)
- Add Welsh language support for the questions and report output
- Write unit tests for `radar_chart.py` and `report_generator.py`
- Improve the PDF layout to include the radar chart as an embedded image

### Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. Please be respectful, constructive, and mindful that contributors may be practitioners in education with different levels of technical background.

---

## Licence

MIT Licence — see [LICENSE](LICENSE) for details.

You are free to use, adapt, and deploy this tool for institutional purposes. If you adapt it for your institution, a note crediting the original project is appreciated but not required.

---

## Citation

If you use this tool in research, a report, or a conference presentation, please cite it as:

```
[Your Name] (2025). AI Maturity Assessment Tool for UK Higher Education.
GitHub. https://github.com/YOUR_USERNAME/ai-maturity-tool
```

---

## Acknowledgements

- **Alan Turing Institute** — AI Maturity Model for Public Sector Organisations (2021)
- **UNESCO** — AI Competency Framework for Teachers (2023)
- **Jisc** — Digital Capability Framework and AI guidance for UK HE/FE
- **OpenAI** — GPT-4o-mini API
- **Streamlit** — Open source web framework

---

<div align="center">

**Built with the belief that responsible AI adoption in education requires honest self-assessment before ambitious deployment.**

[Live Demo](https://huggingface.co/spaces/YOUR_USERNAME/ai-maturity-tool) · [Report an Issue](https://github.com/YOUR_USERNAME/ai-maturity-tool/issues) · [Request a Feature](https://github.com/YOUR_USERNAME/ai-maturity-tool/issues)

</div>