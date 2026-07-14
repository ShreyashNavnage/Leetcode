class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {} 
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in our map, we found our pair
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, add the current number and its index to the map
            num_map[num] = i
            
        return [] # Return empty list if no solution is found (though the problem guarantees one)
