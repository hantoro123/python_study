class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 자릿수 마다 26의 i제곱, 최종 숫자
        i = 0; num = 0
        # 리스트의 역순으로 반복하며
        for excel in columnTitle[::-1]:
            # A=65 Z=90
            # 아스키코드로 변환후 - 64 하고 자릿수를 맞춰준다.
            num += (ord(excel)-64)*(26**i)
            i += 1

        # num반환
        return num