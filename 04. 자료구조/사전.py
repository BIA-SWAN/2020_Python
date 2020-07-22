#사전 {}
a={1:"김", 2:"도"} #1,2 는 key "김", "도" 는 value
print(a[1]) #김
print(a.get(3)) #none
print(a.get(3, "건")) #건
print(1 in a) #a안에 1이  있는가    True

#추가,교체,제거
a[1] = "박" #1을 "박" 으로 교체
a[3] = "건" #3:"건" 추가
print(a) 
del a[2] #2:"도" 제거
print(a)

print(a.keys()) #1, 3
print(a.values()) #박 건
a.clear() #전체 제거