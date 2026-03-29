class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        answer = 0
        longest = 0


        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[longest])
                longest +=1
            charSet.add(s[i])
            answer = max(answer, i - longest + 1)
            

        return answer