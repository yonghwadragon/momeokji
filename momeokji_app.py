# momeokji_app.py
import streamlit as st
import google.generativeai as genai
import re
import urllib.parse

from tools import find_recipe_with_ingredients

# 1) API Key 로딩
if "api_key" not in st.session_state:
    try:
        st.session_state.api_key = st.secrets["general"]["GOOGLE_API_KEY"]
    except:
        st.session_state.api_key = ""  # 키를 못 불러올 경우 ""

# 2) Streamlit 기본 UI
st.title("🍽️ 뭐 먹지?")
st.caption("냉장고 속 재료로 만들 요리를 추천해 드리는 AI 요리사")

st.write("예: `김치, 양파, 달걀` 등 쉼표로 구분해 입력하세요.")

# 채팅 기록 초기화 (원한다면 유지 가능)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3) 메시지 표시 (Optional)
for msg in st.session_state.messages:
    if parts := msg.parts:
        with st.chat_message("human" if msg.role == "user" else "ai"):
            for p in parts:
                st.write(p.text)

# 4) 사용자 입력
user_input = st.chat_input("재료나 궁금한 점을 입력해주세요!")
if user_input:
    with st.chat_message("human", avatar="🙂"):
        st.write(user_input)

    # (A) 요리와 무관한 대화는 AI로 간단 응답
    cooking_keywords = ["재료","요리","레시피","김","국","찌개","볶음","구이","감자","양파","대파",","]
    is_cooking_related = any(kw in user_input.lower() for kw in cooking_keywords)

    if not is_cooking_related:
        if st.session_state.api_key:
            # 키가 있으면 LLM으로 자연스럽게 반응
            genai.configure(api_key=st.session_state.api_key)
            model = genai.GenerativeModel("gemini-2.0-flash")  # or gemini-1.5-pro-latest
            response = model.generate_content(f"""
당신은 요리사 AI입니다.
사용자가 '{user_input}' 이라고 했어요.
1) 1~2문장으로 가볍게 인사/답변
2) 요리에 대해 궁금한 점을 다시 물어보도록 유도
한국어로 답변 부탁.
""")
            with st.chat_message("ai", avatar="👩‍🍳"):
                st.write(response.text)
        else:
            # 키가 없으면 고정 답변
            with st.chat_message("ai", avatar="👩‍🍳"):
                st.write("안녕하세요! 저는 요리사 AI입니다. 요리에 대해 물어봐주시면 더 도와드릴 수 있어요.")
        st.session_state.messages = []
        st.stop()

    # (B) 요리 관련 입력 -> 재료 파싱
    ingredients = [x.strip() for x in user_input.split(",") if x.strip()]
    recommended = find_recipe_with_ingredients(ingredients)

    if "적합한 요리를 찾을 수 없습니다." in recommended:
        with st.chat_message("ai", avatar="👩‍🍳"):
            st.write(recommended)
        st.session_state.messages = []
        st.stop()

    # 5) 요리명 & 재료 추출
    match = re.search(r"'([^']+)'\s+추천할게요", recommended)
    dish_name = match.group(1) if match else "요리"
    dish_encoded = urllib.parse.quote(dish_name, encoding='utf-8')

    youtube_search_link = f"https://www.youtube.com/results?search_query={dish_encoded}"
    mangae_link = "https://www.youtube.com/@%EB%A7%8C%EA%B0%9C%EC%9D%98%EB%A0%88%EC%8B%9C%ED%94%BC"

    # 6) 3단계 요리법 + 유튜브 링크
    recipe_prompt = f"""
{recommended}

아래 요구사항을 반드시 지켜 답변해줘:
1) 위 요리를 3단계로 간단히 만드는 방법 소개(단계별 1~2문장)
2) 마지막 줄에 두 링크 추가:
   - 만개의레시피 채널: {mangae_link}
   - 유튜브 검색: {youtube_search_link}
3) 한국어로 답변
"""

    # 7) AI 호출
    if st.session_state.api_key:
        genai.configure(api_key=st.session_state.api_key)
        # 최신 구버전 방식: GenerativeModel(...)
        model = genai.GenerativeModel("gemini-2.0-flash")  # or "gemini-1.5-pro-latest"
        response = model.generate_content(recipe_prompt)

        with st.chat_message("ai", avatar="👩‍🍳"):
            st.write(recommended)    # 먼저 요리명+재료
            st.write(response.text)  # 이어서 AI답변(3단계+링크)
    else:
        # 키가 없으면 조리법 없이 레시피만 표시
        with st.chat_message("ai", avatar="👩‍🍳"):
            st.write(recommended)

    # 8) 매번 대화 초기화
    st.session_state.messages = []