'''
------------------------------------------
https://biago.ga/
2020 비아고등학교 프로그래밍 동아리(파이썬)
주제: 함수
------------------------------------------
'''
 
def open_account():
    print('새로운 계좌가 생성되었습니다!')

def deposit(balance, money):    #입금
    print('입금이 완료되었습니다. 잔액은 {0} 원 입니다.'.format(balance + money))
    return balance + money

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)
