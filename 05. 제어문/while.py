'''
# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index)) # format 에서 customer이 {0} , index가 {2}.
    index -= 1 # -= 1은 1을 뺴는것, index 값이 다 빠지면 while 문을 빠져나감.
    if index == 0: # index 값이 0으로 다 빠져나감.
        print("커피는 폐기처분 되었습니다.")

        # 다만 모든 커피숍에서 이렇게 까지는 하지 않음.
'''

customer = " 아이언맨 "
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회.".format(customer, index))
    index +=1