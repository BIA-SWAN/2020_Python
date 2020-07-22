try:
    print("/ / 나눗셈 전용 계산기 입니다 / / ")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    print("{0} ÷ {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력받았어요. 정수만 입력해주세요!!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print('알 수 없는 오류가 발생했어요 :(')
    print(err)