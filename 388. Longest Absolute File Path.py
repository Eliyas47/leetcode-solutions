class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        stack = {0: 0}  # depth -> cumulative length

        for line in input.split("\n"):
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name:  # it's a file
                max_len = max(max_len, stack[depth] + len(name))
            else:  # it's a directory
                stack[depth + 1] = stack[depth] + len(name) + 1
        return max_len
