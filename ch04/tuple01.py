# Tuple은 List의 Read Only
# range : List나 Tuple를 사용, 저장하지 않더라도 특정범위의
#          숫자 시퀀스 생성
# range(start,stop,step)

L = range(10) # 0,1,2,3,4,5,6,7,8,9
print (L)

A = L[::2]
print ("L[::2] -> ", L[::2])  # start : end : jump

for aa in A:
    print('A-> ', aa)
