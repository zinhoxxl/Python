# continue문을 이용하여 1~100 까지의 짝수만 출력
for i in range(1,101):
    if i%2==1:
        continue
    print('짝수=',i)
