'''
----------------------------------------
https://biago.ga/
2020 비아고등학교 프로그래밍 동아리 ( 파이썬 )
주제 : 연산자 ( 2020.07.08 )
Made By KimJei.
-----------------------------------------
'''

print(2 + 3 * 4) # 14
print((2 + 3) *4) #20 ( 가로를 통하여 계산 가능 )

number = 2 + 3 * 4 # 14 ( 복합 연산 가능. ) ( 해당 number은 함수로 표현 )
print(number)
number = number + 2 # 16 # 넘버를 14로 인식하였기 떄문
print(number)

number += 2 # 18 number = number + 2 명령어와 똑같이 표현, 간단하게 사용 가능.
print(number)

number *= 2 # 36
print(number)

number /= 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 5 # 1 ( %은 나머지를 표시하기 떄문에 나머지가 0임 )
print(number)