def solution(genres, plays):
    answer = []
    # 각 장르의 총 재생된 횟수
    total = {}
    # 각 장르의 번호마다 재생된 횟수
    count = {}
    for i in range(len(genres)):
        # total에 장르가 있다면
        if total.get(genres[i]):
            # 해당 장르에 총 횟수와 각 번호에 재생된 횟수를 더해준다.
            total[genres[i]] += plays[i]
            count[genres[i]] += [[i,plays[i]]]
        # 장르가 존재하지 않으면
        else:
            # 해당 장르에 총횟수와 번호에 횟수를 넣는다.
            total[genres[i]] = plays[i]
            count[genres[i]] = [[i,plays[i]]]
    
    # total의 경우 큰 순으로 정렬한다.
    total = dict(sorted(total.items(),key=lambda x: -x[1]))

    for c in count:
        # count의 경우도 각 장르에 있는 노래를 큰 순으로 정렬한다.
        count[c] = sorted(count[c],key=lambda x:(x[1],-x[0]), reverse=True)
        

    for t in total:
        # 만약 해당 장르에 노래가 1개 이상이면
        if len(count[t]) > 1:
            # 1,2번 노래만 answer에 넣는다.
            answer.append(count[t][0][0])
            answer.append(count[t][1][0])
        # 만약에 장르에 노래가 1개면
        else:
            # 1번 노래만 answer에 넣는다.
            answer.append(count[t][0][0])    
    
    # 정해진 노래를 담은 playlist를 반환한다.
    return answer