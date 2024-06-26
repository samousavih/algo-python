
"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

 

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
 

Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
"""

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # the timespan 1950-2050 covers 101 years
		delta = [0] * 101

		# to make explicit the conversion from the year (1950 + i) to the ith index
        conversionDiff = 1950 
		
        for l in logs:
			# the log's first entry, birth, increases the population by 1
            delta[l[0] - conversionDiff] += 1 
			
			# the log's second entry, death, decreases the population by 1
            delta[l[1] - conversionDiff] -= 1
        
        runningSum = 0
        maxPop = 0
        year = 1950
		
		# find the year with the greatest population
        for i, d in enumerate(delta):
            runningSum += d
			
			# since we want the first year this population was reached, only update if strictly greater than the previous maximum population
            if runningSum > maxPop:
                maxPop = runningSum
                year = conversionDiff + i
				
        return year