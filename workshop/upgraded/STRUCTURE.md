# upgraded 디렉터리 구조 설명

이 디렉터리는 legacy(`legacy`) 폴더의 전체 내용을 복사하여 최신화 및 리팩토링 작업을 진행하기 위한 공간입니다.

## 디렉터리 및 파일 구조

```
upgraded/
├── README.rst                # 프로젝트 및 사용법 설명서
├── distribute_setup.py       # distribute 설치 스크립트(레거시 패키징)
├── distribute-0.6.10.tar.gz  # distribute 패키지 소스
├── MANIFEST.in               # 패키징 시 포함 파일 명세
├── setup.py                  # setuptools 기반 설치 스크립트
├── docs/                     # Sphinx 기반 문서 디렉터리
│   ├── Makefile
│   ├── build/
│   │   ├── doctrees/
│   │   └── html/
│   └── source/
│       ├── conf.py
│       ├── changelog.rst
│       ├── example_usage.rst
│       ├── getting_started.rst
│       ├── index.rst
│       ├── other_uses.rst
│       └── _static/
│           └── default.css
├── guachi/                   # 주요 패키지 소스 코드
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── tests/
│       ├── test_configmapper.py
│       ├── test_configurations.py
│       ├── test_database.py
│       └── test_integration.py
├── guachi.egg-info/          # 패키지 메타데이터
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
└── .keep                     # 빈 디렉터리 유지를 위한 파일(필요시)
```

## 주요 구성 요소

- **guachi/**: 핵심 라이브러리 코드와 테스트 코드가 위치합니다.
- **docs/**: Sphinx 기반의 문서 소스와 빌드 결과물이 포함됩니다.
- **setup.py, MANIFEST.in, distribute_setup.py**: 레거시 Python 패키징 관련 파일입니다.
- **guachi.egg-info/**: 빌드 및 설치 시 생성되는 메타데이터 디렉터리입니다.
- **tests/**: `guachi/tests/` 하위에 유닛 테스트가 포함되어 있습니다.

> 이 구조는 레거시 코드를 Python 3 및 최신 패키징 표준에 맞게 점진적으로 업그레이드하기 위한 출발점입니다.
