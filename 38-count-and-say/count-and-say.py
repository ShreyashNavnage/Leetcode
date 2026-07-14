class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            next_res = []
            count = 1
            for j in range(1, len(res)):
                if res[j] == res[j - 1]:
                    count += 1
                else:
                    next_res.append(str(count))
                    next_res.append(res[j - 1])
                    count = 1
            next_res.append(str(count))
            next_res.append(res[-1])
            res = "".join(next_res)
        return res