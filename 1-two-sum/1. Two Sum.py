class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersSeenAndIndices = {}
        for i,num in enumerate(nums):
            if target-num in numbersSeenAndIndices:
                return [numbersSeenAndIndices[target-num], i]
            else:
                numbersSeenAndIndices[num] = i

        return []