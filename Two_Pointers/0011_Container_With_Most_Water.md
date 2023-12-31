# Leetcode 0011. Container With Most Water

## Problem Description
Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

## Solution
Python Solution using Two Pointers:
```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

Step-by-step explanation:
1. We initialize two pointers, left and right, to the start and end of the array.
2. We initialize `max_area` to 0.
3. We enter a loop that continues until left is less than right.
4. We calculate the height `h` as the minimum of the heights at the left and right pointers, and the width `w` as the difference between the right and left pointers.
5. We update `max_area` if `h * w` is greater than `max_area`.
6. If the height at the left pointer is less than the height at the right pointer, we move the left pointer to the right. Otherwise, we move the right pointer to the left.
7. We return `max_area`.

Complexity analysis:
- Time complexity: O(n), where n is the number of elements in the array. This is because we are traversing the array once.
- Space complexity: O(1). This is because we are using a constant amount of space.