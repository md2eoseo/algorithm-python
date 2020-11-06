# 힙(heap) : 힙 조건을 만족하는 완전 이진트리
# 힙 조건 : 각 노드의 값이 자식 노드의 값보다 커야한다는 것
# 힙의 루트 노드에는 가장 큰 수(가장 높은 우선순위)가 저장되므로, 루트의 숫자를 힙의 가장 마지막 노드에 있는 숫자와 바꾼다.
# 루트에 새로 저장된 숫자로 인해 위배된 힙 조건을 해결하여 힙 조건을 만족시키고, 힙 크기를 1개 줄인다.
# 이 과정을 반복하여 나머지 숫자를 정렬한다.
# best : n
# average : nlog(n)
# worst : nlog(n)
# memory : 1

from data import data
DATA_LEN = len(data)

def swap(data, a, b):
    data[a], data[b] = data[b], data[a]

def build_heap(heap_size = DATA_LEN):
    for i in range(heap_size//2, 0, -1):
        down_heap(i, heap_size)

def down_heap(i, heap_size = DATA_LEN):
    left = 2*i
    right = 2*i+1

    if left <= heap_size and data[left] > data[i]:
        bigger = left
    else:
        bigger = i
        
    if right <= heap_size and data[right] > data[bigger]:
        bigger = right

    if bigger != i:
        swap(data, i, bigger)
        down_heap(bigger, heap_size)        

def heap_sort():
    build_heap()
    heap_size = DATA_LEN
    for i in range(1, DATA_LEN):
        swap(data, 1, heap_size)
        heap_size -= 1
        build_heap(heap_size)
            
data.insert(0, None)
heap_sort()
print(data)