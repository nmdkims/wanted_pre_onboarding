# wanted_pre_onboarding

<details>
<summary>과제 전문</summary>
<div markdown="1">

# 백엔드 코스 - 선발과제
## 과제안내

- 아래 서비스 개요 및 요구사항을 만족하는 REST API 서버를 구현합니다.
- 사용가능 언어 와 프레임워크: **Python - Django, Flask** 또는 **Javascript** - **Node.js(Express**, **NestJS)**

## 서비스 개요

- 본 서비스는 기업의 채용을 위한 웹 서비스 입니다.
- 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.

## 요구사항

1. **채용공고를 등록합니다.**
    
    <aside>
    ➡️ 회사는 아래 데이터와 같이 채용공고를 등록합니다.
    
    </aside>
    
    ```json
    Example)
    # 데이터 예시이며, 필드명은 임의로 설정가능합니다.
    {
      "회사_id":회사_id,
      "채용포지션":"백엔드 주니어 개발자",
      "채용보상금":1000000,
      "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
      "사용기술":"Python"
    }
    ```
    
2. **채용공고를 수정합니다.**
    
    <aside>
    ➡️ 회사는 아래 데이터와 같이 채용공고를 수정합니다. (회사 id 이외 모두 수정 가능합니다.)
    
    </aside>
    
    ```json
    Example)
    # 데이터 예시이며, 필드명은 임의로 설정가능합니다.
    {
      "채용포지션":"백엔드 주니어 개발자",
      "채용보상금":1500000, # 변경됨
      "채용내용":"원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다. 자격요건은..", # 변경됨
      "사용기술":"Python"
    }
    
    or
    
    {
      "채용포지션":"백엔드 주니어 개발자",
      "채용보상금":1000000,
      "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
      "사용기술":"Django" # 변경됨
    }
    ```
    
3. **채용공고를 삭제합니다.**
    
    <aside>
    ➡️ DB에서 삭제됩니다.
    
    </aside>
    
4. **채용공고 목록을 가져옵니다.**
    
    <aside>
    ➡️ 4-1. 사용자는 채용공고 목록을 아래와 같이 확인할 수 있습니다.
    
    </aside>
    
    ```json
    Example)
    [
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"원티드랩",
    	  "국가":"한국",
    	  "지역":"서울",
    	  "채용포지션":"백엔드 주니어 개발자",
    	  "채용보상금":1500000,
    	  "사용기술":"Python"
    	},
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"네이버",
    	  "국가":"한국",
    	  "지역":"판교",
    	  "채용포지션":"Django 백엔드 개발자",
    	  "채용보상금":1000000,
    	  "사용기술":"Django"
    	},
      ...
    ]
    ```
    
    <aside>
    ➡️ 4-2. 채용공고 검색 기능 구현**(선택사항 및 가산점요소).**
    
    </aside>
    
    ```json
    # Example - 1) some/url?**search=원티드**
    [
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"원티드랩",
    	  "국가":"한국",
    	  "지역":"서울",
    	  "채용포지션":"백엔드 주니어 개발자",
    	  "채용보상금":1500000,
    	  "사용기술":"Python"
    	},
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"원티드코리아",
    	  "국가":"한국",
    	  "지역":"부산",
    	  "채용포지션":"프론트엔드 개발자",
    	  "채용보상금":500000,
    	  "사용기술":"javascript"
    	}
    ]
    
    # Example - 2) some/url?**search=Django**
    [
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"네이버",
    	  "국가":"한국",
    	  "지역":"판교",
    	  "채용포지션":"Django 백엔드 개발자",
    	  "채용보상금":1000000,
    	  "사용기술":"Django"
    	},
    	{
    		"채용공고_id": 채용공고_id,
    	  "회사명":"카카오",
    	  "국가":"한국",
    	  "지역":"판교",
    	  "채용포지션":"Django 백엔드 개발자",
    	  "채용보상금":500000,
    	  "사용기술":"Python"
    	}
      ...
    ]
    ```
    
5. **채용 상세 페이지를 가져옵니다.**
    
    <aside>
    ➡️ 사용자는 채용상세 페이지를 아래와 같이 확인할 수 있습니다.
    
    - “채용내용”이 추가적으로 담겨있음.
    - 해당 회사가 올린 다른 채용공고 가 추가적으로 포함됩니다**(선택사항 및 가산점요소).**
    </aside>
    
    ```json
    Example)
    {
    	"채용공고_id": 채용공고_id,
      "회사명":"원티드랩",
      "국가":"한국",
      "지역":"서울",
      "채용포지션":"백엔드 주니어 개발자",
      "채용보상금":1500000,
      "사용기술":"Python",
    	"채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
    	"회사가올린다른채용공고":[채용공고_id, 채용공고_id, ..] # id List **(선택사항 및 가산점요소).**
    }
    ```
    
6. **사용자는 채용공고에 지원합니다(선택사항 및 가산점요소).**
    
    <aside>
    ➡️ 사용자는 채용공고에 아래와 같이 지원합니다. (가점 요소이며, 필수 구현 요소가 아님)
    
    - 사용자는 1회만 지원 가능합니다.
    </aside>
    
    ```json
    Example)
    {
    	"채용공고_id": 채용공고_id,
      "사용자_id": 사용자_id
    }
    ```
    

<aside>
☝ **개발 시 참조하세요!**

- 위 예시 데이터는 구현의 편의를 위해 제공되는 정보이며, 요구사항(의도)을 만족시킨다면 **다른 형태의 요청 및 리스폰스**를 사용하여도 좋습니다.

- 필요한 모델: **회사**, **사용자**, **채용공고,** 지원내역(선택사항)
  ****(이외 추가 모델정의는 자유입니다.)

- 위 제공된 **필드명**은 예시이며**, 임의로** 생성 가능합니다.

- 회사, 사용자 등록 절차는 생략합니다. 
  (**DB에 임의로 생성**하여 진행)

- 로그인 등 사용자 **인증절차는 생략합니다**.

- **Frontend 요소(html, css, js 등)는 개발 범위에 제외**됩니다. 
  (구현시 불이익은 없지만, 평가에 이점 또한 없습니다.)

- 명시되지 않은 조건또한 자유롭게 개발 가능합니다.

</aside>

## 필수 기술요건

- REST API 로 구현.
- ORM 사용하여 구현.
- RDBMS 사용 (SQLite, PostgreSQL 등).

## 평가 요소

- 요구사항 구현정도
    - 모든 기능을 구현하지 않더라도 평가를 진행합니다.
- 모델링
- REST API 설계 적합성
    - ex) Endpoint URL / 적절한 Request Methods 및 Response Status 등
- 코드 가독성 및 코드 컨벤션

## 기술점수 가산점 요소

- **(제출시기 가산점과 달리 기술점수 5점 이내 포함되는 가산점 입니다.)**
- 가산점이 포함된 요구사항 해결(요구사항 5~6)
- Unit Test 구현
- README 에 요구사항 분석 및 구현 과정을 작성
- Git commit 메시지 컨벤션
    
</div>
</details>


<details>
<summary>요구사항 분석 및 구현 과정</summary>
<div markdown="2">
필수 기술요건
REST API 로 구현.
ORM 사용하여 구현.
RDBMS 사용 (SQLite, PostgreSQL 등).
요구사항
1. 채용공고 Create.

2. 채용공고를 Update.
3. 채용공고를 Delete.
4-1. 채용공고 Read.

4-2. 채용공고 검색 Search(선택사항 및 가산점요소). _contains 이용 구상

5. 채용 상세 페이지를 가져옵니다. - detail page 불러오는 느낌으로 채용 공고 검색으로 나오는 내용 이외에 
    ** 채용내용이 있어야 함
    ** 해당 회사가 올린 다른 채용공고가 추가적으로 포함되는것은 가산점 요소 (가져오는 상세페이지 작성 회사를 이용해서 검색 )
6. 사용자는 채용공고에 지원합니다(선택사항 및 가산점요소). - many to many 구상중
 

</div>
</details>

