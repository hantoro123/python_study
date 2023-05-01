class Solution:
    def romanToInt(self, s: str) -> int:
        # 각 로만자에 대한 숫자
        Roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # 로만자를 정수로 바꿀 변수
        integer = 0
        # 로만자 만큼 반복하며 조건문을 따른다.
        for i in range(len(s)):
            if Roman[s[i]] < Roman[s[i+1]]:
                integer -= Roman[s[i]]
            else:
                integer += Roman[s[i]]

        return integer + Roman[s[-1]]