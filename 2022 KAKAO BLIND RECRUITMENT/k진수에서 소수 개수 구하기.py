import math
def is_prime(num):
    if num==1:
        return 0
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1
def k_decimal(num,k):
    decimal_num = ''
    while num!=0:
        bit = num%k
        num = int(num/k)
        decimal_num += str(bit)
    return decimal_num[::-1]
def find_prime(decimal):
    k_nums = decimal.split('0')
    prime_count = 0
    for i in k_nums:
        if i=='':
            continue
        if is_prime(int(i)):
            prime_count += 1
    return prime_count
def solution(n,k):
    decimal_num = k_decimal(n,k)
    answer = find_prime(decimal_num)
    return answer