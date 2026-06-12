class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###order doesnt matter, but if a large value is skipped on repetitive
        ###sequence ends. sorted = O(nlogn), so find another way to sort

        ###get rid of repetitive values, set.
        unique = set(nums)
        answer = 0
        
        for num in unique:
            if (num - 1) not in unique:
                curr = num
                length = 1
                #consider bigger values being included
                while curr + 1 in unique:
                    length += 1
                    curr += 1
                answer = max(length, answer)
        
        return answer
    
"""
Problem:
Longest Consecutive Sequence

Pattern:
Unsorted array + need to know whether values exist → use a set.
Set lookup + sequence starts.

Core idea:
The original order of nums does not matter. I only care whether
neighboring values exist somewhere in the array.

Why not sorting:
Sorting would make the consecutive sequence obvious, but sorting costs
O(n log n) not O(n).

Why use a set:
A set removes duplicates and gives O(1) average-time lookup for whether
a number exists.

Key insight:
Only start counting from the beginning of a sequence.

A number is the start of a sequence if:
    num - 1 not in unique

If num - 1 exists, then num is in the middle of a sequence, so starting
there would repeat work.

How the counting works:
Once I find a sequence start, I walk forward:
    curr, curr + 1, curr + 2, ...

I count how long that sequence is and update the longest answer.

Why loop through unique instead of nums:
nums can contain duplicates. Looping through unique avoids rechecking
the same number multiple times.

Time complexity:
O(n), because each number is checked in the set and sequences are only
expanded from their true starting points.

Space complexity:
O(n), because the set stores up to n unique values.
"""