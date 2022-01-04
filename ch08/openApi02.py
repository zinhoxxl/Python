# Open API
# ① http://developers.naver.com 싸이트 이동
# ② Naver API 사용 위해 Application 등록 수행
# ③ 사용 API에서 검색 서비스 선택(get / post 방식)
# ④ 파이썬 검색어로 검색하여 결과 JSON 확인

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제
# 네이버 검색 Open API 예제 - 블로그 검색

import requests
import pprint

headers = {
    'X-Naver-Client-Id' : 'D6E8zfH8Ief1IzvShb57' ,
    'X-Naver-Client-Secret' : '4IbYPU7R6F' ,
}

payLoad = {
    'query' : '스프링',
    'display' : 100,
}

url = 'https://openapi.naver.com/v1/search/blog' # json 결과

res = requests.get(url, headers=headers, params=payLoad)

print('request sended...')
#응답이 json 형태로 오기로 되어 있음
print(res.json())

# json Web Viewer -> jsonviewer.stack.hu(3번째 결과)
result = res.json()['items'][5]['title']
print('result 5번째 title만 가져옴')
print(result)