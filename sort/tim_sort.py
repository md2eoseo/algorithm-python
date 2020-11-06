# minrun보다 크기가 큰 경우 합병정렬, 작은 경우 삽입정렬
# 삽입정렬 되어있는 부분들을 합병정렬
# best : nlog(n)
# average : nlog(n)
# worst : nlog(n)
# memory : 

from data import data
DATA_LEN = len(data)
RUN = 32

def insertion_sort(data, left, right):
    for i in range(left+1, right+1):
        temp = data[i]
        j = i-1
        while j >= left and data[j] > temp:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp

def merge(data, l, m, r):
    len1, len2 = m-l+1, r-m
    left, right = [], []
    for i in range(0, len1):
        left.append(data[l+i])
    for i in range(0, len2):
        right.append(data[m+i+1])

    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        data[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        data[k] = right[j]
        k += 1
        j += 1

def tim_sort(data):
    for i in range(0, DATA_LEN, RUN):
        insertion_sort(data, i, min((i+31), (DATA_LEN-1)))

    size = RUN
    while size < DATA_LEN:
        for left in range(0, DATA_LEN, 2*size):
            mid = left + size - 1
            right = min((left+2*size-1), (DATA_LEN-1))
            merge(data, left, mid, right)
        size = 2*size

tim_sort(data)
print(data)