#https://leetcode.com/problems/palindrome-number/description/
#9. Palindrome Number
#Runtime: 51ms
import time
start_time = time.time()

class Solution(object):
    def __init__(self, x):
        self.x = x
    def isPalindrome(self, x):
        x = str(x)
        order = []
        reverse = []
        for char in x:
            order.append(char)
        length = len(order)
        count = length - 1
        for i in range(0, length):
            reverse.append(order[count])
            count -= 1
        if order == reverse:
            return True
        return False

x = 14441
answer = Solution(x)
result = answer.isPalindrome(x)
print(result)

#7ms solution
# class Solution(object):
#     def isPalindrome(self, x):
#         i=str(x)
#         return i==i[::-1]
    