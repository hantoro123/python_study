class Solution:
    def mySqrt(self, x: int) -> int:
        # x의 값이 0이면 0
        if x == 0:
            return 0
        # 4보다 작으면 무조건 1
        elif x < 4:
            return 1
        else:
            # 그외의 숫자는
            for i in range(2,x):
                # 2부터 제곱을 했을때 제곱이 커지면 그 전 숫자를 반환
                if x < i*i:
                    return i-1