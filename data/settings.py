POSTGRE_HOST = "210.123.105.183"
POSTGRE_PORT = "30523"
POSTGRE_USERNAME = "postgres"
POSTGRE_PASSWORD = "4460"
POSTGRE_DATABASE_1 = "ai_lab"

user_info = [
                {
                    "fullname": "이루오",
                    "birthday": "1985.01.10",
                    "sex": "male",
                    "mbti": "ENTJ"
                }
            ]
educations = [
                {
                    "name": "전남대학교",
                    "major": "시각디자인",
                    "start_dt": "2003.03",
                    "end_dt": "2012.02",
                    "status": "졸업",
                    "kind": "학사",
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
career_history = [
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
                        "end_dt": "2016.06",
                    },
                    {
                        "name": "세계외국어학원",
                        "department": "토익부",
                        "position": "토익 전임 강사",
                        "start_dt": "2013.03",
                        "end_dt": "2014.10",
                    },
                    {
                        "name": "이은식어학원",
                        "department": "",
                        "position": "토익 강사",
                        "start_dt": "2011.05",
                        "end_dt": "2012.05",
                    }
                ]
career_achievements = """1. B2B 서비스를 위한 딥러닝 분류 서비스 연구 및 웹 앱 개발
- 문서 간 토픽모델링을 위한 LDA 분석 및 시각화
- 텍스트 간 유사 범주 어휘 분석을 위해 PCA/t-SNE 분석 적용 및 시각화
- 모델 성능 평가를 위한 10,000건의 테스트 데이터 구성
- zero-shot classification과 gpt-3 모델 fine-tuning
- 타 부서 업무 협업 웹앱 제공(streamlit 사용하여 DL 모델 서빙)

2. 웹 데이터 수집 프로그램 고도화, 데이터 ETL 엔진 및 REST API 개발 및 리딩
- DDD(domain driven development)에 따른 개발 설계
- postgreSQL 과 MongoDB ERD설계 및 data lake 구축
- fastAPI를 사용하여 REST API 개발
- OAuth2.0 리소스 서버 구축
- k8s와 컨테이너 환경에서 스크래핑 앱 개발 및 배포
- teamcity를 통한 CI/CD

3. B2C “AI 진단 추천 서비스” 모델 개발
- 120만건 텍스트 데이터 형태소 분석 및 자연어처리(kiwi 사용)
- 문서/토큰 간 유사도 계산 알고리즘 개발 (gensim/text-distance 사용)
- 유사 기업 클러스터링 엔진 연구 개발 및 테스트
- 구직자-기업 간 컬쳐핏 매칭률 산출 알고리즘 개발
- 1000명의 베타 테스터를 통한 B2C 플랫폼, GRABBER "AI진단" 서비스 론칭
- “기계학습을 이용한 구직자-구인자 컬쳐핏 매칭 방법” 에 대한 발명자로서 특허출원 (제2022-0109802호)

4. On Premise 인프라 사내 서버 구축(90%비용 절감효과 창출)
- Kuberenetes 클러스터 구축
- Teamcity CI/CD 구축
- 월 평균 개발 유지비용 90% 절감
- 개발 환경 구축 평균 시간 50% 감소

5. “2022년 인공지능 온라인 경진대회”에 팀 “그레이비랩”으로 참여
- QA(문서 검색 효율화를 위한 기계독해 문제) task를 위한 KoElectra 모델 finetuning
- 한국어 텍스트 데이터 전처리 및 데이터 증강 수행
- 평가지표(EM, Exact Matching) 65.07점 기록

6. 빅데이터 ETL 파이프라인 구축
- Scrapy 모듈을 사용하여 웹 스크래퍼 제작
- 데이터 파이프라인 기존 레거시 코드 고도화
- 120만건 정형/비정형 데이터 분산 수집 및 MongoDB 적재
- AWS LightSail 클라우드 환경 구축
- Jenkins CI/CD 구축 및 관리

7. 서울시 IoT 도시데이터 분석(서울시청 외주)
- 시계열 데이터 분석 및 정제
- 시계열 데이터 분석 시각화 리포트 작성
- 도메인 별 시계열 데이터 품질 가이드 템플릿 작성"""

prompt_default = """회사의 가치, 문화, 비즈니스 및 기대하는 역량에 대한 이해를 토대로 작성하세요.
지나치게 길거나 어려운 문장은 피하세요. 간결하고 명확한 문장으로 긍정적인 이미지를 전달하며 읽기 쉽게 작성하세요.
개인적인 이야기와 성과를 통해 지원자의 독특한 가치를 증명할 수 있도록 작성하세요.
경험과 역량을 설명할 때 구체적인 예시를 들어서 설명하세요. 사례를 통해 지원자가 실제로 어떤 업무를 수행했는지 보여주어 신뢰성을 높은 글을 작성하세요.
존대말, 겸손한 표현 및 적절한 경어를 사용하여 전문성을 보여주세요. 지나친 자신감이나 거만한 표현은 피하세요.
한국어와 markdown 언어로 작성하세요."""
