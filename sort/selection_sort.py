# 데이터에서 최댓값(최솟값)을 가장 오른쪽(왼쪽) 값과 swap
# best : n(2)
# average : n(2)
# worst : n(2)
# memory : 1

from data import data
DATA_LEN = len(data)

def swap(data, a, b):
    data[a], data[b] = data[b], data[a]

def max_selection_sort(data):
    for size in reversed(range(DATA_LEN)):
        max_i = 0
        for i in range(1, size + 1):
            if data[max_i] < data[i]:
                max_i = i;
        swap(data, max_i, size)

def min_selection_sort(data):
    for size in reversed(range(DATA_LEN)):
        min_i = DATA_LEN - 1
        for i in range(DATA_LEN - size - 1, DATA_LEN):
            if data[min_i] > data[i]:
                min_i = i;
        swap(data, min_i, DATA_LEN - size - 1)

min_selection_sort(data)
print(data)