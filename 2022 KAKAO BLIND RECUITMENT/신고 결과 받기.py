def solution(id_list, report, k):
    report_dict = dict()
    report_result = dict()
    answer=[]

    for i in id_list:
        report_dict[i] = set()
        report_result[i] = 0
    for i in report:
        reporter, reported = i.split()
        report_dict.get(reported).add(reporter)
    for key,val in report_dict.items():
        if len(val)>=k:
            for j in val:
                report_result[j] += 1
    for key, val in report_result.items():
        answer.append(val)
    return answer

