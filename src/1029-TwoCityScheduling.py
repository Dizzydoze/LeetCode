class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        # Send all man to A
        costs_a = sum([a for a, b in costs])
        # Check if there's a refund sending the same guy to B
        refunds = [b - a for a, b in costs]
        # Sort the refunds
        refunds.sort()
        # Meaning: If we send first N person to B, we save the most amount of money
        # b - a < 0, we save money by sending the same guy to B
        # b - a > 0, the sorted price is still cheapest compare to the rest of guys
        return costs_a + sum(refunds[:n])
