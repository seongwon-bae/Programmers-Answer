def solution(s):
    ten_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while 1:
        try:
            if type(1)==type(int(s)):
                break
        except:
            for t in ten_digits:
                if t in s:
                    s = s.replace(t,str(ten_digits.index(t)))
    return int(s)