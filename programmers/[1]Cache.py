def solution(cacheSize, cities):
    # 실행될 runtime과
    runtime = 0
    # 도시 이름이 들어갈 cache
    cache = []
    for city in cities:
        # 모든 도시이름은 소문자로 하고
        c = city.lower()
        # cache에 도시이름이 있다면
        if c in cache:
            # 도시이름을 cache 마지막에 두고
            cache.remove(c)
            cache.append(c)
            # runtime을 1만 증가
            runtime += 1
            continue
        else:# 찾지 못했했다면
            # cache가 꽉차면
            if len(cache) >= cacheSize:
                # cache에 도시이름을 넣고
                cache.append(c)
                # 첫번째 cache를 삭제한다.
                del cache[0]
            else:
                # cache가 공간이 있으면 그냥 넣는다.
                cache.append(c)
            # 최종적으로 runtime + 5
            runtime += 5
    
    # runtime을 반환
    return runtime