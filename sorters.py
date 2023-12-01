import numpy as np


def BubbleSort(array):
    size = len(array)
    for i in range(size):
        swap = False
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break
    return array


def HeapSort(array):
    heapsize = len(array)

    for i in range(heapsize // 2, -1, -1):
        heapify(array, heapsize, i)

    for i in range(heapsize - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


def heapify(array, heapsize, root):
    largest = root
    left = root * 2 + 1
    right = root * 2 + 2

    if left < heapsize and array[left] > array[largest]:
        largest = left

    if right < heapsize and array[right] > array[largest]:
        largest = right

    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        heapify(array, heapsize, largest)


def QuickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot = partition(array, low, high)
        QuickSort(array, low, pivot - 1)
        QuickSort(array, pivot + 1, high)

    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def MergeSort(array):
    size = len(array)
    if size <= 1:
        return array

    middle = size // 2
    left = MergeSort(array[:middle])
    right = MergeSort(array[middle:])

    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    res = np.array([], dtype=np.float64)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            np.append(res, left[i])
            i += 1
        else:
            np.append(res, right[j])
            j += 1

    np.append(res, left[i:], 0)
    np.append(res, right[j:], 0)

    return res
