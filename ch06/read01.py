f = open('data.txt', 'r', encoding='utf-8')  # data.txt 파일을 일기모드로 열기
data = f.read()                              # data.txt 의 모든 내용을 한꺼번에 읽어온다.
print(data)
f.close()
