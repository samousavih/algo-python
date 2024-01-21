def selection_k_largest(arr,k):
    
    low = 0
    hi = len(arr)-1

    while low <= hi:
        p = pivot(arr,low,hi)
        if k==p:
            return arr[p]
        elif k < p:
            hi = p-1
        else:
            low = p+1
    return arr[k]

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

def test_k_largest():
    array = [5,3,6,9,12,6,6,25,0]
    array_copy = array.copy()
    array_copy.sort()
    assert selection_k_largest(array,len(array)-1) == array_copy[len(array)-1]
    assert selection_k_largest(array,len(array)//2) == array_copy[len(array)//2]

test_k_largest()