"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        dict_roman_num = { 1 : "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        if(number < 0):
            print("number can not less than 0")
            return
        
        roman_text = ""
        for key in sorted(dict_roman_num.keys(), reverse=True):
            while number >= key:
                roman_text += dict_roman_num[key]
                number -= key
        print(roman_text)
        
        pass
    
number = int(input("Enter number: "))
sol = Solution()
sol.number_to_roman(number)
