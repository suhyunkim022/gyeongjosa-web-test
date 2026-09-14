import streamlit as st


st.set_page_config(
    page_title="경조사 메일 만들기",
    page_icon="✉️",
    layout="centered",
)

st.title("경조사 메일 만들기")
st.caption("현재 단계에서는 화면과 입력 기능만 테스트합니다. 메일은 발송하지 않습니다.")

inout = st.radio(
    "1. 내부/외부 선택",
    ["외부", "내부"],
    horizontal=True,
)

category = st.radio(
    "2. 경조사 유형",
    ["부고", "결혼"],
    horizontal=True,
)

st.divider()

title = st.text_input("메일 제목", placeholder="예: 홍길동 부친상 안내")
intro = st.text_input("본문 안내 문구", placeholder="예: 아래와 같이 알려드립니다.")

if category == "부고":
    fields = [
        "별세",
        "빈소",
        "입관",
        "발인",
        "장지",
        "연락처",
        "마음 전하는 곳",
    ]
else:
    fields = [
        "일시",
        "장소",
        "연락처",
        "마음 전하실 곳",
        "모바일 청첩장",
    ]

values = {}
st.subheader("경조사 내용")
for field in fields:
    values[field] = st.text_area(field, height=70)

extra = st.text_area("기타 유의사항", height=100, placeholder="한 줄에 한 가지씩 입력하세요.")

law = st.radio(
    "청탁금지법 해당 여부",
    ["해당없음", "해당됨"],
    horizontal=True,
)

if st.button("입력 내용 확인하기", type="primary", use_container_width=True):
    if not title.strip():
        st.warning("메일 제목을 먼저 입력해주세요.")
    else:
        st.success("화면 테스트가 끝났습니다. 아직 실제 메일은 보내지 않습니다.")
        st.subheader("입력한 내용")
        st.write(f"**내부/외부:** {inout}")
        st.write(f"**경조사 유형:** {category}")
        st.write(f"**메일 제목:** {title}")
        if intro.strip():
            st.write(f"**본문 안내 문구:** {intro}")

        for field, value in values.items():
            if value.strip():
                st.write(f"**{field}:** {value}")

        if extra.strip():
            st.write(f"**기타 유의사항:** {extra}")
        st.write(f"**청탁금지법:** {law}")
