# Think Mate (씽크메이트)

영업 큐레이터를 위한 AI 기반 장소 추천 및 활동 관리 앱

## 기능

- 🏠 **홈 화면**: 대시보드, 달성 현황, 일정 관리
- 📍 **AI 추천**: 유동인구 기반 핫스팟 추천
- 💬 **챗봇**: 대화형 활동 결과 입력
- 👤 **마이페이지**: 활동 이력 관리

## 로컬에서 확인하기

`index.html` 파일을 브라우저에서 열면 바로 확인할 수 있습니다:

```bash
open index.html
```

또는 간단한 로컬 서버 실행:
```bash
python -m http.server 8000
```

브라우저에서 http://localhost:8000 접속

## 주요 특징

- 모바일 최적화 디자인 (max-width: 420px)
- 4060 타겟을 위한 큰 글씨 및 고대비 UI
- 직관적인 대화형 인터페이스
- 실시간 활동 기록 및 통계 (localStorage 사용)
- 프리미엄 디자인 (그라데이션, 애니메이션, glassmorphism)

## 기술 스택

- **HTML5**: 시맨틱 마크업
- **CSS3**: 그라데이션, 애니메이션, 반응형 디자인
- **Vanilla JavaScript**: 순수 자바스크립트로 상태 관리
- **localStorage**: 클라이언트 측 데이터 저장

## 🌐 Netlify 배포 방법

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

### 3. 배포 완료!
몇 초 후 자동 배포됩니다.
URL: `https://[your-site-name].netlify.app`

### 특징:
- ✅ **즉시 배포** - 빌드 없이 바로 배포
- ✅ **무료** - Netlify Free 플랜 사용 가능
- ✅ **자동 배포** - GitHub push 시 자동 재배포
- ✅ **HTTPS** - 무료 SSL 인증서 제공
- ✅ **모바일 최적화** - 420px 반응형 디자인

## 📦 파일 구조
```
thinkmate/
├── index.html         # 메인 HTML 파일
├── netlify.toml       # Netlify 배포 설정
├── .gitignore         # Git 제외 파일
└── README.md          # 문서
```

## 사용 흐름

1. **홈** → AI 장소 추천 클릭
2. **추천 페이지** → 장소 선택 → 카카오내비 출발
3. **챗봇** → 활동 결과 입력 (리드, 계약)
4. **마이페이지** → 저장된 활동 이력 확인
