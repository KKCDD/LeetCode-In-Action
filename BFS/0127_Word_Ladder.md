# Leetcode 0127. Word Ladder

## Problem Description
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

For example, given:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

## Solution
Python Solution:
```python
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0
```

Step-by-step explanation:
1. Convert the word list to a set for quick lookup, and check if the end word is in the word set.
2. Initialize a queue with the begin word and its length.
3. While the queue is not empty, pop a word and its length from the queue.
4. If the word is the end word, return its length.
5. Otherwise, for each position in the word, replace the character at that position with each letter from 'a' to 'z', and if the new word is in the word set, remove it from the word set and append it to the queue with its length increased by 1.
6. If no transformation sequence is found, return 0.

Complexity analysis:
- Time complexity: O(n*m^2), where n is the number of words in the word list and m is the maximum length of a word. This is because in the worst case, we need to visit each word and generate all possible next words by changing each character.
- Space complexity: O(n), because we need to store the word set and the queue.