#코테 가장 큰 수
def solution(numbers):

    print(type(numbers))
    print(type(numbers[0]))

    numbers = list(map(str,numbers))

    print(type(numbers))
    print(type(numbers[0]))

    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))