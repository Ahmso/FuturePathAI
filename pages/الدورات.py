import streamlit as st
from utils.ui import info_card, inject_global_styles, page_intro, section_title

st.set_page_config(page_title="الدورات | FuturePath AI", page_icon="📚", layout="wide")
inject_global_styles()
page_intro("LEARN & GROW", "الدورات التعليمية", "مساحة مخصصة لبناء مكتبة تعلم مرتبطة باهتماماتك ونتائج تحليلك المهني.")
section_title("ماذا ستجد هنا؟", "سيتم ربط هذه المساحة بالدورات المناسبة لكل مسار مهني في المرحلة التالية.")
cols = st.columns(3)
with cols[0]: info_card("🎯", "مسارات مخصصة", "دورات مرتبة حسب التخصص والمهارات التي تحتاج إلى تطويرها.")
with cols[1]: info_card("🧠", "تعلم عملي", "محتوى يركز على المشاريع والتطبيق وليس المعرفة النظرية فقط.")
with cols[2]: info_card("📈", "تقدم قابل للقياس", "تابع إنجازك وابنِ ملفاً تعليمياً يدعم مستقبلك.")
st.info("ستظهر قائمة الدورات عند إضافة مصادر المحتوى إلى قاعدة بيانات المشروع.")
