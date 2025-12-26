import streamlit as st
from datetime import datetime

# 1. 頁面設定
st.set_page_config(page_title="健身諮詢", page_icon="💪")
st.title("💪 專業健身諮詢")

# 2. 問卷題目
st.subheader("1. 您滿意自己的身型嗎？")
q1 = st.radio("", ["滿意", "尚可", "不滿意"], horizontal=True)

st.subheader("2. 您有什麼樣的需求？(可複選)")
needs = []
c1, c2 = st.columns(2)
with c1:
    if st.checkbox("減重降脂"): needs.append("減重降脂")
    if st.checkbox("局部雕塑"): needs.append("局部雕塑")
    if st.checkbox("過瘦增重"): needs.append("過瘦增重")
with c2:
    if st.checkbox("肌肉強化"): needs.append("肌肉強化")
    if st.checkbox("全身線條"): needs.append("全身線條")
    if st.checkbox("強化體能"): needs.append("強化體能")

st.subheader("3. 您試過什麼方式？")
methods = []
m1, m2 = st.columns(2)
with m1:
    if st.checkbox("少吃多運動"): methods.append("少吃多運動")
    if st.checkbox("減肥藥"): methods.append("減肥藥")
with m2:
    if st.checkbox("健身房"): methods.append("健身房")
    if st.checkbox("醫美診所"): methods.append("醫美診所")

st.subheader("4. 方便諮詢的時間？")
q4 = st.radio("", ["平日白天", "平日晚上", "假日"], horizontal=True)

# 3. 留資料區
st.divider()
st.subheader("📝 預約參觀")
name = st.text_input("姓名")
phone = st.text_input("手機/Line")

if st.button("🚀 送出資料"):
    if name:
        st.success(f"已記錄！{name}")
        # 顯示結果讓你截圖
        st.info(f"需求: {','.join(needs)}\n時間: {q4}")
    else:
        st.error("請填寫姓名喔！")
