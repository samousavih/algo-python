def quick_sort(arr,start,end):
    if start>=end:
        return
    k = pivot(arr,start,end)
    quick_sort(arr,start,k)
    quick_sort(arr,k+1,end)

def pivot(arr,start,end):
    k = start
    low = k+1
    hi = end
    while low <= hi:
        if arr[low] > arr[k] and arr[hi] < arr[k]:
            swap(arr,low,hi)
            low+=1
            hi-=1
        elif arr[low] < arr[k]:
            low+=1
        else:
            hi-=1
    swap(arr, k, low-1)
    return low-1

def swap(arr,i,j):
    temp = arr[j]
    arr[j] = arr[i]          
    arr[i] = temp
         

def test_quick_sort():
    array = [5,3,6,9,12,6,6,25,0]
    array_copy = array.copy()
    quick_sort(array,0,len(array)-1)
    print(array)
    array_copy.sort()
    assert array == array_copy

test_quick_sort()