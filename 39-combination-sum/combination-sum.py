class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index: int, current_sum: int, path: List[int]):
            if current_sum == target:
                res.append(path.copy())
                return
            if current_sum > target or index >= len(candidates):
                return
            path.append(candidates[index])
            backtrack(index, current_sum + candidates[index], path)
            path.pop()
            backtrack(index + 1, current_sum, path)
            
        backtrack(0, 0, [])
        return res