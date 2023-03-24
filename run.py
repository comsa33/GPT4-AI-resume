import sys

import streamlit as st
import openai
import pandas as pd

import core.functions as funcs
from data import settings



st.set_page_config(
    page_title="AI 자소서",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto",
)

st.session_state.table_names = funcs.table_names
st.session_state.models = ["gpt-3.5-turbo", "gpt-4"]

st.title('GPT-4 API-base Resume & Self-introduction Creation Service')

with st.sidebar:
    st.markdown("===[GPT 모델설정]===")
    st.markdown("[나의 OpenAI API keys 확인](https://platform.openai.com/account/api-keys)")
    st.text_input(
        "OpenAI API Keys 입력 👇",
        "",
        key="API_KEY"
    )
    st.selectbox(
        "GPT Model 선택 👇",
        st.session_state.models,
        key="model_name"
    )
    st.slider(
        '창작성 수치를 조절하세요.(1에 가까울 수록 창작성이 높습니다.)',
        0.0, 1.0, 0.7,
        key="temperature"
    )
    st.markdown("===[채용공고 설정]===")
    st.selectbox(
        "채용공고 사이트 선택 👇",
        st.session_state.table_names,
        key="table_name"
    )

if st.session_state.API_KEY:
    openai.api_key = st.session_state.API_KEY

df = funcs.get_data(st.session_state.table_name)
skills = list(set(map(lambda x: x.lower(), sum(df['skill_tags'].tolist(), []))))

st.info('원하는 직무를 검색하고 자소서를 작성할 채용공고를 선택하세요', icon="ℹ️")
with st.expander('펼쳐보기'):
    col1, _, col2 = st.columns([8, 1, 14])
    with col1:
        st.text_input(
            "원하는 직무를 검색하세요 👇",
            "데이터 엔지니어",
            key="search_term"
        )
        st.markdown(f"**채용공고 검색결과**")
        temp_df = df[df['position'].str.contains(st.session_state.search_term)][['company_name', "position"]]
        st.dataframe(temp_df)
        st.selectbox(
                "채용공고 인덱스를 선택하세요 👇",
                temp_df.index.tolist(),
                key="jp_index"
            )

    with col2:
        if st.session_state.jp_index:
            posting = df.iloc[int(st.session_state.jp_index)]

            company_name = posting['company_name']
            position = posting['position']
            requirements = posting['requirements']
            main_tasks = posting['main_tasks']
            intro = posting['intro']

            st.markdown('**채용공고 상세정보** (필드를 더블클릭하면 세부내용을 확인할 수 있습니다.)')
            st.checkbox("표 넓게보기", value=False, key="use_container_width")
            st.dataframe(posting, use_container_width=st.session_state.use_container_width)

st.info('지원자 정보를 자신의 정보에 맞게 수정하세요', icon="ℹ️")
with st.expander('펼쳐보기'):
    st.markdown('(테이블의 셀을 더블클릭하면 정보를 수정할 수 있습니다.)')
    col_user1, _, col_user2, _, col_user3 = st.columns([10, 1, 12, 1, 14])
    with col_user1:
        st.markdown('**지원자 기본정보**')
        info_df = pd.DataFrame(settings.user_info)
        edited_info_df = st.experimental_data_editor(info_df)
    with col_user2:
        st.markdown('**지원자 학력정보**')
        edu_df = pd.DataFrame(settings.educations)
        edited_edu_df = st.experimental_data_editor(edu_df, num_rows="dynamic")
    with col_user3:
        st.markdown('**지원자 경력정보**')
        career_df = pd.DataFrame(settings.career_history)
        edited_career_df = st.experimental_data_editor(career_df, num_rows="dynamic")
    col_user4, _, col_user5 = st.columns([8, 1, 10])
    with col_user4:
        my_skills = st.multiselect(
            '지원자 스킬정보', skills, settings.user_skills)
    with col_user5:
        my_achievements = st.text_area('지원자 경력기술서 및 성과에 대해서 입력하세요', settings.career_achievements)

st.info('AI에게 가이드를 받아보세요', icon="ℹ️")
col_ai1, _, col_ai2, _, col_ai3 = st.columns([20, 1, 10, 1, 10])
with col_ai1:
    st.text_input(
        'AI가 작성할 글의 주제를 직접입력하세요 👇',
        '본인이 지금까지 살아오면서 가장 성취감을 느꼈던 경험(또는 성과)를 구체적으로 기술해 주시기 바랍니다.',
        key='writing_type1'
        )
with col_ai2:
    st.session_state.radio_disabled = True
    if not st.session_state.writing_type1:
        st.session_state.radio_disabled = False
    st.radio(
        "AI가 작성할 글을 선택하세요 👇 (활성화를 하려면 위 주제를 입력하는 박스의 글을 지우세요.)",
        ('자기소개', '지원동기', '나의 장단점'),
        key="writing_type2",
        disabled=st.session_state.radio_disabled
        )
    if not st.session_state.writing_type1:
        subject = st.session_state.writing_type2
    else:
        subject = st.session_state.writing_type1
with col_ai3:
    min_letter, max_letter = st.slider(
        '최소, 최대 글자수를 선택하세요 👇',
        100, 1000, (400, 600))

jp_desc = f"""
- 회사이름: {company_name}
- 채용직무: {position}
- 직무기술: {requirements}
- 맡게 될 업무: {main_tasks}
- 회사에 대한 간단한 소개 및 정보: {intro}"""
user_desc = f"""
- 나의 개인 정보: {edited_info_df.to_dict()}
- 나의 성향: {edited_info_df.to_dict()['mbti'][0]}
- 내 학력: {edited_edu_df.to_dict()}
- 내 보유 스킬: {my_skills}
- 내 경력 정보: {edited_career_df.to_dict()}
- 내 경력기술서 및 성과: {my_achievements}"""
prompt_msg = f"""회사에 이력서와 함께 제출할 {subject}에 대한 글을 작성하세요.
{min_letter}~{max_letter} 글자 사이로 작성하세요.
{settings.prompt_default}"""

_, col_center, _ = st.columns([1, 6, 1])
if st.button('글 생성하기'):
    with col_center:
        try:
            response = openai.ChatCompletion.create(
                model=st.session_state.model_name,
                temperature=st.session_state.temperature,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"나는 회사에 지원하는데 너의 도움이 필요해. 회사의 채용정보는 다음과 같아. {jp_desc}"},
                    {"role": "assistant", "content": "네, 알겠습니다."},
                    {"role": "user", "content": f"나는 다음과 같은 이력을 가지고 있어. {user_desc}"},
                    {"role": "assistant", "content": "네, 알겠습니다."},
                    {"role": "user", "content": f"{prompt_msg}"}
                ],
                stream=True,
            )
            st.markdown(f"### AI 추천 {subject}")
            placeholder = st.empty()
            typed_text = ''
            for chunk in response:
                if chunk['choices'][0]['delta'].get('content'):
                    typed_text += chunk['choices'][0]['delta'].get('content')
                    with placeholder.container():
                        st.write(typed_text)
            st.download_button(f'AI_{subject} 다운로드', typed_text)
        except Exception as e:
            st.write(e)
