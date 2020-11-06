# pivot을 기준으로 pivot 값보다 작은 요소들을 좌측, 큰 요소들을 우측으로 분리시킨다.
# 분리된 양쪽 리스트를 재귀적으로 정렬한다.
# pivot을 중앙에 위치한 요소로 지정
# best : nlog(n)
# average : nlog(n)
# worst : n(2)
# memory : log(n)

from data import data
DATA_LEN = len(data)

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[len(data)//2]
    left, equal, right = [], [], []
    for i in data:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    
    return quick_sort(left) + equal + quick_sort(right)

sorted = quick_sort(data)
print(sorted)