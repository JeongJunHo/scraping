import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
mem = urllib.request.urlopen(url).read()
# mode wb(write binary) 반대 개념 텍스트
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")

# url - url 경로 , savename - 어디에 저장할 것인지
# 아래 코드는 바로 저장이 된다.
# urllib.request.urlretrieve(url, savename)

# 위아래 코드 모두 이미지를 가져오는 코드이다. 추가 작업이 필요하다면 위의 코드를 사용