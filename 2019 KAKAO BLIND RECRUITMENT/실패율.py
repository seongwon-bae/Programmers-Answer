def solution(N, stages):
    stage_info = {i:0 for i in range(1,N+2)}
    for s in stages:
        stage_info[s] += 1
    loser = 0
    for i in range(1,N+1):
        if len(stages)-loser == 0:
            fail_rate = 0
        else:
            fail_rate = stage_info[i] / (len(stages)-loser)
        loser += stage_info[i]
        stage_info[i] = fail_rate
    stage_info = dict(sorted(stage_info.items(), key=lambda x: x[1], reverse=True))
    print(stage_info)
    answer = []
    for k in stage_info.keys():
        if k==N+1:
            continue
        answer.append(k)
    return answer