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

st.info('원하는 직무를 검색하고 자소서를 작성할 채용공고를 선택하세요', icon="ℹ️")
with st.expander('펼쳐보기'):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.text_input(
            "- 원하는 직무를 검색하세요 👇",
            "데이터 엔지니어",
            key="search_term"
        )
        st.markdown(f"- 채용공고 중 검색결과")
        temp_df = df[df['position'].str.contains(st.session_state.search_term)][['company_name', "position"]]
        st.dataframe(temp_df)
        st.selectbox(
                "- 채용공고 인덱스를 선택하세요 👇",
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

            st.markdown('- 채용공고 상세정보')
            st.markdown("   (필드를 더블클릭하면 세부내용을 확인할 수 있습니다.)")
            st.checkbox("표 넓게보기", value=False, key="use_container_width")
            st.dataframe(posting, use_container_width=st.session_state.use_container_width)

st.info('지원자 정보를 자신의 정보에 맞게 수정하세요', icon="ℹ️")
with st.expander('펼쳐보기'):
    st.markdown('   (필드박스를 더블클릭하면 정보를 수정할 수 있습니다.)')
    st.markdown('- 지원자 기본정보')
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

    st.markdown('- 지원자 학력정보')
    edu_df = pd.DataFrame(
        [
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

    st.markdown('- 지원자 경력정보')
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
        '- 지원자 스킬정보',
        skills,
        [])

    my_achievements = st.text_area(
        '지원자 경력기술서 및 성과내용',
    '''1. B2B 서비스를 위한 딥러닝 분류 서비스 연구 및 웹 앱 개발
    - 문서 간 토픽모델링을 위한 LDA 분석 및 시각화
    - 텍스트 간 유사 범주 어휘 분석을 위해 PCA/t-SNE 분석 적용 및 시각화
    - 모델 성능 평가를 위한 10,000건의 테스트 데이터 구성
    - zero-shot classification과 gpt-3 모델 fine-tuning
    - 타 부서 업무 협업 웹앱 제공(streamlit 사용하여 DL 모델 서빙)'''
        )

st.info('AI에게 가이드를 받아보세요', icon="ℹ️")
with st.expander('펼쳐보기'):
    st.radio(
        "- AI가 작성할 글을 선택하세요 👇",
        ('자기소개서', '지원동기', '나의 장단점'),
        key="writing_type"
        )

    prompt_msg = f"""{company_name}의 {position} 직무에 지원하려는데 {st.session_state.writing_type}를 서술형으로 써줘(600~1000자 사이).
    한국어와 markdown 언어로 써줘.
    다음은 나에 대한 정보야.
        - 나의 개인 정보: {edited_info_df.to_dict()}
        - 나의 성향: {edited_info_df.to_dict()['mbti'][0]}
        - 내 학력: {edited_edu_df.to_dict()}
        - 내 보유 스킬: {my_skills}
        - 내 경력 정보: {edited_career_df.to_dict()}
        - 내 경력기술서 및 성과: {my_achievements}
    {company_name}의 {position} 직무에 대한 채용정보는 다음과 같아.
        - 직무기술: {requirements}
        - 맡게 될 업무: {main_tasks}
        - 회사에 대한 간단한 소개 및 정보: {intro}"""

    if st.button('글쓰기'):
        try:
            completion = openai.ChatCompletion.create(
                model=st.session_state.model_name,
                temperature=st.session_state.temperature,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that write a self-introduction."},
                    {"role": "user", "content": f"{prompt_msg}"}
                ]
            )
            st.markdown(f"### AI 추천 {st.session_state.writing_type} 결과")
            st.markdown(completion.choices[0].message["content"])
        except Exception as e:
            st.write(e)
