# Leetcode 56. Merge Intervals

## Problem Description
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example: Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]] Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

## Solution
```python
def merge(intervals):
    # Sort the intervals by their start times
    intervals.sort(key=lambda x: x[0])

    # Initialize the result list with the first interval
    res = [intervals[0]]

    # Iterate over the intervals, starting from the second one
    for i in range(1, len(intervals)):
        # If the current interval's start time is less than or equal to the last interval's end time in the result list
        if intervals[i][0] <= res[-1][1]:
            # Merge the intervals by updating the end time of the last interval in the result list
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            # If the intervals do not overlap, add the current interval to the result list
            res.append(intervals[i])

    return res
```

Step-by-step explanation:
1. Sort the intervals by their start times. This ensures that we can merge all overlapping intervals in one pass.
2. Initialize the result list with the first interval.
3. Iterate over the intervals, starting from the second one.
4. For each interval, if its start time is less than or equal to the end time of the last interval in the result list, merge the intervals by updating the end time of the last interval in the result list. This is because the intervals overlap.
5. If the intervals do not overlap, add the current interval to the result list.
6. Return the result list.

Complexity analysis:
- Time complexity: O(n log n) due to the sorting of the intervals. The merging process takes linear time, so the overall time complexity is dominated by the sorting.
- Space complexity: O(1) or O(n), depending on whether the sort operation is in-place. In Python, the sort function for lists is not in-place, so the space complexity is O(n).