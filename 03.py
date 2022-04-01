def solution(clothes):
    clothesTypeMap={}

    for clothe, clothesType in clothes:

        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

    answer = 1
    for clothesType in clothesTypeMap:
        answer *= (clothesTypeMap[clothesType] + 1)
    return answer-1