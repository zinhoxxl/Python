# 1~n 까지 합을 구하는 프로그램
# 1~n까지 합을 구해주는 함수
def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print('1~3 까지의 합 = ',sum(3))
print('1~10 까지의 합 = ',sum(10))
print('1~20 까지의 합 = ',sum(20))


# 강사님 코드
def sum(n):
    total = 0
    for i in range(1, n + 1):
        sum = sum + i

    print('1~{}까지의 합 = {}'.format(n, sum))

# 함수호출
sum(3)
sum(10)
sum(20)