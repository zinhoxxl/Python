s1 = 'i like programming, i like swimming.'
print("s1                            ", s1)
print("s1.count('like')              ", s1.count('like'))     # 'like' 문자열이 출현한 횟수를 반환
print("s1.find('like')               ", s1.find('like'))      # 'like' 의 첫글자 위치 (offset)를 반환
print("s1.find('programming')        ", s1.find('programming'))   # 'programming'의 첫글자 위치를 반환
print("s1.find('like', 3)            ", s1.find('like', 3))
print("s1.find('my')                 ", s1.find('my'))  # 'my' 단어는 없기 때문에 -1 반환
