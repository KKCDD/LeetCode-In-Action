# Leetcode 0299. Bulls and Cows

## Problem Description
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example:
Input: secret = "1807", guess = "7810"
Output: "1A3B"

## Solution 1
Python Solution:
```python
def getHint(secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
    return '%dA%dB' % (bulls, both - bulls)
```

Step-by-step explanation:
1. We calculate the number of bulls by comparing the secret and guess strings character by character.
2. We calculate the total number of matching characters (both bulls and cows) by counting the occurrences of each digit in the secret and guess strings, and taking the minimum count for each digit.
3. The number of cows is the total number of matching characters minus the number of bulls.
4. We return the hint as a string in the format 'xAyB', where x is the number of bulls and y is the number of cows.

Complexity analysis:
- Time complexity: O(n), where n is the length of the secret (or guess) string. This is because we are traversing the strings once to calculate the bulls and cows.
- Space complexity: O(1), as we are not using any extra space that scales with the size of the input.

## Solution 2
Here's a more readable Python solution for the problem:
```python
def getHint(secret, guess):
    bulls = 0
    cows = 0
    counter = [0]*10

    for i in range(len(secret)):
        s = int(secret[i])
        g = int(guess[i])
        if s == g:
            bulls += 1
        else:
            if counter[s] < 0:
                cows += 1
            if counter[g] > 0:
                cows += 1
            counter[s] += 1
            counter[g] -= 1

    return "{}A{}B".format(bulls, cows)
```

Step-by-step explanation:
1. We initialize counters for bulls and cows, and a list to keep track of the count of each digit.
2. We iterate over the digits in the secret and guess. If a digit in the secret is the same as the corresponding digit in the guess, we increment the count of bulls.
3. If the digits are not the same, we check the count of the secret digit and the guess digit in the counter. If the count of the secret digit is negative, it means the digit appears in the guess more times than in the secret, so we increment the count of cows. Similarly, if the count of the guess digit is positive, it means the digit appears in the secret more times than in the guess, so we increment the count of cows.
4. We then update the counts of the secret digit and the guess digit in the counter.
5. Finally, we return the counts of bulls and cows in the format 'xAyB'.

Complexity analysis:
- Time complexity: O(n), where n is the length of the secret (or guess) string. This is because we are traversing the strings once to calculate the bulls and cows.
- Space complexity: O(1), as we are using a fixed-size list to keep track of the count of each digit.