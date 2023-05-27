def solution(sequence, k):
    answer = []
    l = len(sequence)
    # 오른쪽 인덱스
    right = 0
    # 부분 수열의 합을 계산할 변수
    sub_sum = sequence[0]
    for left in range(l):
        # right + 1이 길이보다작아야하고 합이 k보다 작아야한다.
        while right + 1 < l and sub_sum < k:
            # 오른족을 한칸씩 증가하고 
            right += 1
            # 증가한 인덱스의 값을 합한다.
            sub_sum += sequence[right]
            
        # 합이 k랑 같다면
        if sub_sum == k:
            # answer가 비어있을때는 그대로 넣고
            if not answer:
                answer = [left, right]
            else:
                #아니라면 answer의 인덱스의 길이와 부분 수열 합의 길이를 비교
                if answer[1]-answer[0] > right-left:
                    # 작으면 바꾼다.
                    answer = [left,right]
        # 여기까지 오면 k와 같거나 커다 따라서 - left의 값을 한다.
        sub_sum -= sequence[left]
    
    # 최종 answer를 반환
    return answer