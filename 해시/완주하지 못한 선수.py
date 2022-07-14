def solution(participant, completion):
    player = dict()
    answer = ''
    for p in participant:
        if p in player.keys():
            player[p] += 1
        else:
            player[p]=0
    for c in completion:
        if c in player.keys():
            player[c] -= 1
    for k,v in player.items():
        if v==0:
            answer = k
    return answer