def solution(players, callings):
    players_dict = dict()
    for idx, values in enumerate(players):
        players_dict[values] = idx
    
    for call in callings:
        rank = players_dict[call]
        
        # 딕셔너리 위치 변경
        players_dict[call] -=1
        players_dict[players[rank-1]] +=1
        
        # 배열 위치 변경
        players[rank-1], players[rank] = call, players[rank-1]
                
    answer = players
    return answer