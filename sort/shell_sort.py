# 주어진 간격만큼 떨어진 서브배열을 만들어 삽입 정렬을 수행
# best : nlog(n)
# average : nlog(n)
# worst : n(2)
# memory : 1

from data import data
DATA_LEN = len(data)

def gap_insertion_sort(data, start, gap):
    for target in range(start+gap, DATA_LEN, gap):
        i = target
        val = data[target]
        while i > start:
            if data[i-gap] > val:
                data[i] = data[i-gap]
            else:
                break
            i -= gap
        data[i] = val

def shell_sort(data):
    gap = DATA_LEN // 2;
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(data, start, gap)
        gap = gap // 2

shell_sort(data)
print(data)