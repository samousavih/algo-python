"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

"""
def is_uniq(input):
	input.sort()
	i=1
	while i < len(input)-1:
		if input[i]==input[i-1] or input[i]==input[i+1]:
			return False
		i+=1
	return True

def test_is_uniq():
	assert is_uniq(["a","b","c","d"]) == True
	assert is_uniq(["a","b","c","b"]) == False

test_is_uniq() 
