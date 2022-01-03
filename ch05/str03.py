u = 'spam and ham'
print(u.replace('spam','spam, egg'))   # replace()는 새로운 스트링을 생성함
u = 'spam and ham'
print(" u.split() "         , u.split())   # 공백으로 분리 (모든 공백 제거 및 문자열 내의 단어 리스트를 얻음
print(" u.split('and') "    , u.split('and'))   # 'and' 로 분리
