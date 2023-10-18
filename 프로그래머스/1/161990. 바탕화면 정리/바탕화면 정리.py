# x와 y의 최대, 최소 도출하기
def solution(wallpaper):
    x_min, y_min, x_max, y_max = len(wallpaper), len(wallpaper[0]), 0, 0
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                print(row, col)
                if row <= x_min :
                    x_min = row
                if row > x_max :
                    x_max = row
                if col <= y_min :
                    y_min = col
                if col > y_max :
                    y_max = col
    answer = [x_min, y_min, x_max+1, y_max+1]
    return answer
