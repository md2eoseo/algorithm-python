# pivot을 기준으로 pivot 값보다 작은 요소들을 좌측, 큰 요소들을 우측으로 분리시킨다.
# 분리된 양쪽 리스트를 재귀적으로 정렬한다.
# pivot을 가장 우측에 위치한 요소로 지정
# best : nlog(n)
# average : nlog(n)
# worst : n(2)
# memory : log(n)

from data import data
DATA_LEN = len(data)

def swap(data, a, b):
    data[a], data[b] = data[b], data[a]

def partition(data, p, r):
    x = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= x:
            i += 1
            swap(data, i, j)
    swap(data, i+1, r)
    return i+1

def quick_sort(data, p, r):
    if p < r:
        q = partition(data, p, r)
        quick_sort(data, p, q-1)
        quick_sort(data, q+1, r)

quick_sort(data, 0, DATA_LEN - 1)
print(data)