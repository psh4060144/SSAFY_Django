`

django-admin startproject mypjt

cd mypjt

python manage.py startapp articles

`

### 1. Model 만들기 (Data 정의)

    (aritcles/models.py)

- Article (title, content, created_at, updated_at)

- makemigrations, migrate(모델 변경사항 DB 적용)

- Admin page 설정(createsuper 도 해주세요..)

### 2. 기본설정 (templates)

- Templates (껍데기만)
  
  - 템플릿 경로 (app/templates)
    
    `app/templates` 가 기본경로, 명확한 구분을 위해서 {appname}/ 경로를 추가
  
  - 템플릿 상속 (BASE_DIR/'templates', settings.py > TEMPLATES > DIRS 에도 설정)
  
  - 필요한 화면
    
    - 게시글 목록 (index.html)
    
    - 게시글 작성(create.html)
    
    - 게시글 수정(update.html)
    
    - 게시글 상세(detail.html)

### 3. URL

- url 정의 및 view 함수 정의(껍데기만)
  
  - 게시글 목록보기 (/articles/), views > index()
  
  - 게시글 작성하기 (/articles/create/) create()
    
    - GET : 작성화면 출력
    
    - POST : DB에 저장
  
  - 게시글 상세보기 (/articles/{게시글번호}/) views > detail()
  
  - 게시글 수정하기 (/articles/{게시글번호}/update/) views > update ()
    
    - GET : 게시글 수정화면 출력
    
    - POST : DB 저장
  
  - 게시글 삭제하기 (/articles/{게시글 번호}/delete/) views > delete()

- url naming
  
  - url에 이름을 지정하고, 그 이름으로 url 가져다 쓰기 
    
    /article/create/     >>> 'create'
    
    url 이름이 app 마다 겹칠 수 있으니까...name space를 생성(app_name)
  
  - url 앱 분배 (include, app에 urls.py 만들기)

- variable routing

### 4. Model Form

- ArticleForm

### 5. View 함수, 템플릿 내용채우기
