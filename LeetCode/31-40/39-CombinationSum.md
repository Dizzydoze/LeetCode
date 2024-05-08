# 39. Combination Sum

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`*. You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the 
**frequency** of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

 

**Example 1:**

>**Input:** `candidates = [2,3,6,7], target = 7`  
**Output:** `[[2,2,3],[7]]`

**Explanation:**
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.  
7 is a candidate, and 7 = 7.  
These are the only two combinations.  


**Example 2:**

>**Input:** `candidates = [2,3,5], target = 8`  
**Output:** `[[2,2,2,2],[2,3,3],[3,5]]`

**Example 3:**

>**Input:** `candidates = [2], target = 1`  
**Output:** `[]`
 

**Constraints:**

* `1 <= candidates.length <= 30`
* `2 <= candidates[i] <= 40`
* All elements of `candidates` are **distinct**.
* `1 <= target <= 40`


## Pattern
1. SUM: intuition to do **deduction** with **remainder**.
2. startIndex: always use it to **skip** previous elements at **CURRENT LEVEL**
3. reused: for current number, all the recursion **set(candidates)** stays the same.
4. leave cutting: remain < 0, combination exceeds target.

## Backtracking(elements reused)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking
        # sum: intuition should be deduction using remainder
        # startIndex: always use it to skip previous elements at CURRENT LEVEL
        def backtrack(remain, path, start):
            # combination exceeds the target
            if remain < 0:
                return
            # base case: target combination found
            if remain == 0:
                res.append(path.copy())
            # combination sum still < target
            for i in range(start, len(candidates)):
                # leave cutting, must sort the candidates, no need to check bigger nums
                if remain - candidates[i] < 0:
                    break
                path.append(candidates[i])

                # KEY: startIndex doesn't change, elements can be reused
                backtrack(remain - candidates[i], path, i)
                path.pop()

        res = []
        candidates.sort()
        # 1. start from target, do deduction on the way
        # 2. traverse on CURRENT LEVEL, skip the previous number, start at begin index
        #        2
        #   /   /  \   \
        #  2   3    6   7
        # when we start at 3, only need to check 3, 6, 7, begin index = 1
        # because results of 2 has been recorded
        # 3. for each round, the candidates stay the same(reusage)
        backtrack(target, [], 0)
        return res

```
