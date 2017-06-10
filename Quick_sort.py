from random import randint

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p=randint(0, len(arr)-1)
        swap(arr, 0, p)
        arr, pi = partition(arr)
        arr[:pi] = quick_sort(arr[:pi])
        arr[pi+1:] = quick_sort(arr[pi+1:])
        return arr[:pi]+[arr[pi]]+arr[pi+1:]

def partition(arr):
    i=1
    pivot=arr[0]
    high=len(arr)-1
    for j in range(len(arr)-1):
        if arr[i]<=pivot:
            i+=1
        else:
            swap(arr, i, high)
            high-=1
    swap(arr, 0, i-1)
    return arr, i-1

A=[7,8,0,9,1,3,1]
print("Sorted Array is: ")
print(quick_sort(A))
