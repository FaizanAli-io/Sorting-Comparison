import time
import numpy as np
from sorters import QuickSort, MergeSort, HeapSort


def assert_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            return False
    return True


def test(iterations, array_size):
    algos = [QuickSort, MergeSort, HeapSort]
    times = [[func, 0] for func in algos]

    for i in range(iterations):
        data = np.random.rand(array_size)
        checks = np.array([], dtype=np.bool8)

        for j in range(len(times)):
            now = time.time()
            out = times[j][0](data.copy())
            times[j][1] += time.time() - now
            np.append(checks, assert_sorted(out))

        if np.all(checks):
            print(f"Iteration {i+1}")
        else:
            print("Failed")
    print()

    times.sort(key=lambda x: x[1])
    for i in range(len(times)):
        times[i] = [
            times[i][0].__name__,
            round(times[i][1] / iterations, 5),
        ]

    for item in times:
        print(f"{item[0]}: {item[1]}s")
    print()

    while len(times) > 1:
        fastest = times.pop(0)
        for item in times:
            mult = round(item[1] / fastest[1], 2)
            print(f"{fastest[0]} was {mult}x faster than {item[0]}")


test(50, 20000)
