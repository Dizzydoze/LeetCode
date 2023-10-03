class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack, peek will always be the LOWEST temperature INDEX
        stack = list()
        # store the days to wait
        cnt = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # if stack is not empty and today temperature is higher than previous day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # i: today's index
                # stack[-1]: yesterday's index
                # i - stack[-1]: days to wait
                cnt[stack[-1]] = i - stack[-1]
                # pop out the index has been count
                stack.pop()
            # if stack is empty, push today temperature INDEX into stack
            # it is the LOWEST temperature INDEX for now
            stack.append(i)
        return cnt
