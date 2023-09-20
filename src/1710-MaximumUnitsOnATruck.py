class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        # switch unit and type then sort and reverse, biggest box at idx 0
        # sorted_box = [[unit, num] for(num, unit) in boxTypes].sort()
        # sorted_box = sorted_box[::-1]
        sorted_box = []
        for num, unit in boxTypes:
            sorted_box.append([unit, num])
        sorted_box.sort()

        # started with the biggest box [[unit, num]...]
        count = 0
        max_units = 0
        for i in range(len(sorted_box) - 1, -1, -1):
            while count < truckSize and sorted_box[i][1] > 0:
                max_units += sorted_box[i][0]
                sorted_box[i][1] -= 1  # reduced num of boxes used
                count += 1  # increase boxes loaded
        return max_units
