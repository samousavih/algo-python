"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.
"""

def find_in_sorted_matrix(matrix,m_start,m_end,n_start,n_end,x):
	if m_start > m_end or n_start > n_end:
		return None
	if m_end - m_start == 1 and n_end - n_start == 1:
		if matrix[m_start][n_start] == x:
			return (m_start,n_start)
		elif matrix[m_start][n_end] == x:
			return (m_start,n_end)
		elif matrix[m_end][n_start] == x:
			return (m_end,n_start)
		elif matrix[m_end][n_end] == x:
			return (m_end,n_end)
		else:
			return None
	m_mid = (m_start + m_end) //2
	n_mid = (n_start + n_end) //2
	if matrix[m_mid][n_mid] == x:
		return (m_mid,n_mid)
	if x > matrix[m_mid][n_mid]:
		bottom_right = find_in_sorted_matrix(matrix,m_mid,m_end,n_mid,n_end,x)
		if bottom_right is not None:
			return bottom_right
		bottom_left = find_in_sorted_matrix(matrix,m_start,m_mid,n_mid,n_end,x)
		if bottom_left is not None:
			return bottom_left
		top_right = find_in_sorted_matrix(matrix,m_mid,m_end,n_start,n_mid,x)
		if top_right is not None:
			return top_right
	else:
		top_left = find_in_sorted_matrix(matrix,m_start,m_mid,n_start,n_mid,x)
		if top_left is not None:
			return top_left
		top_right = find_in_sorted_matrix(matrix,m_mid,m_end,n_start,n_mid,x)
		if top_right is not None:
			return top_right
		bottom_left = find_in_sorted_matrix(matrix,m_start,m_mid,n_mid,n_end,x)
		if bottom_left is not None:
			return bottom_left
	return None

def test():
	m=[[1,1,2],[2,4,8],[9,10,12]]
	assert find_in_sorted_matrix(m,0,2,0,2,9) == (2,0)
	assert find_in_sorted_matrix(m,0,2,0,2,4) == (1,1)
	m=[[1,1,2,6],[2,4,8,9],[9,10,12,21],[12,18,19,25]]
	assert find_in_sorted_matrix(m,0,3,0,3,6) == (0,3)
	assert find_in_sorted_matrix(m,0,3,0,3,4) == (1,1)
test()