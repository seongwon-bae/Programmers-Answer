def step1(id):
    return id.lower()
def step2(id):
    changed_id=''
    for i in id:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_' or i=='.':
            changed_id+=i
    return changed_id
def step3(id):
    while 1:
        if '..' in id:
            id = id.replace('..','.')
        else:
            break
    return id
def step4(id):
    while 1:
        if len(id)>=1:
            if id[0]=='.' or id[-1]=='.':
                id = id.strip('.')
            else:
                break
        else:
            break
    return id
def step5(id):
    if id=='':
        id='a'
    return id
def step6(id):
    if len(id)>=16:
        id = id[:15]
        id = id.rstrip('.')
    return id
def step7(id):
    while len(id)<=2:
        id += id[-1:]
    return id
def solution(new_id):
    answer = step1(new_id)
    answer = step2(answer)
    answer = step3(answer)
    answer = step4(answer)
    answer = step5(answer)
    answer = step6(answer)
    answer = step7(answer)
    return answer