import re

def solution(str1, str2):
    answer = 0
    # str1, str2를 모두 소문자로 바꾸고
    str1 = str1.lower()
    str2 = str2.lower()
    # str1, str2의  알파벳만 추출해서 넣는다.
    str1_set = [str1[i]+str1[i+1] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    str2_set = [str2[i]+str2[i+1] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    # 교집합
    union = []
    # str1+str2의 집합에서 해당 문자열이 각 문자열에 몇개 있는지 찾고
    for j in set(str1_set+str2_set):
        s1 = str1_set.count(j)
        s2 = str2_set.count(j)
        # 갯수가 작은걸 넣는다.
        union.append(min(s1,s2))
    
    #합집합
    intersection = []
    # str1+str2의 집합에서
    for i in set(str1_set+str2_set):
        # 각 문자열이 각각에서 몇개인지 찾고
        s1 = str1_set.count(i)
        s2 = str2_set.count(i)
        # 갯수가 큰걸 넣는다.
        intersection.append(max(s1,s2))
    
    
    # 교집합과 합집합이 모두 존재하면
    if union and intersection:
        # 계산한 자카드 유사도애 65536을 곱한 값을 answer에 넣는다.
        answer = int((sum(union)/sum(intersection))*65536)
    elif not union and intersection:
        # 교집합이 없다면 answer는 0
        answer = 0
    else:
        # 그 외에는 65536이다.
        answer = 65536
    
    # answer를 반환한다.
    return answer