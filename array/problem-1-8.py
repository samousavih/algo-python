"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

def set_row_col_zero(matrix,m,n):
	
	i = 0
	while i<n:
		j = 0
		if [i][0] != None:
			while j < m:
				if matrix[i][j] == 0:
					matrix[0][j] = None
					matrix[i][0] = None
				j+=1
		i+=1
	for i in reversed(range(n)):
		for j in reversed(range(m)):
			if matrix[0][j] == None or matrix[i][0] == None:
				matrix[i][j] = 0
	

def test_set_row_col_zero():
	matrix = [[1,1,1],[1,0,1],[1,1,1]]
	set_row_col_zero(matrix,3,3)
	print(matrix)
	assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

test_set_row_col_zero()

		
