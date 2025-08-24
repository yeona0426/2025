import streamlit as st

# (medicine_data, image_urls 동일)

# ------------------------------
# Streamlit 화면
# ------------------------------
st.set_page_config(page_title="증상별 소화제 추천 앱", layout="wide")

# 전체 배경색 + 버튼 스타일
st.markdown("""
<style>
body {
    background-color: #ECECEC;
}
div.stButton > button:first-child {
    background-color: #F5F0E1;  /* 베이지 강조 */
    color: #333333;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# 앱 제목
st.markdown("""
<h1 style='text-align:center; color:#333333; font-family:Arial Black;'>💊 증상별 소화제 추천 앱</h1>
<p style='text-align:center; color:#555555;'>증상을 클릭하면 알맞은 약을 추천해드립니다.</p>
""", unsafe_allow_html=True)

# ⚠️ 경고 문구
st.markdown("""
<div style='background-color:#BBDCE5; color:#333333; padding:15px; border-radius:10px; text-align:center;'>
⚠️ 주의: 이 앱은 일반적인 정보 제공용입니다. 약 복용 전 반드시 약사 또는 의사와 상담하세요.
</div>
""", unsafe_allow_html=True)

# 이미지 선택
cols = st.columns(5)
selected_symptom = None
for idx, (symptom, url) in enumerate(image_urls.items()):
    with cols[idx]:
        st.image(url, use_container_width=True)
        if st.button(f"{symptom}"):
            selected_symptom = symptom

# 약 추천 (가로 2열)
if selected_symptom:
    st.subheader(f"🩺 선택한 증상: {selected_symptom}")
    st.write("**추천 약품:**")
    cols = st.columns(2)
    for idx, med in enumerate(medicine_data[selected_symptom]):
        with cols[idx]:
            st.markdown(f"""
                <div style="
                    background-color: #BBDCE5;  /* 라이트 블루 카드 */
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 4px 4px 12px #F5F0E1;
                    text-align: center;
                    margin-bottom: 15px;
                    color: #333333;
                ">
                    <h3>{med['이름']}</h3>
                    <p><strong>복용법:</strong> {med['복용법']}</p>
                    <p><strong>효능:</strong> {med['효능']}</p>
                    <p><strong>주의사항:</strong> {med['주의사항']}</p>
                </div>
            """, unsafe_allow_html=True)
