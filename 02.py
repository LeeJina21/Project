def solution(phone_book):
    # 문자열의 값에 따라 정렬
    phone_book.sort()

    # 출력 결과
    answer = True

    #반복 횟수
    phone_length = len(phone_book)

    # 기준이 되는 변호이며, 마지막까지 반복할 필요가 없어 마지막 전까지 반복
    for i in range(phone_length-1):

        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False # 맞으면 false로 변경

            break


    return answer