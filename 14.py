#https://leetcode.com/problems/longest-common-prefix/
#14.Longest Common PRefix

class Solution(object):
    def __init__(self):
        pass

    def longestCommonPrefix(self,strs):
        count = 0
        tally = 1
        final = ""
        length = len(strs)
        flag = False
        loop = True
        while loop:
            flag = False
            leng = len(strs[0])
            if count >= leng:
                return final
            previous = strs[0][count]
            for word in strs:
                leng = len(word)
                if count >= leng:
                    return final
                letter = word[count]
                if previous == letter and flag:
                    previous = letter
                    tally += 1
                elif flag:
                    return final
                if tally == length:
                    tally = 1
                    final += letter
                    loop = True
                flag = True
            count += 1

answer = Solution()
strs = ["aaaa", "aaa", "aaa"]
hey = answer.longestCommonPrefix(strs)
print(hey)
