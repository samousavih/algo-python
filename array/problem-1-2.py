"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
s:ABCD
t1:BACD
t2:BAACD
t4:AECBD

"""

def is_perm(s,t):
	if len(s) != len(t):
		return False
	hash_table={}
	i = 0
	while i < len(s):
		hash_table[s[i]]=True
		i+=1
	j = 0
	while j < len(t):
		if hash_table.get(t[j]) is None:
			return False
		j+=1
	return True

def is_perm_optimised(s,t):
	if len(s) != len(t):
			return False
	chars = [0]*128

	i = 0
	while i < len(s):
			chars[ord(s[i])]+=1
			i+=1
	j = 0
	while j < len(t):
			chars[ord(s[j])]-=1
			if chars[ord(s[j])] < 0:
					return False
			j+=1
	return True

def test_is_perm():
	assert is_perm("ABCD","BACD") == True
	assert is_perm("ABACD","BAACD") == True
	assert is_perm("ABACD","BAAACD") == False
	assert is_perm("ABCD","BACED") == False
	assert is_perm_optimised("ABCD","BACED") == False
	assert is_perm_optimised("ABCD","BACD") == True
test_is_perm()

	
	
