import pandas as pd
import plotly.express as px
import streamlit as st
from deep_translator import GoogleTranslator

from career_engine import analyze_student
from database import init_db, save_student
from qr_generator import generate_qr
from report_generator import create_report
from utils.ui import info_card, inject_global_styles, page_intro, section_title

st.set_page_config(page_title="FuturePath AI", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")
inject_global_styles()
init_db()

page_intro("FUTUREPATH AI • CAREER INTELLIGENCE", "اكتشف مسارك المهني بثقة", "منصة ذكية تساعد الطلاب على فهم ميولهم، استكشاف التخصصات المناسبة، وبناء خطوة أوضح نحو المستقبل.")

intro_cols = st.columns(3)
with intro_cols[0]: info_card("🧭", "توجيه شخصي", "تحليل مبني على اهتماماتك وميولك المهنية.")
with intro_cols[1]: info_card("⚡", "تحليل ذكي", "نتائج واضحة تساعدك على اتخاذ قرار أفضل.")
with intro_cols[2]: info_card("🚀", "خطوة للمستقبل", "تخصصات ودورات وجامعات في تجربة واحدة.")

section_title("ابدأ رحلتك", "أدخل بياناتك وأجب عن الأسئلة بصراحة للحصول على توصية أدق.")

with st.form("career_assessment"):
    profile_cols = st.columns([1.5, 1, 1])
    with profile_cols[0]: name = st.text_input("اسم الطالب", placeholder="اكتب الاسم هنا")
    with profile_cols[1]: grade = st.selectbox("الصف الدراسي", ["الأول الثانوي", "الثاني الثانوي", "الثالث الثانوي"])
    with profile_cols[2]: gpa = st.slider("المعدل الدراسي", 60, 100, 90, format="%d٪")
    
    section_title("اختبار الميول المهنية", "قيّم مدى انطباق كل عبارة عليك من 1 إلى 5.")
    questions = [
        ("logic", "أحب حل المشكلات التقنية", "🧩"), 
        ("security", "أهتم بالأمن السيبراني", "🛡️"), 
        ("ai", "أهتم بالذكاء الاصطناعي", "🤖"), 
        ("data", "أحب تحليل البيانات", "📊"), 
        ("software", "أحب البرمجة وتطوير التطبيقات", "💻")
    ]
    answer_cols = st.columns(5)
    answers = {}
    for col, (key, label, icon) in zip(answer_cols, questions):
        with col:
            st.markdown(f"<div class='fp-note' style='font-weight:600; margin-bottom: 0.25rem;'>{icon} {label}</div>", unsafe_allow_html=True)
            answers[key] = st.slider(label, 1, 5, 3, key=f"question_{key}", label_visibility="collapsed")
            
    submitted = st.form_submit_button("تحليل مساري المهني  →", use_container_width=True)

if submitted:
    if not name.strip(): 
        st.warning("يرجى إدخل اسم الطالب للمتابعة.")
        st.stop()
        
    results = analyze_student(answers)
    save_student(name, grade, gpa, str(results))
    st.success("تم تحليل بياناتك بنجاح. هذه هي التوصية الأولية لمسارك:")
    
    result_cols = st.columns([1.35, .65])
    with result_cols[0]:
        df = pd.DataFrame(results, columns=["التخصص", "النسبة"])
        fig = px.bar(
            df, 
            x="النسبة", 
            y="التخصص", 
            orientation="h", 
            color="النسبة", 
            color_continuous_scale=["#1e3a8a", "#2563eb", "#60a5fa"]
        )
        fig.update_layout(
            template="plotly_dark", 
            height=390, 
            margin=dict(l=10, r=10, t=25, b=10), 
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)", 
            coloraxis_showscale=False, 
            yaxis_title="", 
            xaxis_title="نسبة التوافق (%)",
            font=dict(family="Cairo, sans-serif", size=13)
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
        
    with result_cols[1]:
        best_major = results[0][0]
        st.markdown(f"<div class='fp-recommendation' dir='rtl'><small style='color:#94a3b8;'>التخصص الأقرب لميولك</small><h2>{best_major}</h2><p class='fp-note'>هذه النتيجة بداية جيدة لاستكشاف خياراتك التعليمية والمهنية.</p></div>", unsafe_allow_html=True)
        major_translation = {
            "علوم الحاسب": "Computer Science", 
            "هندسة البرمجيات": "Software Engineering", 
            "الأمن السيبراني": "Cyber Security", 
            "الذكاء الاصطناعي": "Artificial Intelligence", 
            "علوم البيانات": "Data Science", 
            "تحليل البيانات": "Data Analytics", 
            "تطوير البرمجيات": "Software Development"
        }
        qr_text = f"الطالب: {name}\nالصف: {grade}\nالمعدل: {gpa}\nالتخصص المقترح: {best_major}"
        st.image(generate_qr(qr_text), width=150)
        
    try: 
        student_name_en = GoogleTranslator(source="ar", target="en").translate(name)
    except Exception: 
        student_name_en = name
        
    pdf_file = create_report(student_name_en, major_translation.get(best_major, best_major))
    with open(pdf_file, "rb") as file: 
        st.download_button("تحميل التقرير PDF", data=file, file_name="FuturePath_Report.pdf", mime="application/pdf")

st.markdown("<div class='fp-note' style='text-align:center;margin-top:3rem'>FuturePath AI · نبني قراراً أوضح لمستقبل أكثر إشراقاً</div>", unsafe_allow_html=True)