"""
Given a book of words. Assume you have enough main memory to accommodate all words. 
design a data structure to find top K maximum occurring words.
The data structure should be dynamic so that new words can be added. 

Answer 1:
    Keep a HashMap for frequency and to find K max, build a max heap (O(uniq words)) and extract K max (O(klog(uw))) 

Answer 2:
    keep a HashMap for word index and frequency and a min heap with size K(assuming K is constant) with index and frequency

    as adding a word update the index in Hashmap and frequency, if updated frequency is less than the min, add the new one instead of min and sift down and then remove the last element.
"""
