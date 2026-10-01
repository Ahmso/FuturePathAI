import sqlite3
import pandas as pd
import streamlit as st
from utils.ui import inject_global_styles, page_intro, section_title

st.set_page_config(page_title="لوحة المعلم | FuturePath AI", page_icon="📊", layout="wide")
inject_global_styles()
page_intro("EDUCATOR CONSOLE", "لوحة المعلم", "نظرة مركزية على نتائج الطلاب لمتابعة التقدم وتقديم إرشاد أكثر دقة.")
conn = sqlite3.connect("students.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
conn.close()
metrics = st.columns(3)
with metrics[0]: st.metric("عدد الطلاب", len(df))
with metrics[1]: st.metric("متوسط المعدل", f"{df['gpa'].mean():.1f}٪" if not df.empty and 'gpa' in df else "—")
with metrics[2]: st.metric("آخر تحديث", "اليوم")
section_title("سجل الطلاب", "يمكن استخدام السجل لمراجعة البيانات والنتائج المحفوظة.")
st.dataframe(df, use_container_width=True, hide_index=True)
