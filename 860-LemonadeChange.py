class Solution:
    def lemonadeChange(self, bills):
        dic = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                dic[10] += 1
                dic[5] -= 1
            else:
                dic[20] += 1
                # first handover $10 to save $5
                if dic[10] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                else:
                    dic[5] -= 3
            for count in dic.values():
                if count < 0:
                    return False
        return True
