"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
 Given two strings, write a function to check if they are one edit (or zero edits) away.
pale, ple -> true
pales,pale -> true
pale, bale -> true
pale, bae -> false
"""

"""
pae, pamne

"""

def is_one_away(s,t):
	if abs(len(s)-len(t))>1:
		return False
	i=0
	j=0
	dist=0
	while i < len(s) and j < len(t):
		if dist > 1:
			return False
		if s[i] != t[j]:
			if i < len(s)-1 and s[i+1] == t[j]:
				dist+=1
				i+=1
			elif j < len(t)-1 and s[i] == t[j+1]:
				dist+=1
				j+=1
			else:
				dist+=1
				i+=1
				j+=1
			
				
		else:
			i+=1
			j+=1
	return True


def test_is_one_way():
	assert is_one_away("pae","pamne") == False
	assert is_one_away("pale","ple") == True
	assert is_one_away("pales","pale") == True
	assert is_one_away("pale","bae") == False
	assert is_one_away("pale","bale") == True	

test_is_one_way()
			 
 
