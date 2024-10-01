#https://leetcode.com/problems/roman-to-integer/description/
#13.Roman to Integer

# accidentally converted Int -> Roman
# class Solution(object):
#     def __init__(self):
#         pass
#     def romanToInt(self, s):
#         string = ""
#         roman_numerals = {
#             1: "I",
#             4: "IV",
#             5: "V",
#             9: "IX",
#             10: "X",
#             40: "XL",
#             50: "L",
#             90: "XC",
#             100: "C",
#             400: "CD",
#             500: "D",
#             900: "CM",
#             1000: "M"
#         }
#         for idx, numeral in enumerate(roman_numerals):
#             if s < numeral:
#                 count = idx-1
#                 break
#             count = 12
#         list_roman = list(roman_numerals)
#         while s > 0:
#             key = list_roman[count]
#             value = roman_numerals.get(key)
#             string += value
#             s-=key
#             while s < key and s > 0:
#                 count -= 1
#                 key = list_roman[count]
#         return string

# --- Correct solution
class Solution(object):
    def __init__(self):
        pass

    def romanToInt(self, s):
        roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        total = 0
        list_roman = list(roman_numerals.keys())[::-1]
        idx = 0
    
        while idx < len(s):
            for i, numeral in enumerate(list_roman):
                value = roman_numerals[numeral]
                if s[idx:idx + len(value)] == value:
                    total += numeral 
                    idx += len(value) 
                    break
        return total

s = "MCMXCIV"
answer = Solution()
result = answer.romanToInt(s)
print(result)

