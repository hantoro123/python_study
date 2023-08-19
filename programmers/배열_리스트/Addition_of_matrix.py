def solution(arr1, arr2):
    answer = []
    # 배열의 row만큼 반복하며
    for i in range(len(arr1)):
        # 더한 값을 넣을 리스트
        sol = []
        # 열을 반복하며
        for j in range(len(arr1[i])):
            # 해당 행과 열의 값을 더해주고
            sol.append(arr1[i][j]+arr2[i][j])
        # answer에 넣는다.
        answer.append(sol)
                       
    # 전부 더해진 행렬을 반환한다.
    return answer