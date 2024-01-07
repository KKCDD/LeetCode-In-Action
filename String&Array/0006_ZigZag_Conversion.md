# Leetcode 0006. ZigZag Conversion

## Problem Description
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

## Solution
```python
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        res = [''] * numRows
        index, step = 0, 1

        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(res)
```

Step-by-step Explanation: 
1. If the number of rows is 1 or greater than or equal to the length of the string, return the string.
2. Initialize a list `res` of empty strings with a length of `numRows`.
3. Initialize `index` and `step` to 0 and 1, respectively.
4. Iterate through the string. For each character, add it to the string at `index` in `res`. If `index` is 0, set `step` to 1. If `index` is `numRows - 1`, set `step` to -1. Then, increment `index` by `step`.
5. After the loop, join the strings in `res` and return the result.

Complexity Analysis: 
- Time complexity: O(n), where n is the length of the string. We need to iterate through the string once.
- Space complexity: O(n), because we need to store the result string.
