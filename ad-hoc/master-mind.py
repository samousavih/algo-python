"""
The Game of Master Mind is played as follows:

The computer has four slots, and each slot will contain a ball that is red (R). yellow (Y). green (G) or blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).

You, the user, are trying to guess the solution. You might, for example, guess YRGB.

When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a pseudo-hit.

For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo-hit. Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.

Given a sequence of colors solution, and a guess, write a method that return the number of hits and pseudo-hit answer, where answer[0] is the number of hits and answer[1] is the number of pseudo-hit.

Example:

Input:  solution="RGBY",guess="GGRR"


Output:  [1,1]


Explanation:  hit once, pseudo-hit once.


Note:

len(solution) = len(guess) = 4
There are only "R","G","B","Y" in solution and guess.

"""

def master_mind(solution,guess):
    colors = {}
    sudo_hit = 0
    hit = 0
    for index,c in enumerate(solution):
        colors[c]=0
        if c == guess[index]:
            hit+=1
    for c in guess:
        if c in colors and colors[c] == 0:
            sudo_hit+=1
            colors[c]+=1
    return hit,sudo_hit-hit

print(master_mind("RGBY","GGRR"))