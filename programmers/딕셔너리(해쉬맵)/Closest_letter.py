def solution(s):
    # 글자의 현재 위치를 담을 딕셔너리
    position = {}
    answer = []
    for i in range(len(s)):
        try:
            # 현재 위치에서 전에 있던 위치를 빼준만큼을 answer에 넣어주고
            answer.append(i-position[s[i]])
            # 글자의 위치를 현재위치로 바꿔 준다.
            position[s[i]] = i
        # 만약 아직 위치가 없다면
        except:
            # answer에 -1을 넣어주고
            answer.append(-1)
            # 글자의 위치를 현재위치로 해준다.
            position[s[i]] = i
    
    # 결과 리스트를 반환한다.
    return answer