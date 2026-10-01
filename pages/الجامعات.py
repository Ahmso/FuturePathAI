import pandas as pd
import streamlit as st
from utils.ui import inject_global_styles, page_intro, section_title

st.set_page_config(page_title="الجامعات المقترحة | FuturePath AI", page_icon="🏛️", layout="wide")
inject_global_styles()
page_intro("EXPLORE YOUR OPTIONS", "الجامعات المقترحة", "استكشف الخيارات الأكاديمية المتاحة وابدأ بتكوين صورة أوضح عن خطوتك التعليمية القادمة.")
df = pd.read_csv("data/universities.csv")
section_title("دليل الجامعات", f"تم العثور على {len(df)} خياراً تعليمياً في قاعدة البيانات الحالية.")
st.dataframe(df, use_container_width=True, hide_index=True)
st.markdown("<div class='fp-note'>نصيحة: استخدم بيانات الجدول كنقطة بداية، ثم تحقق من شروط القبول والتخصصات من الموقع الرسمي لكل جامعة.</div>", unsafe_allow_html=True)
