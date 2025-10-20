class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        res = []
        i=0
        for word in words:
        #     if x in words[i]:
        #         res.append(i)
            wordlen = len(word)
            for char in range(0, wordlen):
                if x ==word[char]:
                    res.append(i)
                    break
            i+=1
        return res

ob = Solution()
print(ob.findWordsContaining(["leet","code"]))
