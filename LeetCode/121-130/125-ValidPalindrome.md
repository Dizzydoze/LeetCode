# 125. Valid Palindrome

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return *`true` if it is a **palindrome**, or `false` otherwise*.

 

**Example 1:**

>**Input:** s = "A man, a plan, a canal: Panama"  
**Output:** true  
**Explanation:** "amanaplanacanalpanama" is a palindrome.  


**Example 2:**

>**Input:** s = "race a car"  
**Output:** false  
**Explanation:** "raceacar" is not a palindrome.  


**Example 3:**

>**Input:** s = " "  
**Output:** true  
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.  
Since an empty string reads the same forward and backward, it is a palindrome.
 

**Constraints:**

* `1 <= s.length <= 2 * 105`
* s consists only of printable ASCII characters.

## Two Pointers

Use isdigit, isalpha to check valid characters.

```python

class SolutionPractice:
    def isPalindrome(self, s: str) -> bool:
        # first loop clean up all non-alpha letters
        clean = list()
        for ch in s.lower():
            if ch.isdigit() or ch.isalpha():
                clean.append(ch)
        # two pointers
        l, r = 0, len(clean) - 1
        while l <= r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True
```

## Slice Reverse

```python
class SolutionOptimized:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for c in s.lower():
            if c.isalnum():
                clean += c
        return True if clean == clean[::-1] else False
```
