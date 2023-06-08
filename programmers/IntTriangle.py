def solution(triangle):
    # 삼각형의 길이
    t_len = len(triangle)
    
    for i in range(1, t_len):
        for j in range(i+1):
            # 각 위치에서 만약 j가 0번이면
            if j == 0:
                # 바로 왼쪽끝이면 i-1의 0번 인덱스값을 더해주고
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                # j가 오른쪽 끝이면 i-1의 j-1번 인덱스값을 더해주고
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 중간 값이라면 i-1의 j,j-1값중 더 큰값을 더해준다.
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    
    # 최종적으로 삼각형의 마지막 줄에서 가장 큰값을 반환한다.
    return max(triangle[-1])