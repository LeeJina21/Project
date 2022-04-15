def solution(answers):
    answer = []

    student1 = [1,2,3,4,5] #학생1
    student2 = [2,1,2,3,2,4,2,5] #학생2
    student3 = [3,3,1,1,2,2,4,4,5,5] #학생3


    results = {1:0, 2:0, 3:0} # Map 구조로 학생:맞춘 정답수 로 저장

    for i in range(len(answers)):
        if student1[i % len(student1)] == answers[i]: #len(student1) 배열 크기 5
            # 맞추면 정답 수 +1 하기
            results[1] += 1

        if student2[i % len(student2)] == answers[i]:
            # 맞추면 정답 수 +1 하기
            results[2] += 1

        if student3[i % len(student3)] == answers[i]:
            # 맞추면 정답 수 +1 하기
            results[3] += 1

    #가장 높은 점수 구하기
    #results 구조의 값 중 가장 큰 숫자 가져오기
    top_score = max(results.values())

    answers=[]

    #학생은 3명이고 학생번호는 1번부터라 range(1,4)선언
    for i in range(1,4):
        if results[i]== top_score:
            answer.append(i)

    return answer