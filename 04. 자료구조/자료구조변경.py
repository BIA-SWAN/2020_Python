#자료구조를 변경가능 ex)list를 set로 바꿈

a={"김", "도", "건"}
print(a type(a)) #type 은 지금 자료구조를 보여줌

a=list(a) #a의 자료구조를 list로 바꿈
a=tuple(a) #a의 자료구조를 tuple로 바꿈
a=set(a) #a의 자료구조를 set로 바꿈