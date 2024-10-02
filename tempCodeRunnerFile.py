class Solution(object):
    def __init__(self):
        pass

    def longestCommonPrefix(self,strs):
        count = 1
        final = ""
        previous = strs[0][0]
        length = len(strs)
        flag = False
        loop = True
        while loop == True:
            flag = False
            count +=1
            for word in strs:
                letter = word[count]
                print(letter)
                print(previous)
                if previous == letter and flag == True:
                    previous = letter
                    print("PREVIOUS!")
                else:
                    return final
                if count == length:
                    print("HI!")
                    final += letter
                    loop = True
                flag = True

answer = Solution()
strs = ["flower", "flow", "flight"]
answer.longestCommonPrefix(strs)