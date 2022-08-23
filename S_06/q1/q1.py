import multiprocessing
import time
from typing import List
import random


def merge(left, right, final):
    final.clear()
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            final.append(left[li])
            li += 1
        else:
            final.append(right[ri])
            ri += 1
    if li == len(left):
        final.extend(right[ri:])
    else:
        final.extend(left[li:])


def mergesort(array, arg=None):
    global onu_core, cores
    if len(array) < 2:
        if arg:
            for ind, i in enumerate(array):
                arg[ind] = i

    else:
        half = len(array) // 2
        left = array[:half]
        right = array[half:]
        if onu_core <= cores-4:
            onu_core += 2
            manager = multiprocessing.Manager()
            return_arr = manager.list(range(len(left)))
            return_arr_1 = manager.list(range(len(right)))
            th1 = multiprocessing.Process(target=mergesort, args=(left, return_arr))
            th2 = multiprocessing.Process(target=mergesort, args=(right, return_arr_1))
            th1.start()
            th2.start()
            th1.join()
            th2.join()
            left = return_arr
            right = return_arr_1

        else:
            mergesort(left)
            mergesort(right)

        merge(left, right, array)

        if arg:
            for ind, i in enumerate(array):
                arg[ind] = i


# [12, 13, 11, 5, 3, 10, 6, 4, 35, 58, 1, 9, 5, 7, 28]
if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(n):
        li.append(random.randint(0, n))

    arr: List[int] = li.copy()
    onu_core = 1
    cores = multiprocessing.cpu_count()
    st = time.perf_counter()
    mergesort(arr)
    en = time.perf_counter()
    print("Sorted array is: ", end="\n")
    # print(arr)
    print("time to calculate :", en-st, sep="\n")
    li.sort()
    if arr == li:
        print("the order of values in list is Correct and checked.")
    else:
        print("the order of values in list is Uncorrected and checked.")
    open("all time.txt", "a").write(f"{len(arr)} :  {en-st}\n")
