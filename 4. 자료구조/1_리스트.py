#리스트 []
a=[1, 2, 3]
print(a) #[1, 2, 3]

s=["김", "도", "건"]
print(s) #['김', '도', '건']
print(s.index("건")) #2
s.append("신") #s에 신 추가
s.insert(3, "병") #s 4번째에 병 추가
print(s) #['김', '도', '건', '병', '신']
print(s.pop()) #맨 뒷 제거
print(s) #['김', '도', '건', '병']
print(s.count("김")) #김 갯수 확인   1

d=[3, 2, 4, 1]
d.sort() #정렬
print(d) #[1, 2, 3, 4]
d.reverse() #뒤집기
d.clear() #전체 지우기

f=["asdf", 2, True]
f.extend(d) #f 에 d 합치기
print(f)
