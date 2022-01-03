# 가변 매개변수(Arbitrary Argument List)
# 입력 개수가 달라질 수 있는 매개변수
# *를 이용하여 정의된 가변 매개변수는 튜플로 처리

# 매개변수 앞에  *를 붙이면 해당 매개변수는 가변매개변수로 지정됨
# def 함수이름(*매개변수):
def merge_string(*text):
    result=''
    print('type(text')