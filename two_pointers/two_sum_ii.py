class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        im thinking of having 2 pointers, L and R
        R must always > L
        check first thing if total is target to close loop.
        If its too big R gets smaller
        if its too small then increase L
        """
        l = 0
        r = len(numbers) - 1 
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            elif total > target:
                r -= 1
            else:
                l += 1


"""
Problem:
Two Sum II - Input Array Is Sorted

Pattern:
Sorted array + find a pair that meets a target → two pointers.

What to bring forward:
When the input is sorted and I need two values that interact, try placing
one pointer at the beginning and one at the end. Use the current result
to decide which side to move.

Core idea:
The array is sorted, so I can use the values at the left and right ends
to decide which pointer should move.

I start with:
    left = 0
    right = len(numbers) - 1

At each step:
    total = numbers[left] + numbers[right]

If total == target:
    I found the answer.

If total < target:
    The sum is too small, so I need a larger number.
    Since the array is sorted, I move left to the right.

If total > target:
    The sum is too large, so I need a smaller number.
    Since the array is sorted, I move right to the left.

Important detail:
The problem asks for 1-indexed positions, so I return:
    [left + 1, right + 1]

Why this works:
Because the array is sorted, moving left rightward always increases
or maintains the value, and moving right leftward always decreases
or maintains the value. This lets me eliminate impossible pairs without
checking every combination.

Bug to avoid:
Always handle the success case inside the loop.
If total == target and I do not return, neither pointer moves and the
loop can run forever.

Time complexity:
O(n), because each pointer moves inward at most n times total.

Space complexity:
O(1), because I only use two pointers and a total variable.
"""


