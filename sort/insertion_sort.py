# 데이터의 두번째 요소부터 좌측에 이미 정렬된 배열 사이에 끼워 넣는다
# best : n
# average : n(2)
# worst : n(2)
# memory : 1

from data import data
DATA_LEN = len(data)

def insertion_sort(data):
    for size in range(1, DATA_LEN):
        i = size
        val = data[size]
        while i > 0 and data[i-1] > val:
            data[i] = data[i-1]
            i -= 1
        data[i] = val

insertion_sort(data)
print(data)