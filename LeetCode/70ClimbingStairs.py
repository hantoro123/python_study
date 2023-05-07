class Solution:
    def climbStairs(self, n: int) -> int:
        # 계단 갯수 마다 방법수 만큼 list에 넣는다.
        dp = [0,1,2,3]+([0]*42)
        # 45개의 계단의 모든 방법 수는
        for i in range(4,46):
            # i개의 계단은 i-1, i-2개의 계단을 오른 방법의 수를
            # 합한 수와 같다
            dp[i] = dp[i-1]+dp[i-2]

        # 해당 계단 수를 출력한다.
        return dp[n] 