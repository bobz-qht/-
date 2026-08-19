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

## 5일차 (2개월차 8주차) — 유튜브 요약 도구

### 만든 것
- `day4_summarizer.py`: 텍스트 요약 로직을 `summarize_text(text)` 함수로 리팩토링 (재사용 가능하게)
- `day5_youtube_summarizer.py`: `youtube-transcript-api`로 자막 텍스트 추출 → 요약 (빠름, 자막 있는 영상만 처리 가능)
- `day5_whisper_summarizer.py`: `yt-dlp`로 오디오 다운로드 → `whisper`로 음성인식 → 요약 (느리지만 자막 없는 영상도 처리 가능)
- `day5_smart_summarizer.py`: 자막 추출을 먼저 시도하고, 실패하면 자동으로 Whisper 방식으로 전환하는 fallback 로직 구현

### 배운 것
- **`print`와 `return`의 차이** — 값을 화면에 보여주는 것과 다른 코드가 재사용할 수 있게 값을 넘겨주는 것은 다르다
- **`import`(모듈 통째로) vs `from ... import`(필요한 것만)** 차이와 각각의 호출 방식
- **`if __name__ == "__main__":`의 역할** — 파일을 직접 실행할 때와 다른 파일에서 import될 때를 구분
- **외부 라이브러리는 버전이 바뀌면 API가 통째로 바뀔 수 있다** (`youtube-transcript-api`가 v1.0에서 `get_transcript` 정적 메서드를 삭제하고 인스턴스 기반 `.fetch()` 방식으로 변경됨) — 에러 메시지 읽고 최신 문서 찾아서 대응하는 것도 실무 스킬
- **try/except를 이용한 fallback 패턴** — 빠르고 가벼운 방법을 먼저 시도하고, 실패 시 느리지만 확실한 방법으로 자동 전환

### 막힌 점 / 한계
- `youtube-transcript-api`의 `get_transcript` 메서드가 최신 버전에서 삭제되어 `YouTubeTranscriptApi().fetch()` + 객체 속성 접근(`snippet.text`) 방식으로 수정
- ffmpeg가 시스템에 설치되어 있지 않아 winget으로 별도 설치 필요 (yt-dlp의 오디오 추출에 필수)
- Whisper `base` 모델은 크기가 작아 정확도가 떨어질 수 있음 — 실제 테스트에서 배경음/노이즈가 있는 영상에서 원본과 무관한 내용(요리 재료 등)을 생성하는 hallucination 현상 확인. 추후 `small`/`medium` 모델 비교 필요

### 마일스톤
**🎯 2개월차(AI 기능 붙이기) 전체 완료.** 텍스트 요약기, PDF 요약기, OCR 도구, 유튜브 요약기(자막/Whisper/fallback 3종)까지 작동하는 AI 도구 다수 확보.

### 다음
3개월차 진입 — 9주차: Webhook 개념 + 간단 실습

## 3개월차 - 9~10주차 (Day 6): Webhook + 조건 분기 + 이메일 연동

### 오늘 만든 것
- `day6_webhook.py`: Flask 기반 웹훅 수신 서버
  - POST 요청으로 들어온 JSON 데이터 수신 및 콘솔 출력
  - `event` 값에 따른 조건 분기 (`urgent` / `form_submit` / 그 외)
  - `urgent` 이벤트 시 Gmail 앱 비밀번호(`smtplib`)로 실제 이메일 알림 발송
  - 웹훅 로그를 리스트로 계속 누적 저장 (JSON 파일)

### 배운 것
- **Webhook**: 내가 요청을 보내는 게 아니라, 남이 보낸 요청을 받아서 반응하는 구조. 지금까지의 `requests.get()`(클라이언트 역할)과 정반대 방향
- **Flask 기본 구조**: `@app.route()`로 URL 경로와 함수를 연결, `request.json`으로 들어온 데이터 추출, `return`으로 응답
- **`response.json()` vs `request.json`**: 전자는 내가 요청 보낸 뒤 받는 응답 해석, 후자는 내가 서버로서 받은 요청 데이터 추출 — 방향이 반대
- **파일 모드(`'w'` vs `'a'`) 함정**: `'w'`로 매번 저장하면 덮어써짐 → 읽어서 리스트에 append 후 다시 쓰는 패턴으로 해결
- **데이터 유효성 방어**: 파일이 "존재하는 것"과 "내용이 유효한 것"은 별개 문제
  - `isinstance(logs, list)`로 타입 불일치 방어 (dict가 남아있던 사례)
  - `json.JSONDecodeError`로 빈 파일 방어
- **Gmail 앱 비밀번호**: 실제 로그인 비밀번호 대신 프로그램 전용 키 발급, `.env`로 분리 관리 (기존 API 키 관리 패턴과 동일)
- **`smtplib` + `MIMEText`**: 파이썬 내장 라이브러리로 SMTP 서버 접속 → 로그인 → 메일 전송

### 막힌 점 / 해결
- 서버 파일 실행 시 아무 반응 없음 → `if __name__ == '__main__': app.run(...)` 누락이 원인
- `AttributeError: 'dict' object has no attribute 'append'` → 이전 버전 코드가 저장해둔 dict 형식 파일이 남아있어 발생 → 타입 체크 방어 코드 추가
- `NameError: GMAIL_ADDRESS` → 코드 자체는 정상이었고 서버 자동 재시작 타이밍 문제 → 완전히 껐다 켜서 해결
- `JSONDecodeError: Expecting value` → `webhook_log.json`이 빈 파일 상태 → `except` 절에 `JSONDecodeError` 추가로 해결

### 결과
- 로드맵 9~10주차 목표(Webhook + 조건 분기 + 이메일 연동) 달성
- 실제 Gmail로 알림 이메일 수신 확인 완료

### 다음 목표
- 11주차: Supabase로 데이터 저장 (2개월차 도구 중 하나에 기록 저장/조회 기능 추가)

## 3개월차 - 11~12주차 (Day 7): Supabase 연동 + 전체 파이프라인 완성

### 오늘 만든 것
- `day7_todo_db.py` — 기존 JSON 파일 저장 방식이던 todo 앱을 Supabase(실제 DB) 저장 방식으로 전환
  - Supabase의 `select`/`insert`/`update`/`delete`를 이용한 할일 추가, 조회, 완료 처리, 삭제
  - `.eq("id", task_id)` 조건으로 특정 할일만 수정하거나 삭제
  - `.order("id")`로 저장 순서에 맞춰 할일 목록 정렬
- `day7_pipeline.py` — 웹훅 수신부터 AI 요약, DB 저장, 이메일 알림까지 이어지는 전체 자동화 파이프라인
  - 웹훅으로 받은 내용을 `day4_summarizer.py`의 `summarize_text()`로 요약
  - 요약 결과를 Supabase `events` 테이블에 저장
  - Gmail SMTP로 요약 완료 이메일 알림 발송

### 배운 것
- **DB vs JSON 파일**: DB는 여러 요청이 동시에 들어와도 데이터를 더 안전하게 관리하고, 유저별 데이터를 분리하기 위해 필요하다
- **Supabase 기본 CRUD**: `.select()`/`.insert()`/`.update()`/`.delete()`로 테이블 데이터를 조회, 추가, 수정, 삭제한다. 테이블 결과는 딕셔너리 리스트와 비슷한 구조다
- **`.eq()` 조건의 중요성**: 조건 없이 `update`/`delete`를 실행하면 테이블 전체에 적용될 수 있으므로 대상 행을 반드시 지정해야 한다
- **`.order("id")`**: DB는 저장 순서를 보장하지 않으므로 원하는 순서가 있다면 명시적으로 정렬해야 한다
- **로컬 모듈 import**: `from day4_summarizer import summarize_text`처럼 직접 만든 파일의 함수를 다른 파일에서 재사용할 수 있다
- **HTTP 상태 코드와 포트 번호**: 400/500은 응답 결과를 나타내는 상태 코드이고, 465/5000은 요청이 향하는 포트 번호다
- **`MIMEText` 객체**: 이메일 본문과 헤더를 조립하는 객체로, `msg["Subject"] = ...`처럼 딕셔너리와 비슷한 문법을 사용한다
- **파이프라인의 부분 실패**: 이메일 발송만 실패해도 DB 저장은 이미 완료될 수 있어, 재시도 시 중복 저장이 발생할 수 있다. 단계별 예외 처리와 재시도 설계가 다음 과제다

### 막힌 점 / 해결
- `SUPABASE_URL`에 `/rest/v1`을 잘못 포함해 발생한 `Invalid path` 에러를 프로젝트 기본 URL로 수정
- `select()` 결과가 저장 순서와 다르게 나와 `.order("id")`를 추가
- 테이블 생성 직후 스키마 캐시가 갱신되지 않아 발생한 `PGRST204` 에러를 스키마 리로드로 해결
- Chrome 번역 기능과 Supabase 대시보드가 충돌해 발생한 `removeChild` 에러를 번역 기능 비활성화로 해결

### 결과
- 로드맵 11~12주차 목표(Supabase 데이터 저장 연동 및 전체 자동화 파이프라인) 달성
- **3개월차(흐름 자동화) 전체 완료**

### 다음 목표
- 4개월차 13주차: HTML/CSS + React 기초
- 결과물: 랜딩페이지 1개
