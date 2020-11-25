def Fosc() :
    global c
    global f
    c=int(input("섭씨온도를 입력해주세요:"))
    f=int((c*9/5)+32)

Fosc()
print("섭씨", c, "도는 화씨", f, "도 입니다.")