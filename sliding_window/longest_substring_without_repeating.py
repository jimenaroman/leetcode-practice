class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ###set to keeptrack fo duplicate, if duplicate start at r
        ###nvm .remove(s[l]) and add the same char?
        ###that doesnt make sense, keep that set and skip to next next letter, 
        ### so abc -> abca -> abcb 
    # lets just move l -> r
    ##save max length then l = r 
        l = 0 
        longest = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in longest:
                #Keep removing characters from the left side 
                #until the duplicate copy of s[r] is gone.
                longest.remove(s[l])
                l += 1
            longest.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
    
"""
Pattern:
Sliding window + set.

A substring is contiguous, so I can use a window:
    s[left : right + 1]

How the window moves:
- The right pointer expands the window by moving forward in the for loop.
- The left pointer shrinks the window only when the window becomes invalid.

I shrink only until the duplicate is removed.

Time complexity:
O(n), because each character is added to the set at most once and removed
from the set at most once.

Space complexity:
O(k), where k is the number of unique characters in the current window.
Worst case O(n).

Pattern trigger:
Longest/shortest substring or subarray with a condition → sliding window.

What I learned:
The right pointer usually expands the window.
The left pointer fixes the window when it breaks the rule.
For loops are useful for controlling the right pointer.
"""