import streamlit as st
from datetime import datetime

# 1. 頁面設定
st.set_page_config(page_title="專業諮詢問卷", page_icon="📝")
st.title("📝 專業諮詢問卷")

# 2. 問卷題目
# 題目一：興趣項目
st.subheader("1. 您對哪個項目有興趣嗎？(可複選)")
interests = []
int_col1, int_col2 = st.columns(2)
with int_col1:
    if st.checkbox("跳床"): interests.append("跳床")
    if st.checkbox("美容"): interests.append("美容")
with int_col2:
    if st.checkbox("越式洗頭"): interests.append("越式洗頭")
    if st.checkbox("AI手搖飲"): interests.append("AI手搖飲")

# 題目二：身型滿意度
st.subheader("2. 您滿意自己的身型嗎？")
q_satisfaction = st.radio("身型滿意度", ["滿意", "尚可", "不滿意"], horizontal=True, label_visibility="collapsed")

# 題目三：需求
st.subheader("3. 您有什麼樣的需求嗎？(可複選)")
needs = []
need_col1, need_col2 = st.columns(2)
with need_col1:
    if st.checkbox("我想減重"): needs.append("我想減重")
    if st.checkbox("我想雕塑"): needs.append("我想雕塑")
with need_col2:
    if st.checkbox("我想增重"): needs.append("我想增重")

# 題目四：試過的方式
st.subheader("4. 您試過什麼方式調整體態？(可複選)")
methods = []
m_col1, m_col2 = st.columns(2)
with m_col1:
    if st.checkbox("少吃多動"): methods.append("少吃多動")
    if st.checkbox("減肥藥"): methods.append("減肥藥")
    if st.checkbox("中醫調理"): methods.append("中醫調理")
    if st.checkbox("保健食品"): methods.append("保健食品")
with m_col2:
    if st.checkbox("健身房"): methods.append("健身房")
    if st.checkbox("醫美診所"): methods.append("醫美診所")
    if st.checkbox("其他"): methods.append("其他")

# 題目五：決心評分
st.subheader("5. 改變體態的決心 (1-10分)")
determination = st.select_slider("分數越高決心越強", options=list(range(1, 11)), value=5)

# 3. 留資訊區
st.divider()
st.subheader("👤 聯絡資訊")
name = st.text_input("姓名：")
age = st.text_input("年齡：")
phone = st.text_input("電話：")

# 4. 送出與複製功能
if st.button("🚀 提交問卷並產生紀錄"):
    if name and phone:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # 整理文字
        copy_text = f"""【問卷紀錄】
時間：{timestamp}
👤 姓名：{name}
🎂 年齡：{age}
📱 電話：{phone}
----------------------
✨ 興趣項目：{", ".join(interests) if interests else "未勾選"}
💪 身型滿意度：{q_satisfaction}
🎯 目標需求：{", ".join(needs) if needs else "未勾選"}
📝 嘗試方式：{", ".join(methods) if methods else "未勾選"}
🔥 改變決心：{determination} 分
----------------------
感謝您幫我們做這個問卷。
感謝您有機會幫我們做量測，可以獲得機票抽獎機會價值$6000！"""
        
        st.success("✅ 已生成！長按下方框內文字即可「全選複製」：")
        st.text_area("複製區", value=copy_text, height=300)
        
        st.info("💡 感謝你幫我們做這個問卷，感謝您有機會幫我們做量測，可以獲得機票抽獎機會價值$6000！")
    else:
        st.error("請填寫姓名與電話喔！")
