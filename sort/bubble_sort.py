# 데이터 정렬 여부 파악에 좋음
# best : n
# average : n(2)
# worst : n(2)
# memory : 1

from data import data
DATA_LEN = len(data)

def swap(data, a, b):
    data[a], data[b] = data[b], data[a]

def bubble_sort1(data):
    for size in range(DATA_LEN):
        for i in range(DATA_LEN - size - 1):
            if data[i] > data[i+1]:
                swap(data, i, i+1)

def bubble_sort2(data):
    for size in reversed(range(DATA_LEN)):
        for i in range(size):
            if data[i] > data[i+1]:
                swap(data, i, i+1)

bubble_sort2(data)
print(data)