# Generates an interactive Plotly radar chart from maturity scores.
# The radar chart shows all five dimensions at a glance — immediately
# useful in a leadership presentation or board meeting.
 
import plotly.graph_objects as go
import plotly.io as pio
 
 
def create_radar_chart(scores: dict, institution_name: str = 'Your Institution') -> go.Figure:
    """
    Creates a radar chart from a dictionary of dimension scores.
 
    Parameters:
    -----------
    scores           : {'Strategy & Leadership': 3.4, 'Infrastructure & Data': 2.8, ...}
    institution_name : Used in the chart title
 
    Returns:
    --------
    A Plotly Figure object (can be displayed with st.plotly_chart())
    """
 
    dimensions = list(scores.keys())
    values = list(scores.values())
 
    # Radar charts need the first point repeated at the end to close the polygon
    dimensions_closed = dimensions + [dimensions[0]]
    values_closed = values + [values[0]]
 
    fig = go.Figure()
 
    # The institution's score trace
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=dimensions_closed,
        fill='toself',
        fillcolor='rgba(46, 109, 164, 0.2)',   # Semi-transparent blue fill
        line=dict(color='#2E6DA4', width=2),
        name=institution_name,
        hovertemplate='<b>%{theta}</b><br>Score: %{r:.1f}/5<extra></extra>'
    ))
 
    # Add a 'sector average' benchmark trace for context
    # In production, replace these with real benchmarks from your dataset
    benchmark = [3.0, 2.8, 2.5, 2.7, 2.6]  # Estimated UK HE averages
    benchmark_closed = benchmark + [benchmark[0]]
 
    fig.add_trace(go.Scatterpolar(
        r=benchmark_closed,
        theta=dimensions_closed,
        fill='toself',
        fillcolor='rgba(200, 200, 200, 0.1)',
        line=dict(color='#AAAAAA', width=1, dash='dot'),
        name='Sector Benchmark (estimated)'
    ))
 
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['1\nUnaware', '2\nExploring', '3\nDeveloping',
                          '4\nEstablished', '5\nLeading'],
                tickfont=dict(size=10),
            )
        ),
        showlegend=True,
        title=dict(
            text=f'AI Maturity Profile: {institution_name}',
            font=dict(size=16, color='#1A3A6B')
        ),
        height=500,
        margin=dict(t=80, b=40, l=80, r=80)
    )
 
    return fig
 
 
def get_overall_maturity_label(avg_score: float) -> tuple:
    """Returns (label, description, colour) for an overall average score."""
    if avg_score < 1.5:
        return 'Unaware', 'AI adoption has not yet begun in a meaningful way.', '#C0392B'
    elif avg_score < 2.5:
        return 'Exploring', 'Initial interest and some experiments, but no coordinated approach.', '#E67E22'
    elif avg_score < 3.5:
        return 'Developing', 'Active work underway with some governance and skills development.', '#F1C40F'
    elif avg_score < 4.5:
        return 'Established', 'AI is embedded with clear ownership, policy, and staff development.', '#27AE60'
    else:
        return 'Leading', 'Sector-leading practice with systematic evaluation and external influence.', '#1A7A6E'
