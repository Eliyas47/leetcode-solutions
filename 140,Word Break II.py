class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(substring):
            if substring in memo:
                return memo[substring]
            if not substring:
                return [""]

            sentences = []
            for word in word_set:
                if substring.startswith(word):
                    suffixes = dfs(substring[len(word):])
                    for suffix in suffixes:
                        if suffix:
                            sentences.append(word + " " + suffix)
                        else:
                            sentences.append(word)
            memo[substring] = sentences
            return sentences

        return dfs(s)
