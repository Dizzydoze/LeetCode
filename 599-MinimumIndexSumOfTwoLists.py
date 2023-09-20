class Solution:
    def findRestaurant(self, list1, list2):
        min_sum = 2000
        result = []
        # store all list1 items into hash table
        store = {string:idx for idx, string in enumerate(list1)}
        # check simliarity
        for i in range(len(list2)):
            if list2[i] in store:  # same string found
                if i + store[list2[i]] < min_sum:
                    min_sum = i + store[list2[i]]  # update min_sum
                    result = [list2[i]] # key point! reset for the smaller one
                elif i + store[list2[i]] == min_sum:
                    result.append(list2[i])
        return result
