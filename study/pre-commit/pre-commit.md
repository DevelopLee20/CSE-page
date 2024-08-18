# pre-commit

[레퍼런스: pre-commit 공식문서](https://pre-commit.com/)

## pre-commit 이란?

- 코드를 커밋하기 전 간단한 문제 식별 가능
- 스테이징 되어있는 파일 기준으로 문제 식별
- PEP(파이썬 코드 규약), 세미콜론 누락, 디버그용 print() 자동 삭제 등등 기능 제공

## 설치 방법

> 기본적으로 파이썬이 설치되어있어야 함

```bash
pip install pre-commit
```

## 설치 확인

```bash
pre-commit --version
```

## 사전 커밋 구성하기

### 1. config 파일 생성

```bash
.pre-commit-config.yaml
```

> 파일 예시

```yaml
repos : 
- repo : https://github.com/pre-commit/pre-commit-hooks rev : v2.3.0 hooks : - id : check-yaml - id : end-of-file-fixer - id : trailing-whitespace - repo : https://github.com/psf/black rev : 22.10.0 hooks : - id : black 
    
```

### 2. 후크 추가

> 아래 url에 접속해 후크와 플러그인 설정하면 끝

[config 파일 플러그인 목록](https://pre-commit.com/#plugins)

[많이 사용되는 후크 모음](https://pre-commit.com/hooks.html)

## git hook 스크립트 파일 설치

```bash
pre-commit install
```

> 위의 플러그인을 자동 실행하도록 .git 파일에 추가 해줌

## 실행 명령어

```bash
pre-commit run --all-files
```

> 모든 파일에 대해 검사를 진행함
