# Main Streamlit application for the AI Maturity Assessment Tool.
# Run with: streamlit run app.py
 
import streamlit as st
import os
from dotenv import load_dotenv
from questions import DIMENSIONS, RATING_LABELS
from radar_chart import create_radar_chart, get_overall_maturity_label
from report_generator import generate_maturity_report
from pdf_generator import generate_pdf_report
 
load_dotenv()
 
st.set_page_config(
    page_title='AI Maturity Assessment Tool',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)
 
# Custom CSS for a professional look
st.markdown('''
<style>
  .dimension-header {
    background: linear-gradient(135deg, #1A3A6B, #2E6DA4);
    color: white; padding: 1rem; border-radius: 8px; margin: 1rem 0;
  }
  .score-badge {
    background: #EAF2FB; border: 2px solid #2E6DA4;
    border-radius: 20px; padding: 4px 12px; font-weight: bold;
  }
  .maturity-level {
    font-size: 1.5rem; font-weight: bold; margin: 1rem 0;
  }
</style>
''', unsafe_allow_html=True)
 
 
# ── Sidebar ──────────────────────────────────────────────────────────
with st.sidebar:
    st.image('https://via.placeholder.com/180x50?text=AI+Maturity', width=180)
    st.markdown('## About This Tool')
    st.markdown('''
    This tool helps UK universities and colleges assess their AI
    maturity across five dimensions, generating a personalised
    report with actionable next steps.
    ''')
    st.markdown('---')
    st.markdown('**Framework grounded in:**')
    st.markdown('- Alan Turing Institute AI Maturity Model')
    st.markdown('- UNESCO AI Competency Framework')
    st.markdown('- Jisc Digital Capability Framework')
    st.markdown('---')
    st.caption('Built as a portfolio project for AI roles in HE')
 
 
# ── Main UI ──────────────────────────────────────────────────────────
st.title('📊 AI Maturity Assessment Tool')
st.markdown('**For UK Higher and Further Education Institutions**')
st.markdown('Complete all 25 questions (5 per dimension) to receive your personalised report.')
st.markdown('---')
 
# Institution details
col1, col2 = st.columns(2)
with col1:
    institution_name = st.text_input(
        'Institution Name',
        placeholder='e.g. Northbridge University'
    )
with col2:
    institution_type = st.selectbox(
        'Institution Type',
        ['University', 'Further Education College',
         'Higher Education College', 'Research Institute']
    )
 
st.markdown('---')
 
# ── Assessment Questions ─────────────────────────────────────────────
all_scores = {}
 
for dim_name, dim_data in DIMENSIONS.items():
    st.markdown(
        f'<div class="dimension-header">'
        f'<h3>{dim_data["icon"]} {dim_name}</h3>'
        f'<p style="margin:0; opacity:0.9">{dim_data["description"]}</p>'
        f'</div>',
        unsafe_allow_html=True
    )
 
    dim_scores = []
    for i, question in enumerate(dim_data['questions'], 1):
        score = st.radio(
            label=f'{i}. {question}',
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: f'{x} — {RATING_LABELS[x]}',
            horizontal=True,
            key=f'{dim_name}_{i}'
        )
        dim_scores.append(score)
 
    dim_average = sum(dim_scores) / len(dim_scores)
    all_scores[dim_name] = round(dim_average, 2)
 
    # Show live dimension average as user completes each section
    st.markdown(
        f'<div style="text-align:right">'
        f'<span class="score-badge">{dim_name} Average: {dim_average:.1f}/5</span>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown('')
 
 
# ── Generate Report ───────────────────────────────────────────────────
st.markdown('---')
generate_btn = st.button(
    '📊 Generate My AI Maturity Report',
    type='primary',
    use_container_width=True
)
 
if generate_btn:
    if not institution_name.strip():
        st.error('Please enter your institution name.')
        st.stop()
 
    overall_avg = sum(all_scores.values()) / len(all_scores)
    label, description, colour = get_overall_maturity_label(overall_avg)
 
    # ── Results Tabs ─────────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(['📈 Radar Chart', '📝 Full Report', '📄 Download PDF'])
 
    with tab1:
        st.markdown(f'### Overall Maturity Level: {label}')
        st.markdown(f'**Average Score:** {overall_avg:.1f}/5  |  {description}')
        fig = create_radar_chart(all_scores, institution_name)
        st.plotly_chart(fig, use_container_width=True)
 
        # Dimension score summary
        st.markdown('### Dimension Breakdown')
        cols = st.columns(5)
        for i, (dim, score) in enumerate(all_scores.items()):
            with cols[i]:
                lbl, _, clr = get_overall_maturity_label(score)
                st.metric(label=dim.split('&')[0].strip(), value=f'{score:.1f}/5', delta=lbl)
 
    with tab2:
        with st.spinner('Generating your personalised report...'):
            report = generate_maturity_report(all_scores, institution_name, institution_type)
        st.markdown(report)
 
    with tab3:
        with st.spinner('Creating PDF...'):
            if 'report' not in dir():
                report = generate_maturity_report(all_scores, institution_name, institution_type)
            pdf_path = generate_pdf_report(institution_name, all_scores, report)
        with open(pdf_path, 'rb') as f:
            st.download_button(
                label='⬇️ Download Full Report (PDF)',
                data=f,
                file_name=f'{institution_name.replace(" ", "_")}_AI_Maturity_Report.pdf',
                mime='application/pdf',
                use_container_width=True
            )
        st.success('Your report is ready to download!')
        st.caption('Share this PDF with your senior leadership team or governing body.')
