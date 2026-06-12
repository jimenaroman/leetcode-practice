class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        a = start, goes up <b <c
        a<b<c
        c moves left, a moves right
        check for a duplicates on a and b .
        if a > 0 to make sure index not out of bounds
        if nums[a] > 0 , everything following is adding up to > 0.
        """
        ###order = sorted(nums)
        ###target = 0
        nums.sort()
        result = []
        for a in range(len(nums)):
            if nums[a] > 0:
                break

            if a > 0 and nums[a] == nums[a-1]: 
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                total = nums[a] + nums[b] + nums[c]
                if total == 0:
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b-1]:
                        # if duplicate b, move to next
                        b += 1
                elif total > 0:
                    c -= 1
                else:
                    b += 1

        return result
    
"""
Problem:
3Sum

Pattern:
Sort + fixed pointer + two pointers.

Core idea:
I need unique triplets where:

    a + b + c = 0

If I fix one number a, then the problem becomes:

    b + c = -a

That is basically Two Sum II on the rest of the sorted array.

Why sorting helps:
Sorting lets me use two pointers because:
- moving b right makes the sum larger
- moving c left makes the sum smaller

Sorting also places duplicate values next to each other, so I can easily skip them.

Duplicate logic:
    if a > 0 and nums[a] == nums[a - 1]:
        continue

This means:
If I already used this same value as the fixed a, skip it.


Time complexity:
O(n^2)

Why:
Sorting costs O(n log n). Then for each fixed a, b and c scan inward
across the rest of the array in O(n). Overall, O(n^2) dominates.

Space complexity:
O(1) extra space, not counting the output list.

What I learned:
Not every problem has an O(n) solution. 3Sum is expected to be O(n^2).
The goal is to improve from brute force O(n^3) to the standard optimized
approach.

Pattern trigger:
Need unique triplets or pairs that add to a target + sorting is allowed
→ sort, fix one value, then use two pointers.

Connection to previous problems:
Two Sum I:
Unsorted array + pair target → hashmap.

Two Sum II:
Sorted array + pair target → two pointers.

3Sum:
Sort array + fix one number + use Two Sum II on the rest.
"""
