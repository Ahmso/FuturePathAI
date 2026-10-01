from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / "assets" / "fonts" / "NotoSansArabic-Regular.ttf"


def inject_global_styles() -> None:
    """Apply the FuturePath AI visual system to the current Streamlit page."""
    font_css = ""
    if FONT_PATH.exists():
        font_css = f"""
        @font-face {{
            font-family: 'FuturePathArabic';
            src: url('file://{FONT_PATH.as_posix()}');
            font-weight: 400;
        }}
        """

    st.markdown(
        f"""
        <style>
        {font_css}
        :root {{
            --fp-bg: #07111f;
            --fp-panel: rgba(14, 32, 54, .82);
            --fp-panel-soft: rgba(18, 42, 69, .66);
            --fp-line: rgba(103, 232, 249, .18);
            --fp-cyan: #67e8f9;
            --fp-blue: #60a5fa;
            --fp-violet: #a78bfa;
            --fp-muted: #a9bad0;
        }}
        html, body, [class*="css"] {{ font-family: 'FuturePathArabic', 'Noto Sans Arabic', sans-serif; }}
        .stApp {{ background: radial-gradient(circle at 85% 0%, rgba(30, 92, 145, .28), transparent 36%), var(--fp-bg); }}
        [data-testid="stHeader"] {{ background: transparent; }}
        [data-testid="stSidebar"] {{ background: linear-gradient(180deg, #0a1a2d 0%, #07111f 100%); border-left: 1px solid var(--fp-line); }}
        [data-testid="stSidebarNav"] {{ padding-top: 1.5rem; }}
        [data-testid="stSidebarNav"] span {{ font-size: .95rem; }}
        .block-container {{ max-width: 1220px; padding-top: 2.2rem; padding-bottom: 4rem; }}
        h1, h2, h3 {{ letter-spacing: -.02em; }}
        h1 {{ font-size: clamp(2rem, 4vw, 3.25rem) !important; }}
        h2 {{ color: #eaf6ff; }}
        h3 {{ color: var(--fp-cyan); }}
        .stButton > button, .stDownloadButton > button {{
            border: 1px solid rgba(103, 232, 249, .45); border-radius: 12px; color: #06111d;
            background: linear-gradient(135deg, var(--fp-cyan), var(--fp-blue)); font-weight: 700;
            min-height: 2.8rem; transition: transform .2s ease, box-shadow .2s ease;
        }}
        .stButton > button:hover, .stDownloadButton > button:hover {{ transform: translateY(-2px); box-shadow: 0 10px 30px rgba(96, 165, 250, .25); }}
        .stTextInput input, .stSelectbox [data-baseweb="select"], .stNumberInput input {{ border-radius: 12px; border: 1px solid var(--fp-line); background: rgba(10, 27, 46, .8); }}
        [data-testid="stMetric"] {{ background: var(--fp-panel); border: 1px solid var(--fp-line); border-radius: 16px; padding: 1rem; box-shadow: 0 12px 35px rgba(0,0,0,.16); }}
        [data-testid="stMetricLabel"] {{ color: var(--fp-muted); }}
        [data-testid="stMetricValue"] {{ color: var(--fp-cyan); }}
        [data-testid="stDataFrame"] {{ border: 1px solid var(--fp-line); border-radius: 14px; overflow: hidden; }}
        .fp-hero {{ position: relative; overflow: hidden; padding: 2.8rem 3rem; border: 1px solid var(--fp-line); border-radius: 26px; background: linear-gradient(120deg, rgba(14, 45, 76, .94), rgba(20, 26, 63, .9)); box-shadow: 0 25px 80px rgba(0,0,0,.22); margin-bottom: 1.5rem; }}
        .fp-hero:after {{ content: ''; position: absolute; width: 250px; height: 250px; left: -80px; top: -100px; border-radius: 50%; background: rgba(103,232,249,.12); filter: blur(2px); }}
        .fp-kicker {{ color: var(--fp-cyan); font-size: .85rem; letter-spacing: .16em; text-transform: uppercase; font-weight: 700; }}
        .fp-hero h1 {{ margin: .35rem 0 .55rem; color: #fff; }}
        .fp-hero p {{ color: #c3d6e9; max-width: 720px; font-size: 1.08rem; line-height: 1.9; margin: 0; }}
        .fp-section {{ margin: 1.5rem 0 .8rem; padding-bottom: .6rem; border-bottom: 1px solid var(--fp-line); }}
        .fp-card {{ height: 100%; padding: 1.25rem; border: 1px solid var(--fp-line); border-radius: 18px; background: linear-gradient(145deg, var(--fp-panel), var(--fp-panel-soft)); }}
        .fp-card .icon {{ font-size: 1.8rem; }}
        .fp-card h4 {{ margin: .55rem 0 .3rem; color: #f2f8ff; }}
        .fp-card p {{ color: var(--fp-muted); line-height: 1.75; margin: 0; }}
        .fp-recommendation {{ padding: 1.35rem 1.5rem; border-radius: 18px; border: 1px solid rgba(103,232,249,.45); background: linear-gradient(120deg, rgba(19, 67, 88, .8), rgba(45, 35, 94, .72)); margin: 1.2rem 0; }}
        .fp-recommendation small {{ color: var(--fp-cyan); }}
        .fp-recommendation h2 {{ margin: .35rem 0 0; color: #fff; }}
        .fp-note {{ color: var(--fp-muted); font-size: .9rem; line-height: 1.8; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_intro(kicker: str, title: str, description: str) -> None:
    st.markdown(
        f"""<section class="fp-hero" dir="rtl">
        <div class="fp-kicker">{kicker}</div>
        <h1>{title}</h1>
        <p>{description}</p>
        </section>""",
        unsafe_allow_html=True,
    )


def section_title(title: str, caption: str = "") -> None:
    extra = f"<div class='fp-note'>{caption}</div>" if caption else ""
    st.markdown(f"<div class='fp-section'><h3>{title}</h3>{extra}</div>", unsafe_allow_html=True)


def info_card(icon: str, title: str, text: str) -> None:
    st.markdown(f"""<div class="fp-card" dir="rtl"><div class="icon">{icon}</div><h4>{title}</h4><p>{text}</p></div>""", unsafe_allow_html=True)
