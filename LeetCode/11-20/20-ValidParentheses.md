# 20-ValidParentheses

Given a string `s` containing just the characters `'(', ')', '{', '}', '['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

**Example 1:**

>**Input:** `s = "()"`  
**Output**: `true`


**Example 2:**

>**Input:** `s = "()[]{}"`    
**Output:** `true`  


**Example 3:**

>**Input:** `s = "(]"`  
**Output:** `false`
 

**Constraints:**

* `1 <= s.length <= 104`
* `s` consists of parentheses only `'()[]{}'`.


## Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        # KEY1: special case:
        if len(s) % 2 != 0:
            return False
        # stack store the left ones
        stack = []
        # use for match check
        dic = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        # )]} # check stack if there's a match
        for item in s:
            if item in dic:
                # empty stack or not match
                if not stack or stack[-1] != dic[item]:
                    return False
                # remove the matched one
                stack.pop()
            # ([{
            else:
                # add left ones to stack
                stack.append(item)
        # KEY2: check if there's sth left unmatched
        return not stack
```