# https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes, truckSize) -> int:
        return self.getMaxUnits(boxTypes, truckSize)

    def getMaxUnits(self, boxTypes, truckSize):
        """
        use greedy and try to find the solution
        """
        # pre processing
        boxTypes = sorted(boxTypes, key=lambda boxType: boxType[1], reverse=True)
        tot_units = 0
        boxes = 0

        for i in boxTypes:
            # select in the order as the selction process is take max units first
            # optimisation measure is increase tot_units
            cur_boxes = i[0]
            cur_units = i[0] * i[1]
            if boxes + cur_boxes <= truckSize:
                tot_units += cur_units
                boxes += cur_boxes
            else:
                # do fraction
                rem_space = truckSize - boxes
                f_units = rem_space * i[1]
                tot_units += f_units
                break
        return tot_units
