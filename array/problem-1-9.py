"""
String Rotation; Assume you have a method is_substring which checks if one word is a substring of another.
Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to is_Substring [e.g., "waterbottle" is a rotation of'erbottlewat")
"""

def is_rotation(s1,s2):
	if len(s1) != len(s2):
		return False
	all_rotation = 2*s1
	print(all_rotation)
	return is_substring(s2,all_rotation)

def is_substring(s1,s2):
	return (s1 in s2)

def test_is_rotation():
	assert is_rotation("waterbottle","erbottlewat") == True

test_is_rotation()
	
