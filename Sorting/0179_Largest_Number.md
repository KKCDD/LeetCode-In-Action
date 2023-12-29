# Leetcode 179. Largest Number

## Problem Description
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Example:
Input: nums = [3,30,34,5,9]
Output: "9534330"
Explanation: The largest formed number is 9534330.

## Solution
Python Solution:
```python
def largestNumber(nums):
    # Convert the numbers to strings
    nums = list(map(str, nums))

    # Define a custom comparator that compares the concatenations of two strings
    nums.sort(key=lambda x, y: cmp(y + x, x + y))

    # Concatenate the strings and remove leading zeros
    largest = ''.join(nums).lstrip('0')

    # Return the largest number, or "0" if it is zero
    return largest or "0"
```

Step-by-step explanation:
1. Convert the numbers to strings, as we need to compare them lexicographically.
2. Define a custom comparator that compares the concatenations of two strings. This ensures that the numbers are arranged in the order that forms the largest number.
3. Sort the strings using the custom comparator.
4. Concatenate the strings to form the largest number.
5. Remove leading zeros from the largest number, as they do not contribute to its value.
6. Return the largest number, or "0" if it is zero.

Complexity analysis:
- Time complexity: O(n log n), where n is the number of numbers. This is because we are sorting the numbers.
- Space complexity: O(n), as we are storing the numbers as strings.