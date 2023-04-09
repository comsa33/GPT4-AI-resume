# GPT-4 API-base Cover Letter Creation Service

> 인공지능 기반의 기술이 급속하게 발전함에 따라, 다양한 분야에서 그 효용성이 인정받고 있습니다.
> 특히, 자연어 처리 분야에서 GPT-4와 같은 고급 기술의 출현은 인간의 언어를 이해하고 생성하는 
> 놀라운 성과를 보여주고 있습니다. 이러한 배경 속에서 본 서비스는 "GPT-4 기반 채용공고별 AI 자소서 
> 작성 가이드 개인화"를 목표로, 지원자들에게 시간 절약과 효율적으로 작성된 글을 제공함으로써 
> 시스템적으로 기여하는 새로운 서비스입니다.

## 연구 방법론
> 본 연구에서는 시간 절약과 효율적인 글 작성을 위한 서비스를 개발하였다.
> 서비스는 다음과 같은 방법론을 통해 구현되었다.
> - 시간절약: 서비스는 채용공고 스크래핑, DB적재, 채용공고 검색 및 필터링, 사용자 정보 입력, 자기소개서 주제 입력, 개인화 자기소개서 작성, 다운로드까지 end-to-end로 구성되어 시간 절약을 실현한다.
> - 효율적인 글 작성 능력 제공: 본 연구에서는 연구 및 실험을 통해 가장 최적화된 프롬프트 적용 방식을 찾아 지원자의 역량이 지원하고자 하는 회사와 직무에 잘 드러날 수 있도록 서비스를 제공한다. 이를 위해 4단계 프롬프트를 활용하여 GPT-4 모델에게 대화식으로 정보를 제공하고, 지원자의 역량이 가장 잘 드러날 수 있는 글을 작성하도록 한다.
## 실험 및 결과
> 본 연구에서는 지원자의 역량을 가장 잘 드러내는 글을 작성하기 위해 최적화된 프롬프트를 연구하고 
> 실험하였다. 실험 결과를 통해 얻어진 4단계 프롬프트는 다음과 같다:
> 1. 시스템 역할 설정
> 2. 회사의 채용 정보 전달
> 3. 지원자의 이력 정보 전달
> 4. 지원자가 작성하고자 하는 자기소개서에 대한 요구사항 전달
```python
openai.ChatCompletion.create(
    model=st.session_state.model_name,
    temperature=st.session_state.temperature,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"나는 회사에 지원하는데 너의 도움이 필요해. 회사의 채용정보는 다음과 같아. {채용공고 정보}"},
        {"role": "assistant", "content": "네, 알겠습니다."},
        {"role": "user", "content": f"나는 다음과 같은 이력을 가지고 있어. {사용자 정보}"},
        {"role": "assistant", "content": "네, 알겠습니다."},
        {"role": "user", "content": f"{자기소개서 작성 프롬프트}+{작성 언어 정보}"}
    ],
    stream=True,
)
```

![image](https://user-images.githubusercontent.com/61719257/228704474-6d2af724-b3a3-4f55-9701-af77e7d4686a.png)
_[그림 1] http://gpt-recruit.com GPT-4 채용공고별 자소서 가이드 서비스 화면: GPT모델 선택 기능, 글 창작성 파라미터 조절 기능, 글 주제 입력 창, 글 생성하기 버튼, 작성된 글 화면 및 결과물 다운로드 버튼을 포함한 서비스 인터페이스_


- service link: https://gpt-recruit.com/
- 관련 문서: [GPT-4 기반 채용공고별 AI 자소서 작성 가이드 개인화 서비스](https://github.com/comsa33/GPT4-AI-resume/blob/main/KIPS_3.pdf)



## LICENSE

이 프로젝트는 [GNU 라이선스](https://github.com/comsa33/GPT4-AI-resume/blob/main/LICENSE)에 따라 라이선스가 부여됩니다.

Copyright © 2023 이루오. All Rights Reserved.
