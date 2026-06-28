class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        count = {}
        window = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            curr = s2[r]
            window[curr] = window.get(curr, 0)+ 1
            if r-l + 1 > len(s1):
                #delete left ch in window
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if window == count:
                return True
        return False

"""
Problem:
Permutation in String

Pattern:
Sliding window + frequency map.

Core idea:
I need to know whether s2 contains any substring that is an anagram of s1.

An anagram/permutation has the same character frequencies.

Because the substring must be the same length as s1, I use a fixed-size
sliding window of length len(s1).

Steps:
1. Count the characters in s1.
2. Slide a window across s2.
3. Add s2[right] to the window count.
4. If the window becomes longer than len(s1), remove s2[left] and move left.
5. If the window count equals s1_count, return True.
6. If no window matches, return False.

Why use a frequency map:
Order does not matter for permutations, but character counts do matter.

Time complexity:
O(n), where n is len(s2), assuming a fixed alphabet size.

Space complexity:
O(1), because there are at most 26 lowercase English letters.

Pattern trigger:
Question asks whether a string contains a permutation/anagram of another
string → frequency counts + sliding window.
"""