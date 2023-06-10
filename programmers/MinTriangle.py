def solution(sizes):
    # 가로와 세로의 최대길이를 입력할 변수
    max1 = 0
    max2 = 0
    for i in range(len(sizes)):
        # 만약 세로가 가로보다 길면 명함을 눕혀 가로와 세로를 바꾸고
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
        
        # 각 가로 세로의 최대값과 지금 값중 큰값을 넣는다.
        max1 = max(max1,sizes[i][0])
        max2 = max(max2,sizes[i][1])
    
    # 찾은 최대값을 곱한다.
    return max1*max2