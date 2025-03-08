class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        result = []
        zero_count = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1
        result.extend([0]*zero_count) 
        nums[:] = result    
