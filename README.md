# 🎯 Django 소모임 프로젝트

> 취미와 관심사를 공유하는 소모임 관리 웹 애플리케이션

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 프로젝트 소개

**Django 소모임 프로젝트**는 다양한 취미와 관심사를 가진 사람들이 모임을 만들고 참여할 수 있는 웹 플랫폼입니다. 
사용자는 자신의 관심사에 맞는 모임을 찾아 참여하거나, 새로운 모임을 개설하여 같은 취미를 가진 사람들과 소통할 수 있습니다.

## ✨ 주요 기능

### 👥 회원 관리
- **회원가입/로그인**: 개인정보 기반 계정 생성
- **프로필 관리**: 개인 정보 및 관심사 설정
- **계정 타입**: 학생, 강사, 관리자 구분

### 🎭 모임 관리
- **모임 검색**: 관심사별, 키워드별 모임 검색
- **모임 생성**: 새로운 소모임 개설
- **모임 참여**: 관심있는 모임 신청 및 참여
- **카테고리별 분류**: 운동/스포츠, 스터디, 취미/여가, 문화/예술

### 📝 게시판 시스템
- **모임별 게시판**: 각 모임마다 전용 게시판
- **카테고리 분류**: 공지사항, 후기, 일반 게시글
- **게시글 작성/수정**: 리치 텍스트 에디터 지원

### 📅 출석 관리
- **출석 체크**: 모임 참석 여부 기록
- **출석 통계**: 개인별 출석률 관리
- **출석 현황**: 모임별 출석 현황 조회

## 🛠️ 기술 스택

### Backend
- **Django 4.2+**: Python 웹 프레임워크
- **Python 3.8+**: 프로그래밍 언어
- **MySQL**: 관계형 데이터베이스

### Frontend
- **HTML5/CSS3**: 마크업 및 스타일링
- **Bootstrap 5**: 반응형 UI 프레임워크
- **JavaScript**: 클라이언트 사이드 인터랙션
- **Font Awesome**: 아이콘 라이브러리

### 개발 도구
- **Git**: 버전 관리
- **MySQL Workbench**: 데이터베이스 관리
- **VSCode**: 통합 개발 환경

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/LeeJaeHaeng/meeting_project.git
cd meeting_project
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. 의존성 설치
```bash
pip install django mysqlclient
```

### 4. 데이터베이스 설정
MySQL에서 `meeting_db` 데이터베이스를 생성하고, `settings.py`에서 데이터베이스 연결 정보를 수정:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meeting_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. 마이그레이션 실행
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 관리자 계정 생성 (선택사항)
```bash
python manage.py createsuperuser
```

### 7. 서버 실행
```bash
python manage.py runserver
```

🌐 **브라우저에서 http://127.0.0.1:8000 접속**

## 📁 프로젝트 구조

```
meeting_project/
├── manage.py                    # Django 관리 스크립트
├── meeting_project/             # 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py             # 프로젝트 설정
│   ├── urls.py                 # URL 라우팅
│   ├── wsgi.py                 # WSGI 설정
│   └── asgi.py                 # ASGI 설정
├── meeting_app/                 # 메인 애플리케이션
│   ├── models.py               # 데이터 모델
│   ├── views.py                # 뷰 함수
│   ├── forms.py                # 폼 클래스
│   ├── urls.py                 # 앱 URL 패턴
│   ├── admin.py                # 관리자 페이지
│   ├── context_processors.py   # 템플릿 컨텍스트
│   └── migrations/             # 데이터베이스 마이그레이션
├── templates/                   # HTML 템플릿
│   ├── base.html               # 기본 템플릿
│   ├── login.html              # 로그인 페이지
│   ├── register.html           # 회원가입 페이지
│   ├── class_search.html       # 모임 검색 페이지
│   ├── post_list.html          # 게시글 목록
│   ├── post_detail.html        # 게시글 상세
│   ├── post_create.html        # 게시글 작성
│   ├── mypage.html             # 마이페이지
│   └── attendance.html         # 출석 관리
└── static/                      # 정적 파일
    ├── css/                    # 스타일시트
    ├── js/                     # JavaScript
    └── images/                 # 이미지
```

## 📊 데이터베이스 구조

### 주요 테이블
- **Member**: 회원 정보
- **Interests**: 관심사 카테고리
- **Class**: 소모임 정보
- **Post**: 게시글
- **Sugang**: 모임 참여 정보
- **Attendance**: 출석 기록
- **MemberInterests**: 회원-관심사 연결

## 🎮 사용 방법

### 1. 회원가입 및 로그인
1. 메인 페이지에서 "회원가입" 클릭
2. 필요한 정보 입력 후 계정 생성
3. 로그인하여 서비스 이용

### 2. 모임 찾기 및 참여
1. "모임 찾기"에서 관심사별 검색
2. 원하는 모임 선택 후 "참여하기" 클릭
3. 모임 게시판에서 다른 멤버들과 소통

### 3. 새 모임 만들기
1. 관리자 페이지에서 새 모임 생성
2. 모임 정보 및 관심사 설정
3. 멤버 모집 및 활동 시작

### 4. 게시글 작성
1. 참여 중인 모임의 게시판 접속
2. "글쓰기" 버튼 클릭
3. 카테고리 선택 후 게시글 작성

## 🔧 개발 환경 설정

### 샘플 데이터 생성
```bash
python manage.py shell
```

```python
from meeting_app.models import *
from datetime import date

# 관심사 생성
interests = ['테니스', '영어회화', '요리', '독서', '프로그래밍']
for name in interests:
    Interests.objects.get_or_create(interestName=name)

# 샘플 회원 생성
Member.objects.get_or_create(
    accountID='testuser',
    defaults={
        'password': 'test123',
        'name': '테스트유저',
        'phoneNum': '010-1234-5678',
        'email': 'test@example.com',
        'birth': date(1990, 1, 1)
    }
)
```

## 🤝 기여하기

1. 이 저장소를 Fork
2. 새로운 기능 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 👤 개발자

**이재행 (LeeJaeHaeng)**
- GitHub: [@LeeJaeHaeng](https://github.com/LeeJaeHaeng)
- 프로젝트 링크: [https://github.com/LeeJaeHaeng/meeting_project](https://github.com/LeeJaeHaeng/meeting_project)

## 🙏 감사의 말

- Django 프레임워크 개발팀
- Bootstrap 개발팀
- Font Awesome 팀
- 모든 오픈소스 기여자들

---
