class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h and h[complement] != i:
                return [min(i, h[complement]), max(i, h[complement])]
            else:
                h[nums[i]] = i
        return []