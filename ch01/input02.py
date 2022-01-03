n1=input(' 첫번째 숫자를 입력해 주세요?')
n2=input(' 두번째 숫자를 입력해 주세요?')

# sum 합계금액을 구한다
# int -> 문자를 숫자로 바꾸어 준다
sum1 = int(n1) + int(n2)

# 문자열로 인식하면 그냥 붙여준다
sum2 = n1 + n2

print('SUM1->', sum1)
print('SUM2->', sum2)
