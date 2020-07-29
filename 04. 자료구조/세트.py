# 집합 (set)
# 중복안됨 순서없음
s={1,2,3,3,3}
print(s) #{1,2,3}

java={"김", "도", "건"}
python={"박", "도", "건"}

#교집합(java python 둘다 있는거)
print(java & python) #{'도', '건'}
print(java.intersection(python)) #{'도', '건'}

#합집합(java python 둘중 하나라도 있는거)
print(java|python)  #{'도', '박', '건', '김'}
print(java.union(python)) #{'도', '박', '건', '김'}

#차집합(java 에는 있으나 python 에는 없느거)
print(java - python)
print(java.difference(python))

#추가
java.add("오")
print(java) #{'김', '도', '건', '오'}

#제거
java.remove("오")
print(java) #{'김', '도', '건'}