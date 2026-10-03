import streamlit as st

def inject_global_styles():
    st.markdown("""
    <style>
    /* استدعاء خط Cairo العصري من Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    :root {
        --font-family: 'Cairo', system-ui, -apple-system, sans-serif;
        --bg-color: #0f172a;
        --card-bg: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --accent-primary: #2563eb;
        --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        --border-color: #334155;
        --border-radius: 12px;
    }

    /* تطبيق الخط واتجاه النص العريض */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: var(--font-family) !important;
        direction: rtl;
        text-align: right;
    }

    /* تحسين خطوط جميع النصوص والعناوين */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        font-family: var(--font-family) !important;
    }

    h1, h2 {
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em;
    }

    /* تنسيق بطاقات المعلومات (Info Cards) */
    .fp-card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 1.25rem;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .fp-card:hover {
        border-color: #60a5fa;
        transform: translateY(-2px);
    }

    .fp-card-icon {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }

    .fp-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.25rem;
    }

    .fp-card-desc {
        font-size: 0.9rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }

    .fp-note {
        color: var(--text-secondary);
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* بطاقة النتيجة والتوصية النهائية */
    .fp-recommendation {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #3b82f6;
        border-radius: var(--border-radius);
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.15);
    }

    .fp-recommendation h2 {
        color: #60a5fa !important;
        font-size: 1.8rem;
        margin: 0.5rem 0;
    }

    /* الأزرار العصرية */
    .stButton > button, div[data-testid="stFormSubmitButton"] > button {
        font-family: var(--font-family) !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        background: var(--accent-gradient) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.65rem 1.5rem !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        opacity: 0.95;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3) !important;
    }

    /* تحسين خيارات الإدخال والقوائم */
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        border-radius: 8px !important;
        border-color: var(--border-color) !important;
    }

    .stSlider {
        padding-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

def page_intro(tag, title, subtitle):
    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <span style="background: rgba(59, 130, 246, 0.12); color: #60a5fa; padding: 4px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em;">
            {tag}
        </span>
        <h1 style="margin-top: 0.75rem; margin-bottom: 0.5rem; font-size: 2.2rem;">{title}</h1>
        <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.6; margin: 0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def section_title(title, subtitle=""):
    sub_html = f"<p style='color: #94a3b8; font-size: 0.95rem; margin-top: 0.25rem;'>{subtitle}</p>" if subtitle else ""
    st.markdown(f"""
    <div style="margin-top: 2rem; margin-bottom: 1rem;">
        <h3 style="margin: 0; font-size: 1.4rem;">{title}</h3>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)

def info_card(icon, title, description):
    st.markdown(f"""
    <div class="fp-card">
        <div class="fp-card-icon">{icon}</div>
        <div class="fp-card-title">{title}</div>
        <div class="fp-card-desc">{description}</div>
    </div>
    """, unsafe_allow_html=True)