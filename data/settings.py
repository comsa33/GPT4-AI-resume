import yaml

# flask server
FLASK_SERVER_URL = "http://210.123.105.183:31888"  # Flask 서버의 URL을 설정합니다.

# linkedin setting
PROFILE_URL = 'https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams),emailAddress,headline,industryName,summary,location,positions,vanityName)'

# postgre credential setting
with open('credential/postgre_credentials.yaml', 'r') as file:
    cred_pg = yaml.safe_load(file)

POSTGRE_HOST = cred_pg['postgre']['host']
POSTGRE_PORT = cred_pg['postgre']['port']
POSTGRE_USERNAME = cred_pg['postgre']['username']
POSTGRE_PASSWORD = cred_pg['postgre']['password']
POSTGRE_DATABASE_1 = cred_pg['postgre']['database_1']

# gpt-4 api secret key
with open('credential/gptapi_credentials.yaml', 'r') as file:
    cred_gpt = yaml.safe_load(file)

GPT_SECRET = cred_gpt['gpt']['secret_key']

# user profile setting and prompt message setting
wanted_url_prefix = "https://www.wanted.co.kr/wd/"

user_info = [
                {
                    "fullname": "이코딩",
                    "birthday": "1988.01.01",
                    "sex": "male",
                    "mbti": "ENTJ"
                }
            ]
user_skills = [
    "python"
]
educations = [
                {
                    "name": "고려대학교대학원",
                    "major": "인공지능",
                    "start_dt": "2022.03",
                    "end_dt": "",
                    "status": "재학",
                    "kind": "석사",
                },
                {
                    "name": "고려사이버대학교",
                    "major": "인공지능",
                    "start_dt": "2019.03",
                    "end_dt": "2022.08",
                    "status": "졸업",
                    "kind": "학사"
                }
            ]
career_history = [
                    {
                        "name": "카카오",
                        "department": "Ai lab.",
                        "position": "Data engineer",
                        "start_dt": "2022.05",
                        "end_dt": "재직중"
                    },
                    {
                        "name": "위즈배라",
                        "department": "Ai lab",
                        "position": "Ai 개발자",
                        "start_dt": "2017.08",
                        "end_dt": "2021.08"
                    }
                ]
career_achievements = """1. B2B 서비스를 위한 딥러닝 분류 서비스 연구 및 웹 앱 개발
2. 웹 데이터 수집 프로그램 고도화, 데이터 ETL 엔진 및 REST API 개발 및 리딩
3. B2C “AI 진단 추천 서비스” 모델 개발
    - “기계학습을 이용한 구직자-구인자 컬쳐핏 매칭 방법” 에 대한 발명자로서 특허출원 (제2022-0109802호)
4. On Premise 인프라 사내 서버 구축(90%비용 절감효과 창출)
5. 빅데이터 ETL 파이프라인 구축
6. 서울시 IoT 도시데이터 분석(서울시청 외주)
"""

prompt_default = """회사의 가치, 문화, 비즈니스 및 기대하는 역량에 대한 이해를 토대로 작성하세요.
지나치게 길거나 어려운 문장은 피하세요. 간결하고 명확한 문장으로 긍정적인 이미지를 전달하며 읽기 쉽게 작성하세요.
개인적인 이야기와 성과를 통해 지원자의 독특한 가치를 증명할 수 있도록 작성하세요.
경험과 역량을 설명할 때 구체적인 예시를 들어서 설명하세요. 사례를 통해 지원자가 실제로 어떤 업무를 수행했는지 보여주어 신뢰성이 높은 글을 작성하세요.
존대말, 겸손한 표현 및 적절한 경어를 사용하여 전문성을 보여주세요. 지나친 자신감이나 거만한 표현은 피하세요."""

prompt_career = """
원하는 직무와 관련된 주요 역량, 스킬, 경험을 파악하세요. 직무 설명서, 채용 공고, 회사 웹사이트를 참고하며 업무와 관련된 기술 및 경험 요구사항을 반영해서 작성하세요.
직무와 관련된 핵심 역량 및 성과를 강조하는 것이 중요합니다. 업무 수행 과정에서 얻은 성과를 구체적인 수치나 예시로 설명하세요.
STAR 방법 사용: 경험을 기술할 때는 상황(Situation), 업무(Task), 행동(Action), 결과(Result)를 포함하는 STAR 방법을 사용하세요. 이를 통해 구체적이고 명확한 경험 기술이 가능해야합니다.
경력기술서는 읽기 쉽고 이해하기 쉬워야 합니다. 불필요한 정보를 제거하고, 중요한 내용을 명료하게 전달하세요. 문장은 간결하게 유지하며, 전문 용어는 풀어서 설명하세요.
"""

prompt_resume = """
워드 파일 형태의 테이블 구조를 사용하고, 다음과 같은 요소들을 고려해서 작성하세요.
템플릿 선택: 깔끔하고 직관적인 템플릿을 사용하세요. 보통 한국 기업들은 1~2페이지 분량의 이력서를 선호합니다. 필요한 정보를 요약하여 표현할 수 있는 템플릿을 선택하세요.
이력서 상단에는 지원하는 회사와 직무를 추가하세요.
사진 첨부: 한국 기업에서는 이력서에 사진을 첨부하는 것이 일반적입니다. 최근 3개월 이내에 촬영한 정장 착용한 정면 사진을 사용하세요. 사진은 깔끔한 이미지와 전문성을 갖춰야 합니다.
개인 정보: 이름, 생년월일, 연락처, 이메일 주소 등의 개인 정보를 명확하게 작성하세요. 이메일 주소는 전문적인 형태로 작성하는 것이 좋습니다.
학력: 최신 학력부터 역순으로 작성하세요. 학교명, 전공, 졸업 예정 또는 졸업일 등의 정보를 포함시키세요. 관련된 학력이나 자격증도 함께 작성합니다.
경력: 경력 정보도 최신 순서대로 역순으로 작성합니다. 회사명, 근무 기간, 직책, 주요 업무 등을 기술하세요. 인턴십, 아르바이트, 프로젝트 경험 등도 포함시킬 수 있습니다.
성과 및 업무 성취: 각 경력에서 이룬 성과나 업무 성취를 구체적으로 기술하세요. 가능하다면 성과를 나타내는 숫자, 비율, 또는 달성한 목표 등으로 표현하는 것이 좋습니다.
어학 및 기타 스킬: 해당 직무와 관련된 어학 능력, 컴퓨터 기술, 인터넷 기술 등을 작성하세요. 공인 시험 점수 또는 자격증 등을 기재하여 신뢰성을 높이세요.
자기소개: 이력서 마지막 부분에 간단한 자기소개를 작성하세요. 본인의 강점, 지원 동기, 포부 등을 간결하게 표현하세요. 이 부분에서 회사가 당신을 채용하고 싶어하는 이유를 제시해야 합니다.
"""

tips_career = """
경력기술서를 효율적으로 작성하려면 다음과 같은 단계를 따르면 좋습니다:

1. **분석 및 조사**: 원하는 직무와 관련된 주요 역량, 스킬, 경험을 파악하세요. 직무 설명서, 채용 공고, 회사 웹사이트를 참고하며 업무와 관련된 기술 및 경험 요구사항을 확인하세요.

2. **목록 작성**: 자신의 경력, 학력, 자격증, 기술, 프로젝트, 수행한 업무 등을 목록으로 작성하세요. 이를 토대로 경력기술서를 작성할 내용을 정리합니다.

3. **핵심 역량 및 성과 강조**: 직무와 관련된 핵심 역량 및 성과를 강조하는 것이 중요합니다. 업무 수행 과정에서 얻은 성과를 구체적인 수치나 예시로 설명하세요.

4. **STAR 방법 사용**: 경험을 기술할 때는 상황(Situation), 업무(Task), 행동(Action), 결과(Result)를 포함하는 STAR 방법을 사용하세요. 이를 통해 구체적이고 명확한 경험 기술이 가능합니다.

5. **간결하고 명료하게 작성**: 경력기술서는 읽기 쉽고 이해하기 쉬워야 합니다. 불필요한 정보를 제거하고, 중요한 내용을 명료하게 전달하세요. 문장은 간결하게 유지하며, 전문 용어는 풀어서 설명하세요.

6. **자기소개서와의 연계**: 경력기술서와 자기소개서는 서로 보완적인 관계입니다. 두 문서가 일관성을 유지하며, 각각의 강점을 부각시키는 것이 중요합니다.

7. **교정 및 피드백**: 완성된 경력기술서를 다른 사람에게 보여주고 피드백을 받으세요. 문법, 맞춤법, 내용의 논리성 등을 확인하며 꼼꼼하게 수정하세요.

8. **지속적인 업데이트**: 경력기술서는 자주 업데이트하는 것이 좋습니다. 새로운 경험, 프로젝트, 기술 등을 적절한 시기에 추가하며, 계속해서 개선해나갑니다.
"""
