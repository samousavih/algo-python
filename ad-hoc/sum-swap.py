"""
Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two arrays the same sum.

Return an array, where the first element is the element in the first array that will be swapped, and the second element is another one in the second array. If there are more than one answers, return any one of them. 
If there is no answer, return an empty array.

Example:

Input: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]

Output: [1, 3]

Example:

Input: array1 = [1, 2, 3], array2 = [4, 5, 6]

Output: []
Note:

1 <= array1.length, array2.length <= 100000

Input: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
[1,1,1,2,2,4] , [3,3,3,6]
11 -1 + 3 = 11 + 2               15 -3 +1 = 15 - 2
diff  = 4 =>  - 2*(a+b) ==> diff - 2(a+b) = 0 => diff/2 = a+b
pickup a and do a binary search for diff/2-a    => O(NLogN ) + O(MLogN) and O(1 )

Better aproach create a set using one array an look for diff/2-a : O(N+M) and O(N) space

"""


def find_swap_values(A, B):
    # Find the sum of both the arrays
    sumA = sum(A)
    sumB = sum(B)

    # Check if the difference between the sum of both the arrays is even or not
    if (sumA - sumB) % 2 != 0:
        print("No Possible Pair exists")
        return

    # Set to store all the elements of A
    possibleX = set(A)

    # Iterate over all the elements of B and check if an
    # element with the value = X is present in A or not
    for Y in B:
        X = (sumA - sumB) // 2 + Y
        if X in possibleX:
            print(X, Y)
            return

    print("No Possible Pair exists")
