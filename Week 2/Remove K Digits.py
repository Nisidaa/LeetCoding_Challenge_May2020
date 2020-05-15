# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


class Solution:
    def unic(self, digits, j):
        setdigits = set(digits)
        morethenk = set(range(j,10))

        if len(digits) == len(setdigits):
            for elem in setdigits:
                if int(elem) in morethenk:
                    return False
            return True
        else:
            return False

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        min = int(num)
        digits = "0" * k
        print(str(len(num)) * k)

        while digits != str(len(num)) * k:
            if self.unic(digits, len(num)):
                mod = num

                for j in range(k):
                    print(digits)
                    mod = mod[:int(digits[j])-j] + mod[int(digits[j])-j+1:]
                    print(mod)
                flag = False
                if int(mod) < min:
                    flag = True
                if flag:
                    min = int(mod)
            digits = str(int(digits)+1)
            digits = digits.zfill(k)

        return str(min)


print(Solution().removeKdigits("1234567890", 9))
