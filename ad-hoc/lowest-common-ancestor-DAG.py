"""
Problem: Lowest Common Ancestor in a Directed Acyclic Graph (DAG)

Given a DAG and two nodes, find the lowest common ancestor (LCA) of the two nodes. The LCA of two nodes v and w in a DAG is the deepest node that is an ancestor of both v and w.

Example:
Consider the following DAG:

    1
   / \
  2   3
 / \ / \
4   5   6

- The LCA of nodes 4 and 5 is 2.
- The LCA of nodes 4 and 6 is 1.
- The LCA of nodes 5 and 6 is 3.

Input:
- A list of edges representing the DAG.
- Two nodes for which the LCA needs to be found.

Output:
- The LCA of the two given nodes.

A,C

(A,B),(B,C) ==> reverse adjacent list
BFS(A) =>  keep order if finding node in HasMap
BFA(C) =>  lookup for common nodes 
[Node,(order reach from A, order reach from C)]
if no common nodes
return empty
if one node 
return one
if more than one node:
for eaxample above and starting from 6 and 3
S1: [(6,0,None), (3,1,0) , (1,2,1)] ==> 3
s2: [(6,0,None), (3,1,0) , (1,1,1)] ==> 3
s3: [(6,0,None), (5,0,None) , (2,1,1), (3,1,1)] ==> [2,3]

"""

