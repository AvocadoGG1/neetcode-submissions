class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:
            # Shorter wall determines the height
            capped = min(heights[l], heights[r])

            # Distance between left and right determines width
            width = r - l

            # Rectangle area
            currArea = capped * width

            # print("left:", l, "right:", r)
            # print("height:", capped, "width:", width)
            # print("area:", currArea)

            if currArea > maxArea:
                maxArea = currArea

            # Move the shorter wall
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
