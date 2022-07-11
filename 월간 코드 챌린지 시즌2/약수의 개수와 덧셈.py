def find_divisor(num):
    count = 1
    for i in range(1,int(num/2)+1):
        if num%i==0:
            count += 1
    if count%2==0:
        return 1
    else:
        return -1

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += i*find_divisor(i)
    return answer