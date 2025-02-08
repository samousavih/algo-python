"""
Given a Singly linked list containing n nodes. The task is to reverse every group of k nodes in the list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed.

Example: 


Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL, k = 2 
Output: head: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> NULL 
Explanation : Linked List is reversed in a group of size k = 2.


Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL, k = 4 
Output: head:  4 -> 3 -> 2 -> 1 -> 6 -> 5 -> NULL
Explanation : Linked List is reversed in a group of size k = 4.


1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL

Start = 1  4-> 3-> 2->1
temp = 2



"""