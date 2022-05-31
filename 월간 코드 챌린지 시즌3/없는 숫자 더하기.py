def solution(numbers):
    answer = sum([i for i in range(1,10)])
    for n in numbers:
        answer -= n
    return answer