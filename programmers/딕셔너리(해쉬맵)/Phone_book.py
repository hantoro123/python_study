def solution(phone_book):
    answer = True
    # 전화번호 목록을 정렬해주고
    sort_book = sorted(phone_book)
    # 마지막 전까지 반복해준다.
    for n in range(len(sort_book)-1):
        # 길이가 뒷 번호 보다 짧거나 같다면
        if len(sort_book[n]) <= len(sort_book[n+1]):
            # 지금 번호가 뒷번호의 접두어로 있는지 확인하다.
            if sort_book[n] == sort_book[n+1][:len(sort_book[n])]:
                # 접두어라면 바로 False를 반환하고
                return False

    # 끝가지 접두어가 없다면 True를 반환한다.    
    return answer