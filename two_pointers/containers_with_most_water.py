class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        ###area = min( value out of height[l] and height[r]) * dist
        maxArea = 0
        while l < r:
            dist = r - l
            area = min(height[l], height[r]) * dist 
            maxArea = max(maxArea, area)
            ###decreasing distance, so now only heights matter for l or r
            if height[l] < height[r]:
                l +=1
            else: #if height[l] > height[r]:
                r -= 1
        return maxArea

""" 
Notes:

Pattern:
Two pointers.

Insight:
Since width gets smaller every time I move a pointer, the only way to
possibly find a larger area is to find a taller limiting wall.

That means I should move the pointer at the shorter wall.

If height[left] < height[right]:
    move left rightward

Else:
    move right leftward

Why not move the taller wall:
If I move the taller wall while keeping the shorter wall, the width gets
smaller and the limiting height stays the same. That cannot create a
better area.

Time complexity:
O(n), because each pointer moves inward at most n times total.

Space complexity:
O(1), because I only use two pointers and a few variables.

Pattern trigger:
Need to choose two positions in an array and the answer depends on both
positions plus the distance between them.
When I can start with the widest option and safely eliminate one side,
think two pointers from both ends.
"""