class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ### convert letter to lowercase
        ### remove all characters include only 65-90, including whiteppace
        clean = ""
        for ch in s.lower():
            ### letters and num stay
            if (ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 48 and ord(ch) <= 57):
                clean += ch
        reverse = clean[::-1]
        return clean == reverse

"""
Notes:

Problem:
Valid Palindrome

Pattern:
Two pointers / string filtering.

Core idea:
A palindrome reads the same forward and backward.

The problem says to ignore non-alphanumeric characters, so punctuation,
spaces, and symbols do not matter. Letters and numbers DO matter.


Important wording:
"Alphanumeric" means letters and digits:
- a-z
- A-Z
- 0-9

Simpler approach:
Build a cleaned lowercase string containing only alphanumeric characters,
then compare it to its reverse.

 clean == clean[::-1]

Time complexity:
O(n), because we scan the string once and reverse the cleaned string.

Pattern:
When a problem asks whether something reads the same forward and backward,
palindrome. A common solution is either:
1. clean + reverse + compare
2. two pointers from left and right


Cleaner version
isalnum() = is alphanumeric (letters or nums)
"""
class Solution(object):
    def isPalindrome(self, s):
        clean = ""

        for ch in s.lower():
            if ch.isalnum():
                clean += ch

        return clean == clean[::-1]
    

"""
Future improvement:
This problem can also be solved with two pointers by comparing the left
and right valid characters directly without building a cleaned string.

That version uses O(1) extra space.

left pointer starts at beginning
right pointer starts at end

skip invalid characters
compare valid characters
move inward
"""


class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            # move left until it points to a valid character
            while left < right and not s[left].isalnum():
                left += 1

            # move right until it points to a valid character
            while left < right and not s[right].isalnum():
                right -= 1

            # compare the actual valid characters
            if s[left].lower() != s[right].lower():
                return False

            # move both pointers inward
            left += 1
            right -= 1

        return True
