def solution(lottos, win_nums):
    correct = 0
    zeros = 0
    for l in range(len(lottos)):
        print(lottos[l])
        if lottos[l] in win_nums:
            correct += 1
        elif lottos[l]==0:
            zeros += 1
    best = 7-(correct+zeros)
    if best==7:
        best=6
    if correct < 2:
        worst = 6
    else:
        worst = 7 - (correct)
    answer = [best, worst]
    return answer

lottos = [1,2,3,4,5,6]
win_nums = [7,8,9,10,11,12]
print(solution(lottos, win_nums))