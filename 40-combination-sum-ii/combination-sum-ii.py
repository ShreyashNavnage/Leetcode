class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start_idx: int, current_sum: int, path: List[int]):
            if current_sum == target:
                res.append(path.copy())
                return
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                    
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
        backtrack(0, 0, [])
        return res