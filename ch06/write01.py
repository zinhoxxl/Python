# 사용자가 입력한 내용을 파일로 저장 - write() 함수

text = input('파일에 저장할 내용을 입력하세요 : ')
# f = open('data.txt', 'w')
f = open('data.txt', 'w', encoding='utf-8')
f.write(text)
f.close()

# with open() as 는 파일처리가 끝나면 자동으로 파일을 닫아 준다.(close() 함수 생략 가능)
# with open('data.txt', 'w', encoding='utf-8') as f:
#     f.write(text)
