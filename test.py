import streamlit as st

# 증상-약 데이터
medicine_data = {
    "속쓰림 / 위산 역류": {
        "성분": "제산제 (알마게이트, 수산화마그네슘, 알루미늄 수산화물 등)",
        "추천 약": ["겔포스", "알마겔"]
    },
    "더부룩함 / 소화불량": {
        "성분": "소화효소제 (판크레아틴, 디아스타제 등)",
        "추천 약": ["훼스탈", "베나치오", "베아제"]
    },
    "과식 후 체함": {
        "성분": "소화효소제 + 생약제",
        "추천 약": ["베아제", "평위산(생약제)", "활명수"]
    },
    "가스참 / 트림 / 방귀 과다": {
        "성분": "소포제 (시메티콘 성분)",
        "추천 약": ["이지엔6 가스정", "가스활명수"]
    },
    "메스꺼움 / 구역질": {
        "성분": "생약성 건위제",
        "추천 약": ["위청수", "활명수"]
    }
}

# 실제 이미지 URL
image_urls = {
    "속쓰림 / 위산 역류": "https://cdn-icons-png.flaticon.com/512/1143/11430828.png",
    "더부룩함 / 소화불량": "https://cdn-icons-png.flaticon.com/512/1143/11430843.png",
    "과식 후 체함": "https://cdn-icons-png.flaticon.com/512/995/9958185.png",
    "가스참 / 트림 / 방귀 과다": "https://cdn-icons-png.flaticon.com/512/993/9930189.png",
    "메스꺼움 / 구역질": "https://cdn-icons-png.flaticon.com/512/1003/10039255.png"
}

st.title("💊 증상별 소화제 추천 앱")
st.write("아래 이미지 중 하나를 클릭하면 알맞은 약을 추천해드립니다.")

# 한 줄에 이미지 5개 배치
cols = st.columns(5)
selected_symptom = None

for idx, (symptom, url) in enumerate(image_urls.items()):
    with cols[idx]:
        st.image(url, caption=symptom, use_container_width=True)
        if st.button(f"{symptom} 선택"):
            selected_symptom = symptom

# 선택된 증상에 따른 약 추천
if selected_symptom:
    st.subheader(f"🩺 선택한 증상: {selected_symptom}")
    st.write(f"**추천 성분**: {medicine_data[selected_symptom]['성분']}")
    st.write("**추천 약품**:")
    for med in medicine_data[selected_symptom]['추천 약']:
        st.markdown(f"- {med}")
