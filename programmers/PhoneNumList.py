def solution(phone_book):
    # 전화번호부 길이를 넣고
    p_len = len(phone_book)
    # 전화번호부를 정렬해준다.
    sort_book = sorted(phone_book)
    # 길이 -1 만큼 반복하며
    for p in range(p_len-1):
        # 지금 위치의 번호가 다음 번호의 0~앞번호의 길이만큼과 같다면
        if sort_book[p] == sort_book[p+1][:len(sort_book[p])]:
            # False를 바로 반환
            return False
    # 아니라면 True를 반환
    return True