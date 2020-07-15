jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("언 : " + jumin[0:2]) # 0 부터 2 직전까지 ( 0 , 2 )
print("월 : " + jumin[2:4])
print("일 " + jumin[4:6])

print("생년월일 : " + jumin[0:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:14]) # 7부터 끝까지
print("뒤 7자리 ( 뒤에부터) : " + jumin[-7:])
# 맨 뒤에서부터 7번쨰부터 끝까지