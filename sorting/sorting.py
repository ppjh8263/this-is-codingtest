import os,sys
sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))))
        
from check_time import check_time

@check_time
def choice_sorting(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr 

@check_time
def insert_sorting(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
    return arr

# @check_time
def quick_sorting(arr,start,end):
    if start >= end:
        return arr
    pivot = start
    left = start + 1
    right = end
    while (left <= right):
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if(left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left],arr[right] = arr[right], arr[left]
    quick_sorting(arr, start, right-1)
    quick_sorting(arr, right+1, end)

    return arr

@check_time    
def quick(arr,start,end):
    return quick_sorting(arr,start,end)

@check_time    
def count_sorting(arr):
    count = [0]*(max(arr)+1)
    result=[]
    for i in range(len(arr)):
        count[arr[i]] += 1

    for idx, value in enumerate(count):
        result += [idx]*value

    return result


if __name__ == '__main__':
    arr = [7,5,9,0,1,6,2,4,8]
    print(choice_sorting(arr))
    print(insert_sorting(arr))
    print(quick(arr,0,len(arr)-1))
    print(count_sorting(arr))