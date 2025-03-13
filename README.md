# 🍽️ 뭐 먹지? - AI 기반 요리 추천 서비스

## 📌 프로젝트 발표 자료 링크
[📄 pdf](https://github.com/your-repo-name/path/to/your-pdf.pdf)

## 📌 프로젝트 개요
**"뭐 먹지?"** 프로젝트는 사용자가 입력한 재료를 기반으로 AI가 적절한 요리를 추천해주는 **AI 기반 요리 추천 서비스**입니다.
이 프로젝트는 **Google Generative AI API**와 **Streamlit 웹 애플리케이션**을 활용하여 개발되었습니다.

**프로젝트 목표:**
- 냉장고 속 재료를 입력하면 AI가 적절한 요리를 추천
- 만개의 레시피 유튜브 채널 및 검색 링크 제공
- AI가 자연스러운 대화로 요리 추천
- 간단한 3단계 요리법 제공

---

## 🕒 개발 히스토리
- 📌 **최초 작성:** 2024년 1월 28일
- 📌 **업데이트:** 2025년 3월 (GitHub 공유 및 문서화 추가)
- 📌 **Streamlit 기반 웹 애플리케이션으로 변환**
- 📌 **Google Generative AI API 적용**

---

## 📂 프로젝트 폴더 구조
```
📂 __pycache__                   # Python 캐시 파일
📂 .streamlit                   # Streamlit 설정 파일
 ├── secrets.toml              # API Key 보관 파일 (gitignore 대상)
📂 .venv                        # 가상환경 폴더
📄 Cooking.csv                  # 요리 데이터셋 (재료 기반 레시피 매칭)
📄 gitignore.txt                 # Git 무시 파일 목록
📄 requirements.txt              # 프로젝트 종속성 목록
📄 뭐 먹지 발표 자료.pdf          # 프로젝트 발표 자료
📄 momeokji_app.py               # Streamlit 기반 메인 애플리케이션
📄 tools.py                      # 요리 추천 로직 구현
📄 README.md                     # 프로젝트 설명 파일
```

---

## 🛠 주요 기능
### 1️⃣ AI 기반 요리 추천 (momeokji_app.py)
- 사용자가 입력한 재료를 분석하여 적절한 요리를 추천
- AI를 이용해 자연스러운 대화 및 요리법 안내
- 유튜브 레시피 검색 링크 제공

### 2️⃣ 요리 데이터 분석 및 매칭 (tools.py)
- Cooking.csv 파일을 기반으로 요리와 재료를 매칭
- AI 없이도 간단한 추천이 가능하도록 로직 설계
- Pandas를 활용하여 데이터 가공 및 필터링

---

## 🎨 Streamlit UI
1. **사용자 입력:** 재료를 쉼표(,)로 구분하여 입력
2. **AI 응답:** 입력된 재료를 기반으로 AI가 요리를 추천
3. **요리법 제공:** 3단계 간략 조리법을 안내
4. **유튜브 검색 링크:** 해당 요리의 유튜브 검색 결과를 제공

---

## 📊 실행 방법
### 📌 Streamlit 웹 애플리케이션 실행
```bash
streamlit run momeokji_app.py
```

### 📌 로컬 환경 설정
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화 (Windows)
source .venv/Scripts/activate

# 패키지 설치
pip install -r requirements.txt
```

---

## 📜 요구사항 (requirements.txt)
```
numpy
pandas
google-generativeai
streamlit
watchdog
```

---

## 🛑 Git 무시 목록 (gitignore.txt)
```
.streamlit/secrets.toml
__pycache__
```

---

## 🚀 마무리
이 프로젝트는 **AI & Machine Learning, Data Science & Visualization, Learning & Experiments** 카테고리에 해당합니다.

📌 향후 개선 사항:
- 요리 추천 알고리즘 고도화 (ML 활용 가능성 검토)
- 사용자 맞춤형 레시피 추천 기능 추가
- 더 많은 요리 데이터셋 활용하여 다양성 확보

