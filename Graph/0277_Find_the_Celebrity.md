# Leetcode 0277. Find the Celebrity

## Problem Description
Suppose you are at a party with `n` people (labeled from `0` to `n - 1`, inclusive) and among them, there may exist one celebrity. The definition of a celebrity is that all the other `n - 1` people know him/her, but he/she does not know any of them.

You are given a helper function `bool knows(a, b)` which tells you whether `a` knows `b`. Implement a function `findCelebrity(n)`, your goal is to find out who the celebrity is or verify that there is not one. The helper function `knows` is defined as follows:

```python
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a: int, b: int) -> bool:

```

If there is a celebrity, return his/her label. If there is no celebrity, return `-1`.

## Solution
The logic is to eliminate non-celebrities by using the `knows` API.

1. First, you can find a candidate for celebrity by looping through all people. Start by assuming the first person (0) is the celebrity. For each person `i`, if the celebrity candidate knows `i`, then the candidate is not a celebrity and `i` could be the celebrity. Set `i` as the new celebrity candidate.
2. After this loop, you'll have a candidate for celebrity. But you need to check if the candidate really is a celebrity by ensuring two things:
    - The candidate doesn't know anyone.
    - Everyone knows the candidate.

Here's the Python code for this approach:

```python
def findCelebrity(n):
    # Step 1: Find the celebrity candidate.
    celebrity_candidate = 0
    for i in range(1, n):
        if knows(celebrity_candidate, i):
            celebrity_candidate = i

    # Step 2: Check if the candidate really is a celebrity.
    for i in range(n):
        if i != celebrity_candidate and (knows(celebrity_candidate, i) or not knows(i, celebrity_candidate)):
            return -1

    return celebrity_candidate

```

- This approach is based on the idea that once you determine that a person `a` knows a person `b`, you can be certain that `a` is not the celebrity (but `b` still might be).
- By the end of the loop, the `celebrity_candidate` might be the actual celebrity, but needs to be checked against the two conditions mentioned. If they don't hold true, then there's no celebrity in the party.