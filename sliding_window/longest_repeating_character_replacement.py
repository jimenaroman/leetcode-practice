class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        best = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
    
"""
Problem:
Longest Repeating Character Replacement

Pattern:
Sliding window + frequency map.

For any window:
    replacements needed = window length - count of most frequent character

If replacements needed <= k:
    the window is valid

If replacements needed > k:
    shrink the window from the left

Why use a frequency map:
I need to know how many times each character appears in the current window.

Variables:
left = start of current window
right = end of current window
count = character frequencies inside the window
max_freq = count of the most frequent character in the window
best = longest valid window seen

Time complexity:
O(n), because right moves through the string once and left only moves forward.

Space complexity:
O(1), because the string uses uppercase English letters, so the dictionary
stores at most 26 characters.

Pattern trigger:
Longest substring/subarray with a condition + window can become invalid
→ sliding window.

What I learned:
Right expands the window.
Left shrinks the window when the condition breaks.
For this problem, the condition is:
    window length - max frequency <= k
"""