def solution(x, y, n):
    # 현재 위치로 오는데 최소값을 넣을 배열
    dp = [10**6]*(10**6+1)
    # 시작 위치는 0번 계산시 올 수 있고
    dp[x] = 0
    
    for i in range(x,y):
        # 만약에 y위치가 최대 숫자말고 값이 있다면
        if dp[y] != 10**6:
            # 즉시 반환하고
            return dp[y]
        
        # i값에 +n,*2,*3 값을 각각하고
        for j in (i+n,i*2,i*3):
            # 최대값을 넘어가면 그냥 다음으로 반복
            if 10**6<j:
                continue
            # j위치에 dp[j]와 dp[i]+1중 작은 값으로
            dp[j] = min(dp[j], dp[i]+1)
    
    # 반복이 종료되면 dp[y]의 값이 있으면 dp[y]를 없으면 -1을 반환
    return dp[y] if dp[y] != 10**6 else -1