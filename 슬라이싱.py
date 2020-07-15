#파이썬은 0부터 센다
rlaehrjs = "040406-3456789"
print("성별 :" + rlaehrjs[7]) #3
print("년 :" + rlaehrjs[0:2]) #04
print("월 :" + rlaehrjs[2:4]) #04
print("일 :" + rlaehrjs[4:6]) #06
print("생년월일 :" + rlaehrjs[:6]) #040406
print("뒷자리 :" + rlaehrjs[7:]) #3456789
print("뒷자리 (뒤에서 부터):" + rlaehrjs[-7:]) #3456789