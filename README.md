# 6개월 AI 웹서비스 개발 로드맵

## 1주차 (환경 세팅 + 첫 자동화)

### 오늘 한 것
- Python, VS Code, Git, Claude Code 설치 및 환경 세팅 완료
- Claude Code에게 요청해서 `organize_files.py` 제작
  - 폴더 안 파일들을 확장자별로 하위 폴더(jpg, pdf, txt 등)로 자동 정리하는 스크립트
  - 폴더/스크립트 자기 자신은 건너뛰는 예외 처리 포함
- 파이썬 기초 개념을 직접 타이핑하며 학습: 변수, 리스트, `for`문, `if`/`else` 조건문
- 테스트 파일 만들어서 스크립트 실행 → 정상 작동 확인
- Git 초기 설정(`git config`) 및 첫 커밋, GitHub 원격 저장소에 push 완료

### 배운 점
- **`import`**: 파이썬에 기본 내장 안 된 기능(파일 이동 등)을 외부 도구 상자에서 가져다 쓰는 것
- **`for`문**: 리스트 안 항목들을 하나씩 꺼내서 반복 처리
- **`if`/`else`**: 조건에 따라 다른 코드 실행
- **Guard clause 패턴**: 작업(파일 이동) 전에 먼저 예외 상황(폴더인지, 스크립트 자신인지)을 걸러내야 에러를 막을 수 있다는 것
- **저장(Ctrl+S) → 실행 흐름**: 코드를 고쳐도 저장 안 하면 예전 버전이 실행된다는 것을 삽질하며 직접 체득

### 막힌 점
- `IndentationError`로 한참 헤맴 — 에디터 화면과 실제 저장된 파일 내용이 달라서 발생 (저장 누락이 원인)
- 터미널 명령어 오타(`pypython`, `organize.py` 등)로 인한 시행착오
- Git 최초 사용 시 `user.email`/`user.name` 설정이 안 되어 있어서 커밋 실패 → 설정 후 해결

### 다음 목표 (2주차)
- Python 기초 복습 (딕셔너리, 함수)
- HTTP/JSON/API 개념 이해
- 공개 API로 데이터 가져오는 스크립트 제작

## 2주차 - Day 1 (Open-Meteo API 연동)

### 오늘 한 것
- 딕셔너리, 함수 복습
- requests 라이브러리 설치
- Claude Code로 Open-Meteo API 연동 스크립트(weather.py) 제작
  - 대구 위도/경도 기준 현재 기온/날씨/바람 출력
- git push 중 원격 저장소(README.md)와 충돌 → git pull로 병합 → push 성공

### 배운 점
- 딕셔너리: 순서가 아니라 이름(key)으로 값을 찾음 → JSON과 구조가 동일해서 API 데이터 다룰 때 필수
- API: 다른 서버의 데이터/기능을 요청-응답으로 빌려쓰는 통로
- JSON: 서버가 텍스트로 보내는 딕셔너리 형태 데이터. `.json()`으로 파이썬 딕셔너리로 변환
- `.get(key, 기본값)` vs `[key]`: `[key]`는 없는 키 접근 시 KeyError로 프로그램이 죽지만, `.get()`은 못 찾으면 기본값을 대신 반환해 프로그램이 안 죽게 함 (API 응답 실패 대비 안전장치)
- git merge 충돌: 원격에 로컬에 없는 커밋(README)이 있으면 push가 거부됨 → `git pull`로 먼저 받아와 병합 후 push해야 함 → Vim 편집기에서 `:wq`로 저장 후 종료하는 법 익힘

### 막힌 점
- git push 거부 (remote에 로컬에 없는 변경사항 존재) → git pull → merge commit(Vim 화면) → push 순서로 해결

### 다음 목표
- 문서 요약기(6주차 예정) 또는 다른 공개 API로 추가 스크립트 실습
- HTTP GET/POST 차이, 상태 코드(200, 404 등) 개념 짧게 정리## 2주차 - Day 1 (전체 완료)

### 오늘 만든 것
- day2_weather.py — Open-Meteo API 기본 연동 (대구 날씨 조회)
- day2_status_test.py — HTTP 상태 코드(200/404) 실험용 스크립트
- day2_multi_city.py — 함수 + 중첩 딕셔너리로 여러 도시 날씨 조회 (오늘 메인 결과물)

### 배운 것
- 딕셔너리: 이름(key)으로 값을 찾는 구조. 리스트보다 안전한 이유는 순서를 몰라도 이름으로 정확히 값을 꺼낼 수 있기 때문
- 중첩 딕셔너리: 한 항목이 여러 정보(위도/경도 등)를 가질 때, 딕셔너리 안에 딕셔너리를 넣어서 이름으로 안전하게 관리
- API/HTTP: 서버에 요청(request) 보내면 응답(response)을 돌려받는 통로. GET은 조회, POST는 3개월차에 다룰 예정
- 상태 코드: 200(성공), 404(요청 실패) 등 서버가 결과를 숫자로 알려줌
- response.raise_for_status(): 상태 코드가 비정상이면 즉시 에러를 발생시켜 프로그램을 멈추는 안전장치. 없으면 문제를 놓치고 계속 진행됨
- .json(): 서버가 텍스트로 보낸 JSON 데이터를 파이썬 딕셔너리로 변환
- .get(key, 기본값): 키가 없어도 에러 없이 기본값을 반환 (KeyError 방지, API 실패 대비 안전장치)
- 함수 설계: 함수가 반복해서 쓰는 데이터(cities 딕셔너리)나 도구(import)는 함수 밖, 파일 상단에 둬야 매번 새로 안 만들고 공용으로 재사용 가능

### 막힌 점 / 해결
- git push 거부(원격에 로컬에 없는 README 존재) → git pull로 병합 → Vim에서 :wq로 커밋 메시지 저장 → push 성공
- 폴더 이름 변경 과정에서 코딩\코딩, py\py 같은 중첩 폴더 발생 → dir로 원인 추적 → robocopy /E /MOVE로 병합, 중복 폴더 삭제하며 정리

### 다음 목표
- HTTP POST 개념 (3개월차 예정이지만 가볍게만)
- 다른 공개 API로 추가 스크립트 실습 또는 6주차 문서 요약기로 진행

## 2주차 - Day 3 (전체 완료)

### 오늘 만든 것
- day3_weather_input.py — day2_multi_city.py를 업그레이드
  - input()으로 사용자가 직접 도시 이름 입력
  - try/except로 API 요청 실패 시 에러 처리
- day3_todo.py — 메뉴 기반 할일 관리 프로그램
  - 1.할일 추가 / 2.완료 처리 / 3.목록 보기 / 4.종료
  - 딕셔너리 리스트({"task": ..., "done": ...})로 할일 관리
  - 인덱스 변환 + 범위 체크로 완료 처리 시 에러 방지
  - 잘못된 메뉴 입력 시 안내 메시지 처리

### 배운 것
- 함수 매개변수: def func(x):의 x는 호출 시점(func(값))에 실제 값을 받는 "빈 상자" — 정의할 땐 값이 없어도 문제없음
- .get()은 다 다른 함수: dict.get(), requests.get(), response.raise_for_status()는 이름이 겹치거나 비슷해 보여도 서로 소속(딕셔너리/requests 라이브러리/Response 객체)이 다른 완전히 별개의 기능
- [] vs .get(): 확실히 존재하는 값은 []로 바로 꺼내고, 없을 수도 있는 값(사용자 입력, API 응답)은 .get()으로 안전하게 처리
- try/except: 항상 세트로 동작. 넓게(except Exception) 잡으면 프로그램은 안 죽지만 진짜 버그(오타 등)까지 숨겨버림 → requests.exceptions.RequestException처럼 좁게 잡는 게 좋은 습관
- while True / break: 조건 없이 무한 반복하다가 특정 조건에서 break로 탈출하는 패턴
- f-string: f"{변수}" 형태로 문자열 안에 변수 값을 끼워 넣는 문법 (줄바꿈과 무관)
- 인덱스 개념: 사람은 1부터 세지만 파이썬 리스트는 0부터 셈 → 사용자 입력(예: "2번째")을 실제 인덱스로 쓰려면 int(입력값) - 1 변환 필요
- 범위 체크: len(리스트)로 리스트 크기를 확인해서, 존재하지 않는 인덱스에 접근하면 나는 IndexError를 미리 방지 (if 인덱스 < 0 or 인덱스 >= len(리스트))
- 딕셔너리 값 읽기 vs 바꾸기: dict["key"]는 읽기, dict["key"] = 새값은 값을 덮어쓰는 것
- 삼항 연산자: 결과 = A if 조건 else B — if/else를 한 줄로 축약

### 막힌 점 / 해결
- 함수 중첩 정의, 들여쓰기 오류(IndentationError) 여러 번 발생 → 콜론(:) 다음 줄은 같은 블록끼리 들여쓰기 레벨이 정확히 일치해야 한다는 걸 체득
- return 위치를 잘못 둬서 그 아래 코드가 죽은 코드가 되는 실수 경험
- 변수 이름 불일치(city_info로 선언하고 city로 사용)로 인한 NameError 디버깅

### 다음 목표
- 리스트/딕셔너리 조합을 더 활용한 확장 (예: 할일 삭제 기능, 우선순위 추가 등)
- 아직 남은 2주차 분량 또는 3~4주차 미니 프로젝트로 자연스럽게 연결 가능한 수준 도달

## Day 3 (이어서 작업) — todo 앱 완성

배운 것:
- try/except ValueError로 잘못된 입력 방어
- json.dump/json.load로 데이터 파일 저장·불러오기 (dump/load는 파일용, dumps/loads는 문자열용)
- del todos[index]로 리스트 항목 삭제, 삭제 시 인덱스가 자동으로 당겨짐(밀림) 이해

막힌 것:
- 함수(def)를 while 루프 안에 정의해서 매 반복마다 재정의되는 실수
- try/except 들여쓰기 에러 (콜론 다음 줄은 항상 한 단계 들여쓰기)

결과물:
- day3_todo.py: 추가/완료처리/목록보기/삭제 + JSON 영속성까지 갖춘 완성형 todo 앱
- 로드맵 3~4주차 "미니 프로젝트 완성" 기준 충족

## 3주차 - Day 4 (OCR + Anthropic Claude 텍스트 요약기)

### 오늘 한 것
- Anthropic 콘솔에서 Claude API 키 발급 및 `python-dotenv`로 `.env`에서 관리
- `py/day4_summarizer.py`에서 `open`/`with`로 `py/input.txt`를 읽고 요약 요청
- `client.messages.create()`로 Claude 모델 호출 성공
- API 호출을 `try/except`로 감싸서 예외를 처리하도록 개선
- `py/day4_pdf_summarizer.py`로 `pypdf` 기반 PDF 텍스트 추출 구현
  - 한글 폰트 인코딩 문제를 디버깅하고 `try/except`로 파일 없음 오류 처리
  - `enumerate()`로 페이지 구분자를 추가하여 출력 정리
- `py/day4_ocr.py`로 `pytesseract` 기반 이미지 OCR 처리 구현
  - Tesseract 설치와 PATH 환경변수 설정 문제를 해결
  - `lang='kor+eng'`로 한/영 동시 인식 지원
- `py/day4_ocr_summarizer.py`에서 이미지 → OCR → AI 요약 파이프라인 완성
  - 기존 두 도구를 조립하고 중복 import 제거 및 불필요 코드 정리 진행
- `.gitignore`에 `.env`, `__pycache__/`, `*.py[cod]` 포함 유지

### 배운 점
- 비밀 키는 저장소에 직접 두지 않고 `.env`로 분리해야 안전하다
- 파일을 읽어와서 모델 요청 텍스트로 사용하는 패턴은 재사용성이 높다
- API 호출은 항상 예외가 발생할 수 있으므로 `try/except`로 감싸야 안정적이다
- PDF 파싱과 OCR을 함께 사용하면 텍스트 데이터 수집 범위를 크게 확장할 수 있다
- OCR 결과를 요약 파이프라인에 연결하면 이미지 기반 문서 처리 자동화가 가능하다

### 결과
- 로드맵 7주차 목표(OCR 도구) 달성
- `README.md` 문서도 최신 작업 내용으로 업데이트됨
- 8주차(음성/유튜브 요약)로 이어질 예정
