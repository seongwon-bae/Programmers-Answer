
def solution(board, moves):
    answer = 0
    basket=[]
    for i in range(len(moves)):
        for p in range(len(board)):
            if board[p][moves[i]-1] == 0:
                continue
            else:
                if len(basket)>0 and basket[-1]==board[p][moves[i] - 1]:
                    board[p][moves[i] - 1] = 0
                    basket.pop()
                    answer += 2
                    break
                else:
                    basket.append(board[p][moves[i] - 1])
                    board[p][moves[i] - 1] = 0
                    break
    return answer