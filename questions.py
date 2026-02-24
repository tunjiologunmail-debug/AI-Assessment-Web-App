# 25 assessment questions across 5 AI maturity dimensions.
# Each question is scored 1-5: 1=Not at all, 3=Partially, 5=Fully
 
DIMENSIONS = {
    'Strategy & Leadership': {
        'description': 'Organisational vision, leadership commitment, and AI roadmap',
        'icon': '🎯',
        'colour': '#2E6DA4',
        'questions': [
            'Our institution has a documented AI strategy approved by senior leadership.',
            'There is a named senior leader (e.g. Deputy VC or Director) responsible for AI.',
            'AI is included in our institutional digital transformation roadmap.',
            'We have dedicated budget allocated for AI initiatives this academic year.',
            'Our AI strategy references ethical principles and responsible deployment.',
        ]
    },
    'Infrastructure & Data': {
        'description': 'Technical foundations, cloud readiness, and data governance',
        'icon': '🏗️',
        'colour': '#1A7A6E',
        'questions': [
            'We have a cloud infrastructure capable of supporting AI workloads.',
            'Our institution has a formal data governance policy covering AI use.',
            'Student and staff data is properly classified and access-controlled.',
            'We have APIs or integration layers that allow AI tools to connect to our systems.',
            'We conduct regular data quality audits relevant to AI applications.',
        ]
    },
    'Skills & Capacity': {
        'description': 'AI literacy and capability across all staff groups',
        'icon': '🧠',
        'colour': '#7D3C98',
        'questions': [
            'Teaching staff can critically evaluate AI tools for pedagogical use.',
            'IT and digital teams have technical AI skills (ML, prompt engineering, APIs).',
            'Leadership understands AI well enough to make informed strategic decisions.',
            'We offer structured AI training and CPD for staff at all levels.',
            'Students receive explicit AI literacy education within their programmes.',
        ]
    },
    'Ethics & Governance': {
        'description': 'Responsible AI frameworks, bias mitigation, and accountability',
        'icon': '⚖️',
        'colour': '#B7770D',
        'questions': [
            'We have a published AI ethics policy accessible to staff and students.',
            'AI tools are reviewed for bias and fairness before institutional deployment.',
            'There is a clear process for students or staff to raise AI-related concerns.',
            'We assess the environmental impact (energy use) of AI tools we procure.',
            'Our AI governance aligns with sector guidance (e.g. Jisc, Office for AI).',
        ]
    },
    'Use-Case Adoption': {
        'description': 'Active AI deployments and their maturity',
        'icon': '🚀',
        'colour': '#C0392B',
        'questions': [
            'AI is actively used in at least one student-facing service (e.g. support, feedback).',
            'AI tools are used in administrative or operational processes (e.g. scheduling, reporting).',
            'We evaluate the effectiveness of deployed AI tools against defined metrics.',
            'We share learning from AI pilots internally across departments.',
            'We contribute to or learn from sector-wide AI pilots (e.g. via Jisc, UUK).',
        ]
    },
}
 
RATING_LABELS = {
    1: 'Not at all',
    2: 'In early stages',
    3: 'Partially in place',
    4: 'Largely in place',
    5: 'Fully in place',
}