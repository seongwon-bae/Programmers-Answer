def to_binary(decimal,n):
    binary_num = list(' '*n)
    index=0
    while decimal!=0:
        if int(decimal%2) == 0:
            pass
        else:
            binary_num[index] = '#'
            binary_num[index].replace(' ', '#')
        decimal = decimal // 2
        index+=1
    return "".join(binary_num)[::-1]
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        output = ''
        for j in range(n):
            if to_binary(arr1[i],n)[j] == '#' or to_binary(arr2[i],n)[j] == '#':
                output += '#'
            else:
                output += ' '
        answer.append(output)
    return answer