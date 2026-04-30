from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i: int, path: list[str]):
            if i == len(s):
                res.append("".join(path))
                return

            ch = s[i]

            if ch.isalpha():
                # lowercase branch
                path.append(ch.lower())
                dfs(i + 1, path)
                path.pop()

                # uppercase branch
                path.append(ch.upper())
                dfs(i + 1, path)
                path.pop()
            else:
                # digit branch (only one option)
                path.append(ch)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res
