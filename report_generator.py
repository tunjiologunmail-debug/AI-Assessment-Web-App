# report_generator.py
# ─────────────────────────────────────────────────────────────────────────────
# PURPOSE: Uses GPT-4o-mini to generate a personalised maturity report.
# The OpenAI client is initialised INSIDE the function (not at module level)
# to avoid import-time errors caused by httpx version conflicts.
# ─────────────────────────────────────────────────────────────────────────────

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# ── System prompt ─────────────────────────────────────────────────────────────
# Defined at module level (just a string — safe, no client involved)
SYSTEM_PROMPT = """You are an expert AI strategy consultant specialising in
UK higher education. You help universities and colleges understand their
AI maturity and develop practical roadmaps for improvement.

Your reports are:
- Specific to the institution's actual score profile (not generic)
- Grounded in UK HE context (Jisc, OfS, HEFCE, sector norms)
- Practical and actionable, not theoretical
- Honest about gaps without being discouraging
- Written for a Deputy Vice-Chancellor, not a developer
"""


# ── Main report generation function ──────────────────────────────────────────
def generate_maturity_report(
    scores: dict,
    institution_name: str,
    institution_type: str = "university"
) -> str:
    """
    Generates a personalised narrative report from maturity scores.

    The OpenAI client is created INSIDE this function — not at module level.
    This prevents the 'proxies' TypeError that occurs when the client is
    instantiated on import in environments with httpx >= 0.28.0.

    Parameters:
    -----------
    scores           : {'Strategy & Leadership': 3.4, 'Infrastructure': 2.8, ...}
    institution_name : Shown in the report header and recommendations
    institution_type : 'university', 'Further Education College', etc.

    Returns:
    --------
    A markdown-formatted string containing the full report.
    """

    # ── Initialise client here, not at module level ───────────────────────────
    # This is the key fix: instantiating inside the function means it only
    # runs when a report is actually requested, not when the module is imported.
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # ── Format scores for the prompt ──────────────────────────────────────────
    score_summary = "\n".join(
        f"- {dim}: {score:.1f}/5" for dim, score in scores.items()
    )

    avg = sum(scores.values()) / len(scores)

    # Identify strongest and weakest dimensions for more targeted prompt
    strongest = max(scores, key=scores.get)
    weakest   = min(scores, key=scores.get)

    # ── Build the user prompt ─────────────────────────────────────────────────
    # We give the model the full rubric alongside the scores so it can reason
    # about the GAP between current state and next level — not just give
    # generic AI adoption advice.
    prompt = f"""
Institution: {institution_name} ({institution_type})
Overall Average Score: {avg:.1f}/5
Strongest Dimension: {strongest} ({scores[strongest]:.1f}/5)
Weakest Dimension:   {weakest} ({scores[weakest]:.1f}/5)

MATURITY SCORES:
{score_summary}

SCORING RUBRIC:
1 = Unaware:     No formal AI activity whatsoever
2 = Exploring:   Initial discussions and isolated experiments, no coordinated approach
3 = Developing:  Active pilots with some governance, patchy skills and policy
4 = Established: Embedded practices with clear ownership, policy, and staff development
5 = Leading:     Sector-leading: systematic evaluation, continuous improvement, external influence

IMPORTANT CONTEXT:
- An institution scoring high on Use-Case Adoption but low on Ethics & Governance
  is in a RISK position — flag this explicitly if present
- An institution scoring high on Strategy but low on Skills & Capacity has an
  implementation gap — leadership intent without execution capability
- FE colleges typically face greater resource constraints than universities —
  recommendations should be proportionate

Please write a maturity assessment report with EXACTLY these five sections:

## Executive Summary
2-3 sentences summarising the institution's overall AI maturity position.
Be specific about their score profile, not generic. Name the overall level
(Unaware / Exploring / Developing / Established / Leading).

## Strengths
Identify the 1-2 highest scoring dimensions. Explain in concrete terms what
this means for the institution's day-to-day operations and strategic position.
What does this strength enable them to do that lower-scoring peers cannot?

## Priority Areas for Development
Identify the 1-2 lowest scoring dimensions. Explain the real-world risk of
leaving these gaps unaddressed — be specific to their actual score combination,
not generic. If Use-Case Adoption is significantly ahead of Ethics & Governance,
call this out as a risk pattern explicitly.

## Recommended Action Plan
### Quick Wins (0–3 months)
List exactly 3 specific, actionable quick wins. Each should be achievable
without significant budget and should address the weakest dimensions.
Reference specific sector resources where appropriate (e.g. Jisc's AI ethics
principles, Alan Turing Institute guidance, OfS expectations).

### Strategic Goals (6–18 months)
List exactly 3 strategic goals that build on the quick wins. These may require
resource, role changes, or external partnerships.

## Sector Context
1 paragraph placing this institution's score relative to the UK HE/FE sector.
Reference relevant sector trends, Jisc guidance, or government policy where
appropriate. Be encouraging but honest.
"""

    # ── Call the API ──────────────────────────────────────────────────────────
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.4,   # Slight creativity for varied but grounded recommendations
        max_tokens=1800    # Enough for a full structured report
    )

    return response.choices[0].message.content


# ── Streaming version ─────────────────────────────────────────────────────────
def generate_maturity_report_streaming(
    scores: dict,
    institution_name: str,
    institution_type: str = "university"
):
    """
    Streaming version — yields report text token by token.
    Use with Streamlit's st.write_stream() for a faster-feeling UI.

    Usage in app.py:
        report_container = st.empty()
        full_report = ""
        for chunk in generate_maturity_report_streaming(scores, name, type):
            full_report += chunk
            report_container.markdown(full_report)
    """

    # Client initialised inside function — same fix as non-streaming version
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    score_summary = "\n".join(
        f"- {dim}: {score:.1f}/5" for dim, score in scores.items()
    )
    avg     = sum(scores.values()) / len(scores)
    strongest = max(scores, key=scores.get)
    weakest   = min(scores, key=scores.get)

    prompt = f"""
Institution: {institution_name} ({institution_type})
Overall Average Score: {avg:.1f}/5
Strongest Dimension: {strongest} ({scores[strongest]:.1f}/5)
Weakest Dimension:   {weakest} ({scores[weakest]:.1f}/5)

MATURITY SCORES:
{score_summary}

SCORING RUBRIC:
1=Unaware | 2=Exploring | 3=Developing | 4=Established | 5=Leading

Please write a concise but specific maturity assessment report covering:
## Executive Summary
## Strengths
## Priority Areas for Development
## Recommended Action Plan (Quick Wins + Strategic Goals)
## Sector Context
"""

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.4,
        max_tokens=1800,
        stream=True   # Enable streaming
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta is not None:
            yield delta


# ── Quick standalone test ─────────────────────────────────────────────────────
# Run with: python report_generator.py
if __name__ == "__main__":
    test_scores = {
        "Strategy & Leadership":  2.4,
        "Infrastructure & Data":  1.8,
        "Skills & Capacity":      2.6,
        "Ethics & Governance":    1.6,
        "Use-Case Adoption":      3.0,
    }

    print("Generating test report...\n")
    report = generate_maturity_report(
        scores=test_scores,
        institution_name="Northbridge College of Further Education",
        institution_type="Further Education College"
    )
    print(report)