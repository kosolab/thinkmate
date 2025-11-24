# Think Mate (씽크메이트) - Streamlit 버전

영업 큐레이터를 위한 AI 기반 장소 추천 및 활동 관리 앱

## 기능

- 🏠 **홈 화면**: 대시보드, 달성 현황, 일정 관리
- 📍 **AI 추천**: 유동인구 기반 핫스팟 추천
- 💬 **챗봇**: 대화형 활동 결과 입력
- 👤 **마이페이지**: 활동 이력 관리

## 설치 및 실행

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 앱 실행
```bash
streamlit run app.py
```

### 3. 브라우저에서 확인
- 자동으로 브라우저가 열립니다 (기본: http://localhost:8501)
- 모바일 뷰를 원하시면 브라우저 개발자 도구(F12)에서 모바일 모드로 전환하세요

## 사용 흐름

1. **홈** → AI 장소 추천 클릭
2. **추천 페이지** → 장소 선택 → 카카오내비 출발
3. **챗봇** → 활동 결과 입력 (리드, 계약)
4. **마이페이지** → 저장된 활동 이력 확인

## 주요 특징

- 모바일 최적화 디자인 (max-width: 420px)
- 4060 타겟을 위한 큰 글씨 및 고대비 UI
- 직관적인 대화형 인터페이스
- 실시간 활동 기록 및 통계

## 기술 스택

- **Streamlit**: 웹 앱 프레임워크
- **Python**: 백엔드 로직
- **Custom CSS**: 모바일 앱 스타일링

## 🚀 Streamlit Cloud 배포 방법

### 1. Streamlit Cloud 가입
- https://share.streamlit.io/ 방문
- GitHub 계정으로 로그인

### 2. 새 앱 배포
- "New app" 버튼 클릭
- Repository: `kosolab/thinkmate`
- Branch: `main`
- Main file path: `app.py`
- "Deploy!" 클릭

### 3. 배포 완료!
몇 분 후 앱이 자동으로 배포됩니다.
URL: `https://[your-app-name].streamlit.app`

## 📦 배포 파일 구조
```
thinkmate/
├── index.html            # 정적 HTML 버전 (Netlify용)
├── netlify.toml          # Netlify 배포 설정
├── app.py                # Streamlit 버전
├── requirements.txt      # Python 패키지
├── .python-version       # Python 버전 (3.9)
├── .streamlit/
│   └── config.toml       # Streamlit 설정
└── README.md             # 문서
```

## 🌐 Netlify 배포 방법 (정적 HTML 버전)

### 1. Netlify 가입
- https://www.netlify.com/ 방문
- GitHub 계정으로 로그인

### 2. 새 사이트 배포
- "Add new site" → "Import an existing project" 클릭
- "Deploy with GitHub" 선택
- Repository: `kosolab/thinkmate` 선택
- Branch: `main`
- Build settings는 기본값 사용
- "Deploy site" 클릭

### 3. 배포 완료! 🎉
몇 초 후 자동 배포됩니다.
URL: `https://[your-site-name].netlify.app`

### 💡 특징:
- ✅ **즉시 배포** - 빌드 없이 바로 배포
- ✅ **무료** - Netlify Free 플랜 사용 가능
- ✅ **자동 배포** - GitHub push 시 자동 재배포
- ✅ **HTTPS** - 무료 SSL 인증서 제공
- ✅ **모바일 최적화** - 420px 반응형 디자인
