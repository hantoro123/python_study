class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 만들어진 파스칼 삼각형 리스트에 1을 채워 넣는다.
        dp=[[1] for _ in range(numRows)]
        if numRows > 1:
            # row가 1보다 크면
            for i in range(1,numRows):
                for j in range(1,i):
                    # 다음 행은 전 행의 j와 j-1인덱스의 값을 합한값
                    dp[i].append(dp[i-1][j-1]+dp[i-1][j])
                # 마지막에는 1을 넣는다.
                dp[i].append(1)
        # 파스칼 삼각형을 출력하면 끝
        return dp