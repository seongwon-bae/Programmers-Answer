def decimal_to_ternary(n):
    code = ''
    while n>0:
        code += str(n%3)
        n = int(n/3)
    return code[::-1]
def ternary_to_decimal(code):
    num=1
    result = 0
    for c in code:
        result += num*int(c)
        num*=3
    return result
def solution(n):
    answer = ternary_to_decimal(decimal_to_ternary(n))
    return answer