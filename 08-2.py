import math
# 입력받은 숫자가 소수인지 판별
# 소수 : true | 소수 아니면 : false
def numberCheck(num):
    # 0.1소수 아님
    if num == 0 or num ==1:
        return False
    else:
        # 2부터 입력받은 숫자의 제곱근까지 반복
        # 입력받은 값이 10이면 10^2 100번 반복
        # 그러나 100은 2의 배수로 반복 1번하고 종료됨
        for i in range(2, int(math.sqrt(num)) + 1):
            print(i)
            # 입력받은 값이 2부터 시작해서 나눠 떨어지는지 체크
            if num % i == 0:
                return False
    return True
# 10은 1번만 반복하면 결과 나옴
print(numberCheck(10))

# 값의 크기가 커질수록연산의 범위가 증가됨
# 238번 반복 달성
print(numberCheck(1111111))

