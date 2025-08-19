import streamlit as st

# 페이지 기본 세팅
st.set_page_config(page_title="MBTI 진로 추천 💡", page_icon="🎯", layout="centered")

# 🌈 CSS로 배경과 폰트 꾸미기
page_bg = """
<style>
/* 전체 배경 - 그라디언트 */
.stApp {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7, #a1c4fd, #c2e9fb);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: #222;
    font-family: "Comic Sans MS", cursive, sans-serif;
}

/* 그라디언트 움직이는 효과 */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 제목 꾸미기 */
h1 {
    text-align: center;
    font-size: 3em;
    color: #fff;
    text-shadow: 2px 2px 5px #ff6f61;
}

/* 직업 리스트 */
ul {
    background: rgba(255,255,255,0.7);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["🧪 과학자 – 분석력 최고!", "♟️ 전략가 – 큰 그림 설계자!", "📊 데이터 분석가 – 숫자의 마법사!"],
    "ENTP": ["🚀 기업가 – 세상을 바꾸는 혁신가!", "📢 광고기획자 – 아이디어 뱅크!", "💡 기술 혁신가 – 미래 창조자!"],
    "INFJ": ["🪄 상담사 – 마음을 치유하는 힐러!", "✍️ 작가 – 글로 세상을 바꾸는 예술가!", "📖 교사 – 가르침의 빛!"],
    "ENFP": ["🎤 마케터 – 사람을 끌어당기는 매력!", "🗂️ 기획자 – 창의력 폭발!", "🎬 크리에이터 – 무대 위 주인공!"],
    "ISTJ": ["📑 회계사 – 꼼꼼함의 대명사!", "🏛️ 행정가 – 질서의 관리자!", "🪖 군인 – 책임감의 상징!"],
    "ESTJ": ["📈 경영자 – 리더십 만렙!", "🛠️ 프로젝트 매니저 – 실행력 갑!", "📋 공무원 – 국가의 버팀목!"],
    "ISFJ": ["💉 간호사 – 따뜻한 헌신!", "🍎 교사 – 학생들의 멘토!", "🤝 사회복지사 – 나눔의 전문가!"],
    "ESFJ": ["👥 HR 전문가 – 사람을 연결하는 다리!", "🩺 간호사 – 공감의 치유자!", "🎯 서비스 기획자 – 만족의 디자이너!"],
    "ISTP": ["⚙️ 엔지니어 – 기술의 장인!", "✈️ 파일럿 – 하늘의 지휘자!", "⛑️ 응급구조사 – 위기의 해결사!"],
    "ESTP": ["💼 세일즈 전문가 – 말의 마술사!", "🏅 스포츠 코치 – 팀의 에너지!", "📊 기업가 – 도전 정신의 끝판왕!"],
    "ISFP": ["🎨 디자이너 – 감각의 천재!", "🎻 예술가 – 감성의 전달자!", "🎶 작곡가 – 음악의 창조자!"],
    "ESFP": ["🎭 배우 – 무대 위의 별!", "🎤 가수 – 열정의 아이콘!", "🎉 이벤트 기획자 – 행복을 만드는 사람!"],
    "INTP": ["🔬 연구원 – 호기심의 화신!", "💻 프로그래머 – 코딩 마스터!", "⚡ 발명가 – 새로운 세상 창조자!"],
    "ENTJ": ["👑 CEO – 카리스마 리더!", "⚖️ 변호사 – 정의의 수호자!", "📊 컨설턴트 – 전략적 해결사!"],
    "INFP": ["💭 심리상담사 – 따뜻한 위로!", "📚 작가 – 마음을 울리는 문장!", "🌍 사회운동가 – 세상을 바꾸는 힘!"],
    "ENFJ": ["🍎 교사 – 영감을 주는 멘토!", "🎯 코치 – 가능성을 키우는 리더!", "📢 강사 – 열정의 전달자!"],
}

# 타이틀
st.markdown("<h1>🌟 MBTI 기반 진로 추천 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:20px;'>당신의 MBTI를 선택하면 ✨ 찰떡같이 맞는 직업을 추천해드립니다! 🚀</p>", unsafe_allow_html=True)

# MBTI 선택
mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(mbti_jobs.keys()))

# 결과 출력
if mbti:
    st.markdown(f"## 🎉 {mbti} 유형에 어울리는 직업")
    st.markdown("<ul>", unsafe_allow_html=True)
    for job in mbti_jobs[mbti]:
        st.markdown(f"<li>{job}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.success("🌈 새로운 가능성을 탐험해 보세요! 🚀💡✨")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center;'>💖 만든이: 동신동덕 팀 💖</p>", unsafe_allow_html=True)
