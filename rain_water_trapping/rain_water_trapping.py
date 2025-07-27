from typing import List


# [4,2,0,3,2,5]
class TrappingRainWaterSolution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        # need atleast 3 height to trap
        if n <= 2:
            return res

        mono_stk = [0]

        # [0,1,0,2,1,0,1,3,2,1,2,1]

        # maintain elements idx in decreasing order of val
        for i in range(1, n):
            if (len(mono_stk) == 0) or height[mono_stk[-1]] > height[i]:
                mono_stk.append(i)
            else:
                # pop each smaller vals
                rt_height = height[i]
                rt_idx = i
                while mono_stk and height[mono_stk[-1]] < height[i]:
                    flr_idx = mono_stk.pop(-1)
                    flr_height = height[flr_idx]

                    if len(mono_stk) > 0:
                        lft_height = height[mono_stk[-1]]
                        lft_idx = mono_stk[-1]
                        # cal res
                        hyt = min(lft_height, rt_height) - flr_height
                        width = rt_idx - lft_idx - 1
                        res += width * hyt
                mono_stk.append(i)
        return res


input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
input = [4, 2, 0, 3, 2, 5]
print(TrappingRainWaterSolution().trap(input))
