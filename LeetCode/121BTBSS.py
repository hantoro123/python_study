class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 이익이 얼마인지와 주식을 샀을때 금액을 0번으로 한다.
        profit = 0; buy = prices[0]
        # 1번 부터 주식 금액을 반복하고
        for sell in prices[1:]:
          # 팔려는 금액이 사려는 금액보다 크다면
          if sell > buy:
            # 지금까지 이익과 지금 팔면 받는 이익중 큰값을 이익으로 정한다.
            profit = max(profit,sell-buy)
          else:
            # 팔려는 금액이 작으면 그금액으로 산다.
            buy = sell

        # 이익을 반환한다.
        return profit