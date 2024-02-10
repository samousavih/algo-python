"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


"""

def compress(s):
	i=0
	compressed=""
	while i < len(s)-1:
		n_reps=1
		compressed+=s[i]
		while i < len(s)-1 and s[i] == s[i+1]:
			n_reps+=1
			i+=1
		i+=1
		compressed+=str(n_reps)
	if len(compressed) < len(s):
		return compressed
	else:
		return s

def test_compress():
	assert compress("aabcccccaaa") == "a2b1c5a3"

test_compress()
		
 
