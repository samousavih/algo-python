def merge_sort_recursive(array,start,end):
    if(start >= end): 
        return
    mid = (end+start)//2
    merge_sort_recursive(array,start,mid)
    merge_sort_recursive(array,mid+1,end)
    merge(array,start,mid,end)
def merge(array,start,mid,end):
    i = start
    j = mid+1
    temp_array = []
    for element in array:
        temp_array.append(element)
    for k in range(start,end+1):
        if i > mid and j <= end:
            array[k] = temp_array[j]
            j+=1
        if j > end and i <= mid:
            array[k] = temp_array[i]
            i+=1
        elif j <= end and i <= mid: 
            if temp_array[i] <= temp_array[j]:
                array[k] = temp_array[i]
                i+=1
            else:
                array[k] = temp_array[j]
                j+=1

def merge_sort_bottom_up(array):
    size=2
    while size//2 <= len(array):
        n=0
        while n <= len(array):
            start = n
            end = (n+size-1)
            if end >= len(array):
                end = len(array)-1
            mid = (start+end)//2
            merge(array,start,mid,end)
            n+=size
        size*=2


def test_merge_sort():
    array = [5,3,6,9,12,25,0]
    array_copy = array.copy()
    merge_sort_recursive(array,0,len(array)-1)
    array_copy.sort()
    assert array == array_copy
def test_merge_sort_bottom_up():
    array = [5,3,6,9,12,25,0]
    array_copy = array.copy()
    merge_sort_bottom_up(array)
    array_copy.sort()
    assert array == array_copy

test_merge_sort()
test_merge_sort_bottom_up()