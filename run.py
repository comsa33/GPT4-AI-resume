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
    st.selectbox(
        "Choose Data 👇",
        st.session_state.table_names,
        key="table_name"
    )
    st.text_input(
        "Enter the position you are interested in 👇",
        "데이터 엔지니어",
        key="search_term"
    )

if st.session_state.API_KEY:
    openai.api_key = st.session_state.API_KEY

df = funcs.get_data(st.session_state.table_name)
skills = sum(df['skill_tags'].tolist(), [])

st.dataframe(df[df['position'].str.contains(st.session_state.search_term)][['company_name', "position"]])

st.text_input(
    "Enter the Index No. of the Job Posting 👇",
    "",
    key="jp_index"
    )


info_df = pd.DataFrmae(
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
edited_edu_df = st.experimental_data_editor(edu_df)

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
        },
        {
            "name": "고파토익어학원",
            "department": "",
            "position": "대표",
            "start_dt": "2014.11",
            "end_dt": "2016.06"

        },
        {
            "name": "세계외국어학원",
            "department": "토익부",
            "position": "토익 전임 강사",
            "start_dt": "2013.03",
            "end_dt": "2014.10"
        },
        {
            "name": "이은식어학원",
            "department": "",
            "position": "토익 강사",
            "start_dt": "2011.05",
            "end_dt": "2012.05"
        }
    ]
)
edited_career_df = st.experimental_data_editor(career_df)

my_skills = st.multiselect(
    'Choose your skills',
    skills,
    [])

my_achievements = st.text_area(
    'Enter the description of your career achievements',
'''
### 1. B2B 서비스를 위한 딥러닝 분류 서비스 연구 및 웹 앱 개발
- 문서 간 토픽모델링을 위한 LDA 분석 및 시각화
- 텍스트 간 유사 범주 어휘 분석을 위해 PCA/t-SNE 분석 적용 및 시각화
- 모델 성능 평가를 위한 10,000건의 테스트 데이터 구성
- zero-shot classification과 gpt-3 모델 fine-tuning
- 타 부서 업무 협업 웹앱 제공(streamlit 사용하여 DL 모델 서빙)

### 2. 웹 데이터 수집 프로그램 고도화, 데이터 ETL 엔진 및 REST API 개발 및 리딩
- DDD(domain driven development)에 따른 개발 설계
- postgreSQL 과 MongoDB ERD설계 및 data lake 구축
- fastAPI를 사용하여 REST API 개발
- OAuth2.0 리소스 서버 구축
- k8s와 컨테이너 환경에서 스크래핑 앱 개발 및 배포
- teamcity를 통한 CI/CD

### 3. B2C “AI 진단 추천 서비스” 모델 개발
- 120만건 텍스트 데이터 형태소 분석 및 자연어처리(kiwi 사용)
- 문서/토큰 간 유사도 계산 알고리즘 개발 (gensim/text-distance 사용)
- 유사 기업 클러스터링 엔진 연구 개발 및 테스트
- 구직자-기업 간 컬쳐핏 매칭률 산출 알고리즘 개발
- 1000명의 베타 테스터를 통한 B2C 플랫폼, GRABBER "AI진단" 서비스 론칭
- “기계학습을 이용한 구직자-구인자 컬쳐핏 매칭 방법” 에 대한 발명자로서 특허출원 (제2022-0109802호)

### 4. On Premise 인프라 사내 서버 구축(90%비용 절감효과 창출)
- Kuberenetes 클러스터 구축
- Teamcity CI/CD 구축
- 월 평균 개발 유지비용 90% 절감
- 개발 환경 구축 평균 시간 50% 감소

### 5. “2022년 인공지능 온라인 경진대회”에 팀 “그레이비랩”으로 참여
- QA(문서 검색 효율화를 위한 기계독해 문제) task를 위한 KoElectra 모델 finetuning
- 한국어 텍스트 데이터 전처리 및 데이터 증강 수행
- 평가지표(EM, Exact Matching) 65.07점 기록

### 6. 빅데이터 ETL 파이프라인 구축
- Scrapy 모듈을 사용하여 웹 스크래퍼 제작
- 데이터 파이프라인 기존 레거시 코드 고도화
- 120만건 정형/비정형 데이터 분산 수집 및 MongoDB 적재
- AWS LightSail 클라우드 환경 구축
- Jenkins CI/CD 구축 및 관리

### 7. 서울시 IoT 도시데이터 분석(서울시청 외주)
- 시계열 데이터 분석 및 정제
- 시계열 데이터 분석 시각화 리포트 작성
- 도메인 별 시계열 데이터 품질 가이드 템플릿 작성
'''
    )

if st.session_state.jp_index:
    posting = df.iloc[int(st.session_state.jp_index)]

    company_name = posting['company_name']
    position = posting['position']
    requirements = posting['requirements']
    main_tasks = posting['main_tasks']
    intro = posting['intro']

    st.dataframe(posting)


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
    completion = openai.ChatCompletion.create(
        model=st.session_state.model_name,
        temperature=st.session_state.temperature,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that write a self-introduction."},
            {"role": "user", "content": f"{prompt_msg}"}
        ]
    )
    st.markdown(completion.choices[0].message["content"])
