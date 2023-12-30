# Leetcode 0049. Group Anagrams

## Problem Description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Solution
Python Solution:
```python
def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())
```

Step-by-step explanation:
1. We create a dictionary to store the anagram groups. The keys are sorted words and the values are lists of words that are anagrams of the sorted word.
2. For each word in the array, we sort the characters in the word and use the sorted word as the key.
3. If the sorted word is already in the dictionary, we append the word to the corresponding list. If it's not in the dictionary, we add a new entry with the sorted word as the key and a list containing the word as the value.
4. Finally, we return the lists of anagrams.

Complexity analysis:
- Time complexity: O(n*m*log(m)), where n is the number of words in the array and m is the maximum length of a word. This is because we sort each word, which takes O(m*log(m)) time, and we do this for each word.
- Space complexity: O(n*m), as we store all words in the dictionary.