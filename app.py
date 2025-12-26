import streamlit as st
from datetime import datetime

# 1. 頁面設定
st.set_page_config(page_title="健身諮詢", page_icon="💪")
st.title("💪 專業健身諮詢")

# 2. 問卷題目
st.subheader("1. 您滿意自己的身型嗎？")
q1 = st.radio("滿意度", ["滿意", "尚可", "不滿意"], horizontal=True, label_visibility="collapsed")

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
with m3:
if st.checkbox("中藥調理"): methods.append("中藥調理")
    if st.checkbox("保健食品"): methods.append("保健食品")


st.subheader("4. 方便諮詢的時間？")
q4 = st.radio("方便時間", ["平日白天", "平日晚上", "假日"], horizontal=True, label_visibility="collapsed")

# 3. 留資料區
st.divider()
st.subheader("📝 預約參觀")
name = st.text_input("姓名")
phone = st.text_input("手機/Line")

# 4. 送出與複製功能
if st.button("🚀 送出並產生紀錄"):
    if name:
        # 整理資料格式
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        needs_str = ", ".join(needs) if needs else "無"
        methods_str = ", ".join(methods) if methods else "無"
        
        # 這段文字就是讓你複製的內容
        copy_text = f"""【新潛在客戶】
📅 時間：{timestamp}
👤 姓名：{name}
📱 電話：{phone}
💪 滿意度：{q1}
🎯 需求：{needs_str}
📝 試過：{methods_str}
⏰ 方便時間：{q4}"""
        
        st.success("✅ 資料已生成！請點擊下方框框右上角的「複製圖示」")
        
        # 顯示可複製的區塊
        st.code(copy_text, language=None)
        
    else:
        st.error("請填寫姓名喔！")
