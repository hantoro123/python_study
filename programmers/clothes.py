def solution(clothes):
    cl_kind = dict()
    # 각 종류의 의상이 몇개인지 종류를 키로 갯수를 value로 딕셔너리를 구성
    for k in clothes:
        if cl_kind.get(k[1]):
            cl_kind[k[1]] += 1
        else:
            cl_kind[k[1]] = 1
    
    
    com = 1
    for c in cl_kind:
        # 해당 종류의 의상을 하나씩 입는경우 + 안입는 경우 한가지를 더헤 곱한다.
        com *= (cl_kind[c]+1)
    
    # 마지막으로 아무것도 안입는 경우 1가지를 빼 반환한다.
    return com-1