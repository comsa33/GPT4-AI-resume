import re

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
st.session_state.models = ["gpt-4", "gpt-3.5-turbo"]

st.title('GPT-4 채용공고별 자소서 가이드')
st.caption('본 테스트 서비스는 사용자 분들의 개인정보를 절대 수집하지 않습니다. 소스코드는 깃허브에 공개되어 있습니다.')

with st.sidebar:
    st.markdown("[**GPT 모델설정**]")
    # st.markdown("[나의 OpenAI API keys 확인](https://platform.openai.com/account/api-keys)")
    # st.text_input(
    #     "OpenAI API Keys 입력(필수) 👇",
    #     "",
    #     key="API_KEY"
    # )
    st.selectbox(
        "🤖 GPT Model 선택",
        st.session_state.models,
        key="model_name"
    )
    st.slider(
        '✒️ 창작성 수치 조절',
        0.0, 1.0, 0.7,
        help="1에 가까울 수록 창작성이 높습니다.",
        key="temperature"
    )
    st.caption("-------------------------")
    st.markdown("[**채용공고 설정**]")
    st.selectbox(
        "🔭 채용공고 사이트 선택",
        st.session_state.table_names,
        key="table_name"
    )
    st.caption(
    """


-------------------------
- 개발자: 이루오
- 이메일: comsa33@kakao.com
- 깃허브: https://github.com/comsa33/GPT4-AI-resume
    """
    )

# if st.session_state.API_KEY:
    # openai.api_key = st.session_state.API_KEY
openai.api_key = settings.my_secret

df = funcs.get_data(st.session_state.table_name)

pattern = r"([^\[\]\(\)]+)(?:\[[^\[\]]*\])?(?:\([^\(\)]*\))?"
skills = list(set(map(lambda x: x.lower(), sum(df['skill_tags'].tolist(), []))))

with st.expander('📜 원하는 직무를 검색하고 자소서를 작성할 채용공고를 선택하세요'):
    col1, _, col2 = st.columns([8, 1, 10])
    with col1:
        st.subheader("**채용공고 검색**")
        col1_sub1, col1_sub2 = st.columns(2)
        with col1_sub1:
            st.text_input(
                "💼 직무 검색",
                help=":grey_question: 지원하고 싶은 직무를 입력하세요.",
                key="position"
            )

        if st.session_state.position != "선택 없음":
            temp_df = df[df['position'].str.contains(st.session_state.position, case=False)][['company_name', "position"]]
            st.session_state.comp_names = ['선택 없음']+list(set(map(
                lambda x: re.search(pattern, x).group(1).strip().lower(),
                temp_df['company_name'].unique().tolist()
                )))
        else:
            temp_df = df[['company_name', "position"]]
            st.session_state.comp_names = ['선택 없음']+list(set(map(
                lambda x: re.search(pattern, x).group(1).strip().lower(),
                df['company_name'].unique().tolist()
                )))

        with col1_sub2:
            st.selectbox(
                "🏢 회사 검색",
                st.session_state.comp_names,
                help=":grey_question: 지원하고 싶은 회사명을 직접 선택하거나, 부분을 입력하면 자동완성 됩니다.",
                key="comp_name"
            )

        if st.session_state.comp_name != "선택 없음":
            temp_df = temp_df[temp_df['company_name'].str.contains(st.session_state.comp_name, case=False)]

        st.caption("-------------------------")
        st.caption('※ 지원하고자 하는 채용공고를 ✅ 선택하세요.')
        temp_df['선택'] = [False]*len(temp_df)
        temp_df = temp_df[['선택', 'company_name', 'position']]
        edited_temp_df = st.experimental_data_editor(temp_df, use_container_width=True)
        # get index no of row whose '선택' column is True
        try:
            st.session_state.jp_index = edited_temp_df[edited_temp_df['선택']==True].index.tolist()[0]
        except IndexError:
            pass

    with col2:
        st.subheader('**채용공고 상세정보**')
        st.caption("-------------------------")
        try:
            posting = df.iloc[int(st.session_state.jp_index)]
            posting_url = settings.wanted_url_prefix+str(posting['id'])
            company_name = posting['company_name']
            position = posting['position']
            requirements = posting['requirements'].replace("•", "  \n-")
            main_tasks = posting['main_tasks'].replace("•", "  \n-")
            intro = posting['intro'].replace("•", "  \n-")
            benefits = posting['benefits'].replace("•", "  \n-")
            preferred = posting['preferred_points'].replace("•", "  \n-")
            deadline = posting['due_time'] if posting['due_time'] else "상시 채용"
            required_skills = ", ".join(posting["skill_tags"]) if posting["skill_tags"] else "제공된 정보 없음"

            with st.container():
                st.markdown(f'[채용 기업] **{company_name}**')
                st.markdown(f'[채용 직무] **{position}**')
                st.caption(intro)
                st.caption(f'[지원 마감일] **{deadline}**')
                tab1, tab2, tab3, tab4 = st.tabs(["주요업무", "자격요건", "우대사항", "복리후생"])
                with tab1:
                    st.caption(f'{main_tasks}')
                    st.caption(f'[필요한 기술]  \n**{required_skills}**')
                with tab2:
                    st.caption(f'{requirements}')
                with tab3:
                    st.caption(f'{preferred}')
                with tab4:
                    st.caption(f'{benefits}')

            application_string = f'<div align="right">&#x27A1; <a href="{posting_url}">지원하기 {st.session_state.table_name} 채용공고 링크</a> </div>'
            st.markdown(application_string, unsafe_allow_html=True)

            # st.dataframe(posting, use_container_width=True)
        except TypeError and AttributeError:
            st.caption("⚠️ 채용공고가 선택되지 않았거나, 선택하신 직무명이나 회사명으로 검색된 채용공고가 없습니다.")


st.caption("-------------------------")
with st.expander('ℹ️ 지원자 정보를 자신의 정보에 맞게 수정하세요'):
    st.caption(':arrow_down: 테이블의 셀을 더블클릭하면 정보를 수정할 수 있습니다.')
    st.markdown('👤 **지원자 기본정보**')
    info_df = pd.DataFrame(settings.user_info)
    edited_info_df = st.experimental_data_editor(info_df, use_container_width=True)

    st.caption("-------------------------")
    st.markdown('🏫 **지원자 학력정보**')
    edu_df = pd.DataFrame(settings.educations)
    edited_edu_df = st.experimental_data_editor(edu_df, num_rows="dynamic", use_container_width=True)

    st.caption("-------------------------")
    my_skills = st.multiselect(
        '⚙️ 지원자 스킬정보를 검색/입력하세요',
        skills,
        settings.user_skills,
        help=":grey_question: 입력시 선택 박스에서 선택하세요."
        )

    st.caption("-------------------------")
    col_user4, _, col_user5 = st.columns([8, 1, 10])
    with col_user4:
        st.markdown('🖥️ **지원자 경력정보**')
        career_df = pd.DataFrame(settings.career_history)
        edited_career_df = st.experimental_data_editor(career_df, num_rows="dynamic", use_container_width=True)
    with col_user5:
        st.markdown('')
        my_achievements = st.text_area(
            '✒️ 지원자 경력기술서 및 성과에 대해서 입력하세요',
            settings.career_achievements,
            height=140,
            help=":grey_question: 자신의 역량을 드러낼 수 있는 성과를 입력하세요. 수치화하여 자세히 입력할 수록 결과물의 품질이 좋아집니다."
        )

st.caption("-------------------------")
st.info('AI에게 가이드를 받아보세요', icon="🤖")
col_ai1, _, col_ai2= st.columns([20, 1, 10])
with col_ai1:
    st.markdown('✏️ AI가 작성할 글의 주제를 직접 입력하거나 아래 주제 중 하나를 선택할 수 있습니다.')
    st.text_input(
        '',
        key='writing_type1',
        label_visibility="collapsed"
        )
    st.radio(
        "",
        ('자기소개', '지원동기', '나의 장단점'),
        key="writing_type2",
        label_visibility="collapsed"
        )
    if not st.session_state.writing_type1:
        subject = st.session_state.writing_type2
    else:
        subject = st.session_state.writing_type1
with col_ai2:
    min_letter, max_letter = st.slider(
        '✉️ 최소, 최대 글자수를 선택하세요',
        100, 1000, (400, 600))
    st.radio(
        "🔠 언어를 선택하세요",
        ('한국어', '영어'),
        key="lang_choice"
    )
    lang = f"{st.session_state.lang_choice}와 markdown 스타일로 작성하세요."
st.caption("-------------------------")

try:
    jp_desc = f"""
    - 회사이름: {company_name}
    - 채용직무: {position}
    - 직무기술: {requirements}
    - 맡게 될 업무: {main_tasks}
    - 회사에 대한 간단한 소개 및 정보: {intro}"""
except NameError:
    jp_desc = ''

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

with st.container():
    st.session_state.typed_text = ''
    if st.button('글 생성하기'):
        if jp_desc:
            _, col_center, _ = st.columns([1, 6, 1])
            with col_center:
                st.caption("⏳ 글 작성이 끝나면 [다운로드 버튼]이 나타납니다.")
                with st.container():
                    try:
                        response = openai.ChatCompletion.create(
                            model=st.session_state.model_name,
                            temperature=st.session_state.temperature,
                            messages=[
                                {"role": "system", "content": "You are a helpful assistant."},
                                {"role": "user", "content": f"나는 회사에 지원하는데 너의 도움이 필요해. 회사의 채용정보는 다음과 같아. {jp_desc}"},
                                {"role": "assistant", "content": "네, 알겠습니다. 위 채용정보를 기반으로 도와드리겠습니다."},
                                {"role": "user", "content": f"나는 다음과 같은 이력을 가지고 있어. {user_desc}"},
                                {"role": "assistant", "content": "네, 알겠습니다. 위 이력을 기반으로 도와드리겠습니다."},
                                {"role": "user", "content": f"{prompt_msg}+{lang}"}
                            ],
                            stream=True,
                        )
                    except Exception as e:
                        st.write(e)
                    title = f"### AI 추천 {subject}"
                    st.markdown(title)
                    placeholder = st.empty()
                    for chunk in response:
                        if chunk['choices'][0]['delta'].get('content'):
                            st.session_state.typed_text += chunk['choices'][0]['delta'].get('content')
                            with placeholder.container():
                                st.write(st.session_state.typed_text)
                    st.session_state.result_text = title + '\n' + st.session_state.typed_text
                    st.download_button('결과물 다운로드', st.session_state.result_text)
        else:
            st.caption("⚠️ 회사의 채용정보를 입력하지 않았습니다.")
    else:
        _, col_center, _ = st.columns([1, 6, 1])
        with col_center:
            try:
                st.write(st.session_state.result_text)
                st.download_button('결과물 다운로드', st.session_state.result_text)
                st.caption(f"⚠️ 전에 작성하신 글입니다. 새로 [글 생성하기]를 하시면 이 글은 사라집니다. [다운로드 버튼]을 눌러 다운로드하세요.")
            except AttributeError:
                st.caption(f"⚠️ 아직 작성한 글이 없습니다. [글 생성하기]를 눌러 글을 작성하세요.")
                pass
