import streamlit as st
from utils.ui import info_card, inject_global_styles, page_intro

st.set_page_config(page_title="نتائج التحليل | FuturePath AI", page_icon="🧠", layout="wide")
inject_global_styles()
page_intro("YOUR INSIGHTS", "نتائج التحليل", "ستجد هنا ملخصات تحليلاتك السابقة والتوصيات التي تم حفظها من رحلاتك المهنية.")
cols = st.columns(3)
with cols[0]: info_card("🧭", "مسارك الأقرب", "استعرض التخصصات التي تتوافق أكثر مع ميولك.")
with cols[1]: info_card("📌", "توصيات محفوظة", "احتفظ بالنتائج التي تريد الرجوع إليها لاحقاً.")
with cols[2]: info_card("📄", "تقاريرك", "حمّل تقريراً منظماً لمشاركته مع المعلم أو ولي الأمر.")
st.info("ستظهر النتائج المحفوظة هنا بعد تفعيل سجل المستخدمين في النسخة القادمة.")
