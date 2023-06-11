def solution(answers):
    answer = []
    # 각 학생이 찍는 순서
    students = {1:[1,2,3,4,5],2:[2,1,2,3,2,4,2,5],3:[3,3,1,1,2,2,4,4,5,5]}
    # 학생이 맞춘 정답의 수를 입력할 리스트
    correct = [0,0,0,0]
    
    for i in range(len(answers)):
        # 각 문제의 길이만큼 학생의 정답과 비교후 맞으면 + 1
        if students[1][i%5] == answers[i]:
            correct[1] += 1
        if students[2][i%8] == answers[i]:
            correct[2] += 1
        if students[3][i%10] == answers[i]:
            correct[3] += 1

    # 가장 높은 점수를 가져와서
    high = max(correct)
    
    for c in range(len(correct)):
        # 각 번호가 high와 같으면 answer에 넣는다.
        if correct[c] == high:
            answer.append(c)
            
    # answer를 반환
    return answer