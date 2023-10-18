# x와 y의 최대, 최소 도출하기
def solution(wallpaper):
    all_row = []
    all_col = []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                all_row.append(row)
                all_col.append(col)
    answer = [min(all_row), min(all_col), max(all_row)+1, max(all_col)+1]
    return answer
