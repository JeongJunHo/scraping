# IMAGE SCRAPING

> 본 실습은 docker 환경에서 진행됩니다. 
>
> repository 내의 docker directory의 명령어를 참고해주세요.

## 실습

### miniconda3 설치

```dockerfile
docker pull continuumio/miniconda3
```

### miniconda3 실행

```dockerfile
docker run -i -t continuumio/miniconda3 /bin/bash
```

### python 사용

```python
python3 -c "print(3*5)"
# 결과 15
```

 -c는 인터프리터 모드이다 즉각 결과를 반환해준다.

-i는 대화형 모드이다. ctrl + d



한번 생성된 이미지 내에서는 어떤 수정을 해도 반영되지않는다.

이미지 수정를 수정 해보자.

### 미니콘다 이미지 내 모듈 설치

beautifulsoup 설치

```
pip install beautifulsoup4
```

requests 설치

```
pip install requests
```

이미지 종료

```
exit
```

### 이미지 수정

컨테이너 실행 기록을 확인합니다.

```dockerfile
docker ps -a
```

![docker ps -a](D:/study/docker/img/ps.PNG)

현재 상태를 이미지에 저장하고자 하는 container id를 찾아 커밋합니다.

```dockerfile
 docker commit 88f0c1d7dd90 mlearn:init
```

커밋 한 이후 부터는 해당 이미지를 실행할 때 명명했던 이미지 네임을 사용합니다.

```dockerfile
docker run -i -t mlearn:init
```

docker 이미지는 모두 독립된 환경이기 때문에 코드를 입력하기 위해서는 내부에서 따로 코드를 입력해야 하지만 vi 편집기등 편집기를 따로 설치해야한다.

불편하기 때문에 홈폴더를 마운트 하는법을 배워보자.

윈도우로 돌아와 원하는 곳에 마운트할 폴더를 만든 후 파일을 채워 넣는다.

image를 빠져나온 후 폴더 마운트한 이미지를 실행한다.

```dockerfile
exit
docker run -i -t -v /d/sample:/sample mlearn:init
```

-v 옵션을 사용하여 마운트 할 수 있으며 이후 한칸 띄고 로컬폴더의 경로를 입력 후 :를 입력하고 독립 컨테이너상의 새로 위치할 폴더의 경로를 입력한다.

이미지 실행 후 현재 위치에서 파일 검색을 해보면 마운트한 폴더가 생성된 걸 확인 할 수 있다.

```dockerfile
ls -l
```

### beautify

```python
import urllib.request
```

python request 라이브러리로 url에 접근해 img, html 파일을 받아올 수 있다.

```python
import urllib.parse
```

한글입력을 처리하기위해 urlencode를 사용하기 위한 라이브러리

### url 접속 예제 코드

```python
import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "where": "nexearch",
    "sm": "top_hty",
    "fbm": "",
    "ie": "utf8",
    "query": "초콜릿"
}
params = urllib.parse.urlencode(values)
url = api + "?" + params

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") # euc-kr 또는 utf-8로 테스트해볼 것
print(text) 
```

### beautify 태그 선택 예제 코드

```python
from bs4 import BeautifulSoup
# 태그 선택자
"ul"
"div"
"li"
# 아이디 선택자
"#<아이디>"
# 클래스 선택자
".<클래스>"
# 여러개의 클래스
".<클래스>.<클래스>.<클래스>"
# 후손 선택자
"#meigen li"
# 자식 선택자
"ul.items > li"

html = """
    <html>
        <body>
            <div id="meigen">
                <h1>위키북스 도서</h1>
                <ul class="items art it book">
                    <li>a</li>
                    <li>b</li>
                    <li>c</li>
                </ul>
            </div>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
header = soup.select_one("div#meigen > h1") # 요소
list_items = soup.select("ul.items > li") # 요소의 배열

print(header.string)
print(soup.select_one("ul").attrs)

for li in list_items:
    print(li.string)
```

