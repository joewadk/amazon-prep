'''
questions taken from here: https://leetcode.com/discuss/interview-question/1826560/amazon-internship-sde-interviews-all-stages-all-questions
Q1. (Note borrowed from here, same OA question)
You are an amazon delivery and you have some boxes that you have to deliver, but there are some conditions -


You can take 2 boxes of same weight in one round
you can take 3 boxes of same weight in one round
You have to find the minimum number of rounds to deliver the boxes or -1 if it is not possible to deliver them.



Example cases -
Input: boxes - [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
Output: 4
Explanation: 3 boxes of weight 2 in 1st round, 2 boxes of weight 3 in 2nd round, 3 boxes of wt 4 in 3rd and 2 boxes of wt 4 in 4th round.


Input: boxes - [2, 3, 3]
Output: -1
Explanation: There is only one box with weight 2 and we can only take either 2 or 3 boxes in one round not lesser.
'''
def boxes():
    boxes = [2,2,2,2,3,4,4,4,3]
    hashm={} #frequency map
    import math
    for item in boxes: #populate our map
        if item not in hashm:
            hashm[item]=1
        else:
            hashm[item]+=1
    total=0
    for counts in hashm.values():
        if counts == 1: return -1 #base case
        total+= math.ceil(counts/3) #ensure that if its 4 or more, we get 2 boxes and not 1 (ie 2 trips of 2 boxes for 4)
    return total
print(boxes())
