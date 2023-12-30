# Leetcode 0735. Asteroid Collision

## Problem Description
You are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

## Solution
Python Solution:
```python
def asteroidCollision(asteroids):
    stack = []
    for new in asteroids:
        while stack and new < 0 < stack[-1]:
            if stack[-1] < -new:
                stack.pop()
                continue
            elif stack[-1] == -new:
                stack.pop()
            break
        else:
            stack.append(new)
    return stack
```

Step-by-step explanation:
1. We initialize a stack to store the asteroids.
2. We iterate over the asteroids. If the current asteroid is moving to the left (new < 0) and the top asteroid in the stack is moving to the right (stack[-1] > 0), there will be a collision.
3. In the case of a collision, if the absolute value of the current asteroid is greater than the top asteroid in the stack, we pop the top asteroid from the stack and continue to the next iteration. If they are equal, we pop the top asteroid from the stack and break the inner loop. If the absolute value of the current asteroid is less than the top asteroid in the stack, we break the inner loop.
4. If there is no collision, we push the current asteroid onto the stack.
5. After iterating over all the asteroids, we return the stack as the final state of the asteroids.

Complexity analysis:
- Time complexity: O(n), where n is the number of asteroids. This is because we are traversing the asteroids once.
- Space complexity: O(n), where n is the number of asteroids. In the worst case, we will push all the asteroids onto the stack.