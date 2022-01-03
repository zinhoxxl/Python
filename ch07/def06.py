# 기본값 매개변수(Default Argument Value)

# 기본값 매개변수 cnt=1 로 정의
def str(text, cnt=1):
    for i in range(cnt):    # i=0~2까지 3번 loop가 돌아감
        print(text)

# 함수를 호출할때 2번째 매개변수를 생략하면 기본값 매개변수 cnt=1이 사용됨
str('안녕하세요 기본')
print()

str('안녕하세요3', 3)
