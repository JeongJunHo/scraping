import urllib.request

url = "https://www.google.co.kr/"

# 다운로드
mem = urllib.request.urlopen(url).read()

print(mem.decode("euc-kr"))
# 그냥 실행하면 binary 파일로 읽혀진다.
# 디코드를 원한다면 인코딩 방식에 맞게 디코드를 진행