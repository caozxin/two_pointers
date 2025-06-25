class Solution:
    def maxArea(self, height: List[int]) -> int:
        #none handling:
        if not height:
            return 0

        n = len(height)
        left , right = 0, n - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            # print(left, right, area)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
