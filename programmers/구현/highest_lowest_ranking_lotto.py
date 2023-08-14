def solution(lottos, win_nums):
    # 몇개의 번호가 일치하면 몇등을 하는지 딕셔너리로 선언
    win = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    # max_win과 min_win 선언
    max_win = 0
    min_win = 0
    # 로또 번호가 있다면
    for l in lottos:
        # 맞는 번호가 있을때
        if l in win_nums:
            # max와 min을 +1
            min_win += 1
            max_win += 1
        elif l == 0:
            # 지워진 부분은 max만 +1
            max_win += 1
    
    # 구한 max와 min을 반환
    return [win[max_win], win[min_win]]