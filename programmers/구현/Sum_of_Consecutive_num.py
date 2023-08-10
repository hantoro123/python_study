def solution(num, total):
    answer = []
    # 숫자가 시작하는 값과
    start = 0
    while True:
        # start부터 start+num까지 1씩 증가하며 리스트를 만들고
        answer = [i for i in range(start,start+num)]
        # 리스트의 합이 total보다 크면
        if sum(answer) > total:
            # start를 -1해주고
            start -= 1
        # 합이 total보다 작으면
        elif sum(answer) < total:
            # start를 + 1gownrh
            start += 1
        else:
            # total이랑 같으면 answer를 반환
            return answer
        