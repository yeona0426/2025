import streamlit as st

# ------------------------------
# 페이지 기본 설정
# ------------------------------
st.set_page_config(page_title="💊 소화제 추천 앱", layout="wide")

# ------------------------------
# CSS 스타일 (배경/카드 꾸미기)
# ------------------------------
page_style = """
<style>
/* 전체 배경 */
.stApp {
    background-color: #FAF3E0; /* 베이지 톤 */
}

/* 카드 스타일 */
.card {
    background-color: #D6EAF8; /* 파스텔 블루 */
    padding: 20px;
    border-radius: 16px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin: 10px;
}
.card h3 {
    margin-top: 0;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# ------------------------------
# 데이터
# ------------------------------
medicine_data = {
    "속쓰림 / 위산 역류": [
        {"이름": "겔포스", "설명": "위산 과다 및 속쓰림 완화. 알루미늄/마그네슘 성분의 제산제."},
        {"이름": "오메프라졸", "설명": "위산 분비 억제제. 위식도 역류질환에 사용."}
    ],
    "더부룩함 / 소화불량": [
        {"이름": "차마다이제", "설명": "소화 효소 + 생약 성분. 소화불량, 식후 더부룩함 완화."},
        {"이름": "훼스탈", "설명": "지방, 탄수화물 분해효소 포함. 과식/기름진 음식 소화에 도움."}
    ],
    "과식 후 체함": [
        {"이름": "차마다이제", "설명": "체한 느낌, 소화 촉진에 도움."},
        {"이름": "훼스탈", "설명": "과식으로 인한 소화불량 완화."}
    ],
    "가스참 / 트림 / 방귀 과다": [
        {"이름": "가스칼", "설명": "위장 내 가스 제거, 더부룩함 개선."},
        {"이름": "베나치오", "설명": "가스팽만, 복부 불쾌감 완화."}
    ],
    "메스꺼움 / 구역질": [
        {"이름": "베나치오", "설명": "소화불량 동반 구역, 오심 완화."},
        {"이름": "겔포스", "설명": "위산 과다로 인한 메스꺼움 완화."}
    ]
}

# ------------------------------
# 앱 제목
# ------------------------------
st.markdown("<h1 style='text-align: center; color: #333;'>💊 소화제 추천 앱</h1>", unsafe_allow_html=True)

# ------------------------------
# 선택
# ------------------------------
symptom = st.selectbox("증상을 선택하세요 👇", list(medicine_data.keys()))

# ------------------------------
# 결과 출력 (카드 형태, 가로 정렬)
# ------------------------------
st.subheader(f"👉 '{symptom}' 증상에 추천되는 약")
cols = st.columns(2)

for idx, med in enumerate(medicine_data[symptom]):
    with cols[idx]:
        st.markdown(f"""
        <div class="card">
            <h3>{med['이름']} 💊</h3>
            <p>{med['설명']}</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------
# 경고 문구
# ------------------------------
st.markdown("""
⚠️ **주의:** 이 앱은 일반적인 정보 제공용입니다.  
약 복용 전 반드시 약사 또는 의사와 상담하세요.  
""")

# ------------------------------
# 💊 알약 떨어지는 효과 버튼
# ------------------------------
if st.button("💊 알약 떨어뜨리기!"):
    pill_rain = """
    <style>
    @keyframes pillFall {
        0% { transform: translateY(-10vh); opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    .pill {
        position: fixed;
        top: 0;
        font-size: 30px;
        animation: pillFall 3s linear infinite;
    }
    </style>
    <div class="pill" style="left:10%;">💊</div>
    <div class="pill" style="left:30%;">💊</div>
    <div class="pill" style="left:50%;">💊</div>
    <div class="pill" style="left:70%;">💊</div>
    <div class="pill" style="left:90%;">💊</div>
    """
    st.markdown(pill_rain, unsafe_allow_html=True)
