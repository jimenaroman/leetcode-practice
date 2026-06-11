## First attempt response:

class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        for key in nums: 
            if key not in count:
                count[key] = 0
            count[key] +=1
            if count[key] > 1:
                return True
        return False

""" 
Notes:
- Set stores unique values, does faster checks.
- This dict stores extra information

Correct Reasoning:

Create an empty collection of seen numbers.

For each number:
    If the number is already in the seen set:
        Duplicate exists -> True
    Otherwise:
        Add it to the seen set

    Loop finished, so there is no duplicate -> False

"""
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
"""

Even less information yet still O(n):

return len(nums) != len(set(nums))

"""