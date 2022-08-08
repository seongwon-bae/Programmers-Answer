def solution(dartResult):
    scores=[]
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            score = int(dartResult[i-1])
            if dartResult[i-1]=='0' and dartResult[i-2]=='1':
                score = 10
            if dartResult[i]=='S':
                scores.append(score**1)
            elif dartResult[i]=='D':
                scores.append(score**2)
            else:
                scores.append(score**3)
        elif dartResult[i] == '*':
            if len(scores)==1:
                scores.append(scores.pop()*2)
            else:
                num1 = scores.pop()*2
                num2 = scores.pop()*2
                scores.append(num2)
                scores.append(num1)
        elif dartResult[i] == '#':
            scores.append(scores.pop()*-1)
    return sum(scores)