class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 번호를 넣을 변수와 digits의 길이를 넣는다.
        num = 0; digit_len = len(digits)
        # 길이만큼 반복하면서
        for i in range(digit_len):
            # 각 숫자를 자릿수에 맞게 곱해서 숫자로 변환한다.
            num += digits[i]*(10**(digit_len-i-1))

        # num+1을 하여 리스트로 반환
        return list(map(int,f"{num+1}"))