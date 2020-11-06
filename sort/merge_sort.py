# 분할정복 알고리즘
# 리스트의 길이가 0 또는 1일 때 정렬된 것으로 보고 그렇지 않으면 리스트를 절반으로 나눈다.
# 각 리스트를 재귀적으로 앞의 과정을 반복하여 정렬하고 정렬된 두 리스트를 합쳐 정렬된 리스트를 합병한다.
# best : nlog(n)
# average : nlog(n)
# worst : nlog(n)
# memory : n

from data import data

def merge(left, right):
    l = 0
    r = 0
    sorted = []

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1

    while l < len(left):
        sorted.append(left[l])
        l += 1
    while r < len(right):
        sorted.append(right[r])
        r += 1

    return sorted

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

sorted = merge_sort(data)
print(sorted)