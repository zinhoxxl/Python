# Yesterday.txt를 읽어 해석하는 PGM
# 네이버 검색 Open API 예제 - 블로그 검색
# 파파고 SMT API 예제
# 과제 : 1) Yesterday.txt 파일을 읽기
#        2) 한 라인씩 읽고 원문 한라인, 해석된 한 라인 씩
#           전체문장을 해석 YesterdayTrans.txt에 저장

from requests import Request
from requests import Session

s = Session()

# ID와 비밀 Key Setting
headers = {
    'X-Naver-Client-Id' : 'D6E8zfH8Ief1IzvShb57' ,
    'X-Naver-Client-Secret' : '4IbYPU7R6F' ,
}

# 문장번역 URL 지정
url = "https://openapi.naver.com/v1/papago/n2mt"

# 문장번역 누적 변수
totalText = ''
with open('Yesterday.txt','r') as readFile:
    sourceText = 'Start..'   # 초기화된 값을 설정, 일단 시작할수 있도록...

    while sourceText != '':   # readline()함수는 파일의 끝에 도달하면 ''를 반환함
        #print(line, end='')
        sourceText = readFile.readline()
        payLoad = {
            'source': 'en',
            'target': 'ko',
            'Yesterday.txt': r,
        }