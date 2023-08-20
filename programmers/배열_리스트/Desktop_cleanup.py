def solution(wallpaper):
    # 바탕화면의 왼쪽위 끝 오른쪽 아래 끝의 좌표를 넣어주고 
    x1,x2,y1,y2 = len(wallpaper),0,len(wallpaper[0]),0
    
    # x길이만큼 반복
    for x in range(len(wallpaper)):
        # x에 따른 y의 길이 만큼 반복하고
        for y in range(len(wallpaper[x])):
            # 해당 좌표에 파일이 있는지 확인하고
            if wallpaper[x][y] == '#':
                # 드래그하기 위해 현재 좌표의 x,y값이 가장 큰지 작은지 확인 후 넣는다.
                if x < x1:
                    x1 = x
                if x > x2:
                    x2 = x
                if y < y1:
                    y1 = y
                if y > y2:
                    y2 = y
    # 드래그 하기위한 좌표를 구하면 이를 반환한다.                    
    return [x1,y1,x2+1,y2+1]