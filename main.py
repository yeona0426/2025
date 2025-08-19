import streamlit as st

# 페이지 기본 세팅
st.set_page_config(page_title="MBTI 진로 추천 💡", page_icon="🎯", layout="centered")

# MBTI별 추천 직업 데이터 (설명 추가)
mbti_jobs = {
    "INTJ": ["🧪 과학자", "♟️ 전략가", "📊 데이터 분석가"],
    "ENTP": ["🚀 기업가", "📢 광고기획자", "💡 기술 혁신가"],
    "INFJ": ["🪄 상담사", "✍️ 작가", "📖 교사"],
    "ENFP": ["🎤 마케터", "🗂️ 기획자", "🎬 크리에이터"],
    "ISTJ": ["📑 회계사", "🏛️ 행정가", "🪖 군인"],
    "ESTJ": ["📈 경영자", "🛠️ 프로젝트 매니저", "📋 공무원"],
    "ISFJ": ["💉 간호사", "🍎 교사", "🤝 사회복지사"],
    "ESFJ": ["👥 HR 전문가", "🩺 간호사", "🎯 서비스 기획자"],
    "ISTP": ["⚙️ 엔지니어", "✈️ 파일럿", "⛑️ 응급구조사"],
    "ESTP": ["💼 세일즈 전문가", "🏅 스포츠 코치", "📊 기업가"],
    "ISFP": ["🎨 디자이너", "🎻 예술가", "🎶 작곡가"],
    "ESFP": ["🎭 배우", "🎤 가수", "🎉 이벤트 기획자"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "⚡ 발명가"],
    "ENTJ": ["👑 CEO", "⚖️ 변호사", "📊 컨설턴트"],
    "INFP": ["💭 심리상담사", "📚 작가", "🌍 사회운동가"],
    "ENFJ": ["🍎 교사", "🎯 코치", "📢 리더십 강사"],
}

# 타이틀
st.markdown(
    """
    <div style="text-align: center;">
        <h1>🌟 MBTI 기반 진로 추천 🌟</h1>
        <p style="font-size:18px;">당신의 <b>MBTI</b>를 선택하면,<br>✨ 딱 맞는 직업을 추천해드립니다! ✨</p>
    </div>
    """, unsafe_allow_html=True
)

# MBTI 선택
mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(mbti_jobs.keys()))

# 결과 출력
if mbti:
    st.markdown(f"## 🎉 {mbti} 유형에 어울리는 직업은?")
    st.markdown("✨ 아래의 직업들이 당신에게 잘 맞을 거예요! ✨")
    for job in mbti_jobs[mbti]:
        st.markdown(f"- {job}")

    st.success("🌈 새로운 가능성을 탐험해 보세요! 🚀💡")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>💖 만든이: 동신동덕 팀 💖</p>", unsafe_allow_html=True)
