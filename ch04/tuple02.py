t = (1,2,3)
print("len(t) -> ", len(t))

print("t[0] ->", t[0])
print(t[-1])
print("t[0:2] ->", t[0:2])
print("t[::2] ->", t[::2])

t[1] = 7  # 읽기 전용이라 수정하려 하면 에러남
