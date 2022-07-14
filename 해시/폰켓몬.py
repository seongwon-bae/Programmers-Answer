def solution(nums):
    count = int(len(nums)/2)
    poncketmons = set()
    answer = 0
    for i in nums:
        poncketmons.add(i)
    if len(poncketmons) >= count:
        answer = count
    else:
        answer = len(poncketmons)
    return answer