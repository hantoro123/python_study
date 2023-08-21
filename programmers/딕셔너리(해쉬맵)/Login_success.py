def solution(id_pw, db):
    user_db = {}
    # db의 id와 pwd를 가져와 딕셔너리에 넣어준다.
    for d in db:
        user_db[d[0]] = d[1]
    
    try:
        # 만약 id에 해당하는 비번이 맞으면 
        if user_db[id_pw[0]] == id_pw[1]:
            # login반환
            return 'login'
        # 비번이 틀리면 wrong pw 반환
        else:
            return 'wrong pw'
    except:
        # id가 존재하지 않으면 fail반환
        return 'fail'