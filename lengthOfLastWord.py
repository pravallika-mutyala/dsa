class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n= len(s)
        count = 0
        for i in range(n-1, -1,-1):
            if s[i]!=" ":
                count +=1
                # print(s[i])
            if count>0 and s[i] == " ":
                break
        return count


obj = Solution()
print(obj.lengthOfLastWord("hello world"))
