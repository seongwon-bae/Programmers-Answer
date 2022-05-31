def calculate_distance(now, dest):
    distance = 0
    distance += abs(now[0]-dest[0]) + abs(now[1]-dest[1])
    return distance
def dicision_position(now,n,keypad):
    now_position = []
    dest_position = []
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] == now:
                now_position = [i, j]
            if keypad[i][j] == n:
                dest_position = [i, j]
    distance = calculate_distance(now_position, dest_position)
    return distance
def solution(numbers, hand):
    keypad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ['*',0,'#']]
    answer = ''
    now_left = '*'
    now_right = '#'
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            now_left = n
        elif n in [3,6,9]:
            answer += 'R'
            now_right = n
        else:
            distance_left = dicision_position(now_left,n,keypad)
            distance_right = dicision_position(now_right,n,keypad)
            if distance_left < distance_right:
                answer += 'L'
                now_left = n
            elif distance_left > distance_right:
                answer += 'R'
                now_right = n
            else:
                if hand=='left':
                    answer += 'L'
                    now_left = n
                else:
                    answer += 'R'
                    now_right = n
    return answer