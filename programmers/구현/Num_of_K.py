def solution(i, j, k):
    answer = 0
    # i부터 j까지
    for n in range(i,j+1):
        # n을 문자열로 바꾸고
        num = str(n)
        # num에 k의 개수를 더해준다
        answer += num.count(str(k))
    # k의 총 개수를 반환
    return answer