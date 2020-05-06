# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            result = True
            for j in range(len(s)):
                if i != j:
                    if s[i] == s[j]:
                        result = False
                        break
            if result:
                return i
        return -1


print(Solution().firstUniqChar('aaaaaabaaaa'))
