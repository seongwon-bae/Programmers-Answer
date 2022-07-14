def is_prime(num):
    prime = True
    for i in range(2,int(num/2)+1):
        if num%i==0:
            prime = False
            break
    return prime

def solution(nums):
    count = 0
    for i in range(len(nums)):
        first = nums[i]
        for j in range(i+1,len(nums)):
            mid = nums[j]
            for k in range(j+1, len(nums)):
                last = nums[k]
                if is_prime(first+mid+last):
                    count += 1
    return count