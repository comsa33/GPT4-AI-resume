POSTGRE_HOST = "210.123.105.183"
POSTGRE_PORT = "30523"
POSTGRE_USERNAME = "postgres"
POSTGRE_PASSWORD = "4460"
POSTGRE_DATABASE_1 = "ai_lab"

my_secret = "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"

user_info = [
                {
                    "fullname": "이루오",
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

prompt_default = f"""회사의 가치, 문화, 비즈니스 및 기대하는 역량에 대한 이해를 토대로 작성하세요.
지나치게 길거나 어려운 문장은 피하세요. 간결하고 명확한 문장으로 긍정적인 이미지를 전달하며 읽기 쉽게 작성하세요.
개인적인 이야기와 성과를 통해 지원자의 독특한 가치를 증명할 수 있도록 작성하세요.
경험과 역량을 설명할 때 구체적인 예시를 들어서 설명하세요. 사례를 통해 지원자가 실제로 어떤 업무를 수행했는지 보여주어 신뢰성을 높은 글을 작성하세요.
존대말, 겸손한 표현 및 적절한 경어를 사용하여 전문성을 보여주세요. 지나친 자신감이나 거만한 표현은 피하세요."""
