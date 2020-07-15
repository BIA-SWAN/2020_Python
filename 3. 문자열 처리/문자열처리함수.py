python = "Python is Amazing"
print(python.lower()) #모두 소문자로 출력
print(python.upper()) #모두 대문자로 출력
print(python[0].isupper()) #첫번째가 대문자인가
print(len(python)) #문자열 python의 길이
print(python.replace("Python", "Java")) #문자열 python속 Python을 Java로 대체
index = python.index("n") #변수 index의 첫번째 n의 위치
print(index) #5
index = python.index("n", index + 1) #변수 index의 두번째 n의 위치
print(index) #15
print(python.find("java")) #변수 python속 java가 있는가 없으면 -1을 출력
print(python.count("n")) #변수 python속 n의 갯수
