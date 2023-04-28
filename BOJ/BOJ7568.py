def big(p,n):
    rank = [ 1 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if p[i][0] > p[j][0] and p[i][1] > p[j][1]:     # i번 사람이 j번 사람보다 몸무게 키가 크면
                    rank[j] += 1                                # j번 사람 등수 +1

    return rank
 
person=[]                           
n = int(input())                    # 사람 몇명인지
for i in range(n):
    x,y = map(int,input().split())  # 몸무게 키 받기
    person.append([x,y])            # 0~n번 사람까지 몸무게 키 넣기

print(*big(person,n))