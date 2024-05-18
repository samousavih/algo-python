"""
Given a group of N people, each having a unique ID value from 0 to (N – 1) and an array arr[] of M elements of the form {U, V, time} representing that the person U will become acquainted with person V at the given time. Let’s say that person U is acquainted with person V if U is friends with V, or U is a friend of someone acquainted with V.
The task is to find the earliest time at which every person became acquainted with each other.

Examples:

Input: N = 4, arr[] = {{0, 1, 2}, {1, 2, 3}, {2, 3, 4}}
Output: 4
Explanation: Initially, the number of people are 4, i.e, {0}, {1}, {2}, {3}. 

At time = 2, {0} and {1} became friends. Therefore, the group of acquainted people becomes {0, 1}, {2}, {3}.
At time = 3, {1} and {2} became friends. Therefore, the group of acquainted people becomes {0, 1, 2}, {3}.
At time = 4, {2} and {3} became friends. Therefore, the group of acquainted people becomes {0, 1, 2, 3}.
Hence, at time = 4, every person became acquainted with each other.


Input: N = 6, arr[] = {{0, 1, 4}, {3, 4, 5}, {2, 3, 14}, {1, 5, 24}, {2, 4, 12}, {0, 3, 42}, {1, 2, 41}, {4, 5, 11}}
Output: 24


min heap
two hash tables 
one for ech set and one for membership
"""

from queue import PriorityQueue


def earliest_time(arr,N):
    minHeap = PriorityQueue()
    sets = {}
    inSet = {}
    lastSetNumber = 0
    for p in arr:
        minHeap.put((p[2],p))
    while not minHeap.empty():
        _,current = minHeap.get()
        first,second,time = current
        if first not in inSet and second not in inSet:
            inSet[first] = inSet[second] = lastSetNumber
            newSet = set()
            newSet.add(first)
            newSet.add(second)
            sets[lastSetNumber] = newSet
            lastSetNumber+=1
            if len(newSet) == N:
                return time
        elif first in inSet and second in inSet: 
              if inSet[first] != inSet[second]:
                    merge(first,second,sets,inSet)
                    if len(sets[inSet[first]]) == N:
                        return time
        elif first not in inSet:
              setId = inSet[first] = inSet[second]
              sets[setId].add(first)
              if len(sets[setId]) == N:
                return time
        else:
              setId = inSet[second] = inSet[first]
              sets[setId].add(second)
              if len(sets[setId]) == N:
                return time
    return 0

def merge(first,second,sets,inSet):
        firstSetId = inSet[first]
        secondSetId = inSet[second]
        firstSet = sets[firstSetId]
        secondSet = sets[secondSetId]
        if len(firstSet) < len(secondSet):
            firstSet,secondSet = secondSet,firstSet    
        firstSet = firstSet.union(secondSet)
        sets[firstSetId] = firstSet
        for item in list(secondSet):
            inSet[item] = firstSetId
        del sets[secondSetId]

print(earliest_time([(0, 1, 2), (1, 2, 3), (2, 3, 4)],4))
print(earliest_time([(0, 1, 4), (3, 4, 5), (2, 3, 14), (1, 5, 24), (2, 4, 12), (0, 3, 42), (1, 2, 41), (4, 5, 11)],6))

           
{0,1}
{3,4,5,2}








