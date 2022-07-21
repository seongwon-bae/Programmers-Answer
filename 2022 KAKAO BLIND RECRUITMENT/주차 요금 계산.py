import math

def time_transform(time):
    hour, minute = map(int,time.split(':'))
    return hour*60 + minute

def time_calculate(in_time, out_time):
    return time_transform(out_time) - time_transform(in_time)

def fee_calculate(base_time, base_fee, unit_time, unit_fee, full_time):
    remain_time = full_time-base_time
    if remain_time<0:
        remain_time=0
    return base_fee + (math.ceil((remain_time)/unit_time))*unit_fee

def solution(fees, records):
    # 차량번호가 작은 차부터 주차 요금을 차례대로 넣음.
    IO_time = {x.split()[1]: [] for x in records}
    for r in records:
        IO_time[r.split()[1]].append(r.split()[0])
    for k,v in IO_time.items():
        if len(v)%2 != 0:
            IO_time[k].append("23:59")
    IO_time=dict(sorted(IO_time.items()))
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    answer = []
    for k,v in IO_time.items():
        all_time = 0
        for index in range(0,len(v),2):
            all_time += time_calculate(v[index], v[index+1])
        all_fee = fee_calculate(base_time, base_fee, unit_time, unit_fee, all_time)
        answer.append(all_fee)
    return answer

# fees : [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
# records : [시각, 차량번호, 내역(IN/OUT)]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees,records))