# Runtime Exception

class big_number_error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("<한 자리 숫자 나누기 전용 계산기입니다.>")
    num1 = int(input("첫 번재 숫자를 입력하세요 : "))
    num2 = int(input("두 번재 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise big_number_error("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except big_number_error as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)