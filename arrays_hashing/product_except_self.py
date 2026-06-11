class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1]*n
        pre = 1
        for i in range(n):
            answer[i] = pre
            pre *= nums[i]
        suf = 1
        for i in range(n-1,-1,-1):
            answer[i] *= suf
            suf *= nums[i]
        return answer 
    
"""
Notes: This is done in 2n, there is a 3n version.
    
Pattern:
Prefix/Postfix

Trigger:
For each index, I need information from the left side and the right side.

Move:
First pass stores product before each index.
Second pass multiplies by product after each index.

Bring forward:
When every answer depends on “everything before me” and “everything after me,” think prefix/suffix.

Core idea:
For each index i, the answer is:

    product of everything before i * product of everything after i

Instead of recomputing those products for every index, we do two passes:
1. Left to right: store prefix products in answer.
2. Right to left: multiply each answer[i] by the postfix product.


Time complexity:
O(n), because we make two passes through the array.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Pass 1: store prefix products in answer
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply by postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer    