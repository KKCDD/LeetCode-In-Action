# Leetcode 1472. Design Browser History

## Problem Description
Design your implementation of the browser history. Your browser history is initialized with your homepage. You can visit(url), back(steps), and forward(steps).

- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
- void visit(string url) Visits url from the current page. It clears up all the forward history.
- string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
- string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will return only x steps. Return the current url after forwarding in history at most steps.

## Solution
Python Solution:
```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
```

Step-by-step explanation:
1. We initialize a list to store the history and a variable to store the current index.
2. When we visit a url, we remove all the urls after the current url from the history, append the new url to the history, and increment the current index.
3. When we go back, we decrement the current index by the given steps but not less than 0, and return the current url.
4. When we go forward, we increment the current index by the given steps but not more than the length of the history minus 1, and return the current url.

Complexity analysis:
- Time complexity: O(1) for the visit, back, and forward operations. This is because we are performing a constant number of operations.
- Space complexity: O(n), where n is the number of urls visited. This is because we store all the urls in the history.