import streamlit as st
import openai
import pandas as pd

import core.functions as funcs



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
    st.markdown("[OpenAI API keys 확인](https://platform.openai.com/account/api-keys)")
    st.text_input(
        "Enter your OpenAI API Keys 👇",
        "",
        key="API_KEY"
    )
    st.selectbox(
        "Choose GPT Model 👇",
        st.session_state.models,
        key="model_name"
    )
    st.slider(
        'Select Temperature',
        0.0, 1.0, 0.7,
        key="temperature"
    )
    st.markdown("===[채용공고 설정]===")
    st.selectbox(
        "Choose Data 👇",
        st.session_state.table_names,
        key="table_name"
    )

if st.session_state.API_KEY:
    openai.api_key = st.session_state.API_KEY

df = funcs.get_data(st.session_state.table_name)
skills = list(set(sum(df['skill_tags'].tolist(), [])))

with st.expander('원하는 직무를 검색하고 자소서를 작성할 채용공고를 선택하세요 👇'):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.text_input(
            "원하는 직무를 검색하세요 👇",
            "데이터 엔지니어",
            key="search_term"
        )
        st.markdown(f"- 채용공고 중 검색결과")
        temp_df = df[df['position'].str.contains(st.session_state.search_term)][['company_name', "position"]]
        st.dataframe(temp_df)
        st.selectbox(
                "Choose the Index No. of the Job Posting 👇",
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

            st.markdown('### 채용공고 상세정보')
            st.markdown("필드를 더블클릭하면 세부내용을 확인할 수 있습니다.")
            st.checkbox("Use container width", value=False, key="use_container_width")
            st.dataframe(posting, use_container_width=st.session_state.use_container_width)

with st.expander('지원자 정보를 자신의 정보에 맞게 수정하세요 👇'):
    st.markdown('- 박스를 더블클릭하면 정보를 수정할 수 있습니다.')
    st.markdown('### 지원자 기본정보')
    info_df = pd.DataFrame(
        [
            {
                "fullname": "이루오",
                "birthday": "1985.01.10",
                "sex": "male",
                "mbti": "ENTJ"
            }
        ]
    )
    edited_info_df = st.experimental_data_editor(info_df)

    st.markdown('### 지원자 학력정보')
    edu_df = pd.DataFrame(
        [
            {
                "name": "전남대학교",
                "major": "시각디자인",
                "start_dt": "2003.03",
                "end_dt": "2012.02",
                "status": "졸업",
                "kind": "학사"
            },
            {
                "name": "고려사이버대학교",
                "major": "인공지능",
                "start_dt": "2020.03",
                "end_dt": "2023.08",
                "status": "재학",
                "kind": "학사"
            }
    ]
    )
    edited_edu_df = st.experimental_data_editor(edu_df, num_rows="dynamic")

    st.markdown('### 지원자 경력정보')
    career_df = pd.DataFrame(
        [
            {
                "name": "그래이비랩",
                "department": "기업부설연구소 Ai lab.",
                "position": "Ai/Ml engineer Part Lead",
                "start_dt": "2022.05",
                "end_dt": "재직중"
            },
            {
                "name": "토익쉽어학원",
                "department": "",
                "position": "대표",
                "start_dt": "2017.08",
                "end_dt": "2020.08"
            }
        ]
    )
    edited_career_df = st.experimental_data_editor(career_df, num_rows="dynamic")

    my_skills = st.multiselect(
        'Choose your skills',
        skills,
        [])

    my_achievements = st.text_area(
        'Enter the description of your career achievements',
    '''### 1. B2B 서비스를 위한 딥러닝 분류 서비스 연구 및 웹 앱 개발
    - 문서 간 토픽모델링을 위한 LDA 분석 및 시각화
    - 텍스트 간 유사 범주 어휘 분석을 위해 PCA/t-SNE 분석 적용 및 시각화
    - 모델 성능 평가를 위한 10,000건의 테스트 데이터 구성
    - zero-shot classification과 gpt-3 모델 fine-tuning
    - 타 부서 업무 협업 웹앱 제공(streamlit 사용하여 DL 모델 서빙)'''
        )



    prompt_msg = f"""
    Write a self-introduction for the postion of {position} at {company_name}.
    Refer to the candidate's information and job description below.

    Here is the candidate information.
        - basic information: {edited_info_df.to_dict()}
        - education background: {edited_edu_df.to_dict()}
        - skills: {my_skills}
        - career: {edited_career_df.to_dict()}
        - achievements: {my_achievements}
    and Here is Job description:
        - job requirements: {requirements}
        - job main tasks: {main_tasks}
        - introduction of the company: {intro}

    It should be written in Korean and Markdown language.

    Refer to the following writing style and contents' flow.

    - 인사말 및 간단 자기소개 (학력을 언급하지는 말고 경력과 관련 역량 위주로 어필할 것)
    - 회사의 목표와 align된 지원동기 (왜 이 회사 혹은 지원하고자 하는 직무와 잘 맞는지 상세한 근거를 언급할 것)
    - 지원하고자 하는 직무와 align된 내가 보유한 대표 역량(커리어에 기반하여 작성), 스킬 및 관련된 세부 경험(목록을 만들지 말고 서술형으로 자연스럽게)
    - 지원하고자 하는 직무에 잘 맞는 나의 강점 (mbti성향을 참고하되 지원자의 mbti를 직접적으로 언급하지는 말 것) 및 관련된 경험 사례
    - 나의 앞으로의 계획 및 각오

    """

if st.button('AI 자소서 만들기'):
    try:
        completion = openai.ChatCompletion.create(
            model=st.session_state.model_name,
            temperature=st.session_state.temperature,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that write a self-introduction."},
                {"role": "user", "content": f"{prompt_msg}"}
            ]
        )
        st.markdown("### AI 추천 자소서 결과")
        st.markdown(completion.choices[0].message["content"])
    except Exception as e:
        st.write(e)
