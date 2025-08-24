import streamlit as st

# ------------------------------
# 증상별 추천 약 정보
# ------------------------------
medicine_data = {
    "속쓰림 / 위산 역류": [
        {"이름": "겔포스", "복용법": "식사 후 1~2정", "효능": "위산 중화, 속쓰림 완화", "주의사항": "신장질환 환자는 사용 전 의사 상담"},
        {"이름": "알마겔", "복용법": "식사 후 2~3정", "효능": "위산 중화, 위염 완화", "주의사항": "장기간 사용 시 변비 유발 가능"}
    ],
    "더부룩함 / 소화불량": [
        {"이름": "훼스탈", "복용법": "식사 직후 1~2정", "효능": "소화 효소 보충, 소화불량 완화", "주의사항": "췌장질환 환자는 사용 전 의사 상담"},
        {"이름": "베아제", "복용법": "식사 직후 1~2정", "효능": "소화불량 개선", "주의사항": "특정 음식 알레르기 확인 필요"}
    ],
    "과식 후 체함": [
        {"이름": "활명수", "복용법": "식사 후 10ml", "효능": "소화 촉진, 체한 증상 완화", "주의사항": "카페인 민감자는 주의"},
        {"이름": "훼스탈", "복용법": "식사 직후 1~2정", "효능": "과식 후 소화불량 완화", "주의사항": "췌장질환 환자는 사용 전 의사 상담"}
    ],
    "가스참 / 트림 / 방귀 과다": [
        {"이름": "가스활명수", "복용법": "식사 후 10ml", "효능": "트림, 방귀 과다 완화", "주의사항": "심한 복통 시 사용 금지"},
        {"이름": "차마다이제", "복용법": "식사 직후 1~2정", "효능": "복부 팽만 및 가스 제거", "주의사항": "심한 복통 시 사용 금지"}
    ],
    "메스꺼움 / 구역질": [
        {"이름": "위청수", "복용법": "식사 후 10ml", "효능": "메스꺼움 완화, 소화 촉진", "주의사항": "알코올 섭취 주의"},
        {"이름": "활명수", "복용법": "식사 후 10ml", "효능": "구역질 완화, 소화 촉진", "주의사항": "카페인 민감자 주의"}
    ]
}

# ------------------------------
# 증상별 이미지 (GitHub raw 링크)
# ------------------------------
image_urls = {
    "속쓰림 / 위산 역류": "https://github.com/yeona0426/image/raw/main/acid.PNG",
    "더부룩함 / 소화불량": "https://github.com/yeona0426/image/raw/main/stom.PNG",
    "과식 후 체함": "https://github.com/yeona0426/image/raw/main/eat.PNG",
    "가스참 / 트림 / 방귀 과다": "https://github.com/yeona0426/image/raw/main/gas.PNG",
    "메스꺼움 / 구역질": "https://github.com/yeona0426/image/raw/main/to.PNG"
}

# ------------------------------
# Streamlit 화면
# ------------------------------
st.set_page_config(page_title="증상별 소화제 추천 앱", layout="wide")
st.title("💊 증상별 소화제 추천 앱")

# ⚠️ 경고 문구
st.warning("⚠️ 주의: 이 앱은 일반적인 정보 제공용입니다. \n약 복용 전 반드시 약사 또는 의사와 상담하세요.")

st.write("증상을 클릭하면 알맞은 약을 추천해드립니다.")

# 이미지 5개 한 줄로 배치
cols = st.columns(5)
selected_symptom = None

for idx, (symptom, url) in enumerate(image_urls.items()):
    with cols[idx]:
        st.image(url, use_container_width=True)
        if st.button(f"{symptom}"):
            selected_symptom = symptom

# 선택된 증상에 따른 약 추천 (가로 2열, 베이지 카드)
if selected_symptom:
    st.subheader(f"🩺 선택한 증상: {selected_symptom}")
    st.write("**추천 약품:**")
    
    cols = st.columns(2)
    for idx, med in enumerate(medicine_data[selected_symptom]):
        with cols[idx]:
            st.markdown(f"""
                <div style="
                    background-color: #F5F0E1;  /* 베이지 배경 */
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 4px 4px 12px rgba(0,0,0,0.2);
                    text-align: center;
                    margin-bottom: 15px;
                    color: #333333;  /* 무채색 텍스트 */
                ">
                    <h3>{med['이름']}</h3>
                    <p><strong>복용법:</strong> {med['복용법']}</p>
                    <p><strong>효능:</strong> {med['효능']}</p>
                    <p><strong>주의사항:</strong> {med['주의사항']}</p>
                </div>
            """, unsafe_allow_html=True)
