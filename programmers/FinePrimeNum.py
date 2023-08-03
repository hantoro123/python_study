def isprime(n):
    # 2보다 작으면 소수가 아님 False반환
    if n < 2:
        return False
    # 2~n-1까지 반복하며 나누어 떨어지는지 확인한다.
    for i in range(2,n):
        # 나누어 떨어지면 False반환
        if n%i == 0:
            return False
    # 나누어 안떨어지면 소수이므로 True
    return True    

from itertools import permutations

def solution(numbers):
    # 모든 조합을 담을 집합
    pnum = set()
    for r in range(1,len(numbers)+1):
        # number를 r개씩 뽑아서 생길 수 있는 조합을 com에 넣는다.
        com = list(permutations(numbers,r))
        # com 내부 원소들을 반복하며
        for c in com:
            # num에 int형으로 담고
            num = int(''.join(c))
            # 소수인지 판별 후
            if isprime(num):
                # 소수면 집하베 add
                pnum.add(num)
    
    # 소수의 갯수를 반환
    return len(pnum)