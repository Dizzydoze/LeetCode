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

## Solution

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """DFS, Backtracking, Target - Current, Begin index avoid repetition"""

        # candidates: can be used unlimited times, always the same
        # target: will be udpated to (target - current num) 
        # begin: skip all the previous elements at the same level, which has been calculated before
        def dfs(candidates, target, begin, path):
            # sorted candidates, no need to check the next bigger num
            if target < 0:
                return
            # match found, add path to res
            if target == 0:
                res.append(path)
                return
            # traverse on current level, skip the previous number, start at begin index
            #        2
            #   /   /  \   \
            #  2   3    6   7
            # when we start at 3, only need to check 3, 6, 7, begin index = 1
            # because results of 2 has been recorded
            for i in range(begin, n):
                # end the loop at current level, no need to check bigger nums
                if target - candidates[i] < 0:
                    break
                # a copy of new path contains current element
                # target - candidates[i]: the new target we're looking for
                # i: current index, avoid next dfs to check the previous elements before this one
                dfs(candidates, target - candidates[i], i, path + [candidates[i]])

        res = list()
        # sort, when target - current < 0, no need to check bigger number, break
        candidates.sort()
        n = len(candidates)
        dfs(candidates, target, 0, [])
        return res
```
