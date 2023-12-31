# Leetcode 1423. Maximum Points You Can Obtain from Cards

## Problem Description
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints. In one step, you can take one card from the beginning or the end of the row. You have to take exactly k cards. Your score is the sum of the points of the cards you have taken. Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

## Solution
```python
class Solution:
    def maxScore(self, cardPoints, k):
        total = sum(cardPoints)
        n = len(cardPoints)
        size = n - k
        minSubArraySum = float('inf')
        currentSubArraySum = 0

        for i in range(n):
            if i >= size:
                minSubArraySum = min(minSubArraySum, currentSubArraySum)
                currentSubArraySum -= cardPoints[i - size]
            currentSubArraySum += cardPoints[i]

        minSubArraySum = min(minSubArraySum, currentSubArraySum)
        return total - minSubArraySum
```

Step-by-step Explanation: 
1. Calculate the total sum of the card points.
2. Initialize the size of the subarray to be the total number of cards minus k.
3. Initialize the minimum subarray sum to be infinity and the current subarray sum to be 0.
4. Iterate through the card points. For each card point, if the index is greater than or equal to the size of the subarray, update the minimum subarray sum and subtract the card point at the beginning of the current subarray from the current subarray sum.
5. Add the current card point to the current subarray sum.
6. After the loop, update the minimum subarray sum one last time.
7. Return the total sum of the card points minus the minimum subarray sum.

Complexity Analysis: 
- Time complexity: O(n), where n is the number of cards. We need to iterate through the card points once.
- Space complexity: O(1), because we only use a constant amount of space to store the variables `total`, `size`, `minSubArraySum`, and `currentSubArraySum`.