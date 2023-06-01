def solution(genres, plays):
    answer = []
    # 음악과 각 장르별 총 play를 담을 딕셔너리
    music = dict()
    total_p = dict()
    # 장르의 길이만큼 반복하며
    for i in range(len(genres)):
        # g,p에 해당 인덱스의 장르와 play수를 담고
        g = genres[i]
        p = plays[i]
        # music에 장르가 있으면
        if music.get(g):
            # music의 장르에 해당하는 키의 value에 play와 장르를 리스트로 담는다.
            music[g].append([p,i])
            # 장르의 토탈 play에 더해준다.
            total_p[g] += p
        else:
            # 장르가 아직 등록 안되어 있다면 일단 넣어준다.
            music[g] = [[p,i]]
            total_p[g] = p
    
    # 각 장르를 value인 play의 내림차순이면서 같으면 인덱스의 오름차순으로 정렬한다.
    for m in music:
        music[m] = sorted(music[m], key=lambda x:(-x[0],x[1]))
    
    # total도 value로 내림차순 한다.
    total_p = dict(sorted(total_p.items(), key=lambda x: -x[1]))  
    # 각 장르마다
    for p in total_p:
        # 두개씩 넣는데 하나만 있다면 하나만 넣는다.
        if len(music[p]) > 1:
            answer.append(music[p][0][1])
            answer.append(music[p][1][1])
        else:
            answer.append(music[p][0][1])
    
    # 최종 answer 반환
    return answer