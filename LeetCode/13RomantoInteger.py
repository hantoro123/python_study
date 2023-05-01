class Solution:
    def romanToInt(self, s: str) -> int:
        # 각 로만자에 대한 숫자
        Roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # 로만자를 정수로 바꿀 변수
        intenger = 0
        # 로만자 만큼 반복하며 조건문을 따른다.
        for i in range(len(s)):
            if i < len(s)-1:
                if s[i] == 'I':
                    if s[i+1] == 'V':
                        intenger -= Roman[s[i]]
                    elif s[i+1] == 'X':
                        intenger -= Roman[s[i]]
                    else:
                        intenger += Roman[s[i]]
                elif s[i] == 'X':
                    if s[i+1] == 'L':
                        intenger -= Roman[s[i]]
                    elif s[i+1] == 'C':
                        intenger -= Roman[s[i]]
                    else:
                        intenger += Roman[s[i]]
                elif s[i] == 'C':
                    if s[i+1] == 'D':
                        intenger -= Roman[s[i]]
                    elif s[i+1] == 'M':
                        intenger -= Roman[s[i]]
                    else:
                        intenger += Roman[s[i]]
                else:
                    intenger += Roman[s[i]]
            else:
                intenger += Roman[s[i]]

        return intenger