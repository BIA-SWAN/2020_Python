animal = "강아지" 
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집 " + animal + "의 이름은 " + name + "에요")
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 매우 좋아해요")
print(name, "는", age , "살이며, ",hobby,"을 매우 좋아해요.") # + 커맨드 대신 , 로 표기 가능.
print(name + " 어른일까요? " + str(is_adult))