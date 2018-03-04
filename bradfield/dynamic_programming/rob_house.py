# ex nums: [4, 1, 1, 4]
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        f(0) = nums[0]
        f(1) = max(nums[0], nums[1])
        f(2) = max(f(0) + nums[2], f(1))
        f(k) = max(nums[k] + f(k - 2), f(k - 1))
        """
        # Initial maxes always start out like this
        cumulative_maxs = [ nums[0], max(nums[0], nums[1]) ]

        for i in range(2, len(nums)):
            # best could do if robbed current house
            robbed_current_house = cumulative_maxs[i - 2] + nums[i]
            # best could do if didn't rob current house
            didnt_rob_current_house = cumulative_maxs[i - 1]
            new_max = max(robbed_current_house, didnt_rob_current_house)
            cumulative_maxs.insert(i, new_max)

        return cumulative_maxs[-1]




s = Solution()
print(s.rob([4, 1, 1, 4]) == 8)
