"""
4
[8,2,3,4,9,5,7]
[0,1,1,0,0,1,1]
[8,2,3]
[0,0,1]

"""

def binary_search_with_gap(k,array,gap):
    if len(array) == 0:
        return -1
    start = 0
    end = len(array)-1
    
    while start <= end:
        mid = (start+end)//2 # be careful about this, you are making too many mistakes here, dont forget parenthesis 
        if gap[mid] == 0:
            goLeft = mid-1
            goRight = mid+1
            while goLeft >= start or goRight <= end:
                if goLeft >= start and gap[goLeft] == 1:
                    mid = goLeft
                    break
                if goRight <= end and gap[goRight] == 1:
                    mid = goRight
                    break
                goRight+=1
                goLeft-=1
        if gap[mid] == 0:
            return -1
        if array[mid] == k:
            return mid
        if array[mid] > k:
            end = mid-1
        else:
            start = mid+1
    return -1
print(binary_search_with_gap(3,[8,2,3],[0,0,1]))
print(binary_search_with_gap(2,[8,2,3],[0,0,1]))
print(binary_search_with_gap(4,[8,2,3,4,9,5,7],[0,1,1,0,0,1,1]))