def solution(quiz):
    answer = []
    # 값을 가져와서 반복한다.
    for q in quiz:
        # 퀴즈를 공백으로 구분하고
        calcul = list(q.split())
        # 연산자가 +면 
        if calcul[1] == '+':
            # 두 정수를 더해주고 그 값이 답과 같다면 
            if int(calcul[0])+int(calcul[2]) == int(calcul[4]):
                # answer에 O를
                answer.append('O')
            else:
                # 다르면 answer에 X를 append
                answer.append('X')
        # 연산자가 -면
        else:
            # 두 정수를 빼주고 그 값이 답과 같다면
            if int(calcul[0])-int(calcul[2]) == int(calcul[4]):
                # answer에 O를
                answer.append('O')
            else:
                # 다르면 answer에 X를 append 한다.
                answer.append('X') 
            
    # 모든 퀴즈의 답이 있는 answer를 반환
    return answer