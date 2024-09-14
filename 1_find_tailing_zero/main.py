"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            print("number can not be negative")
            return
        
        factorial = 1
        for i in range(1,number+1):
            factorial *= i
        print("factorial result: ",factorial)
        
        count = 0
        while factorial % 10 == 0:
            count += 1
            factorial = factorial // 10
        print("total of last zero digit: ", count)
        
        pass

number = int(input("Enter number: "))

sol = Solution()
sol.find_tailing_zeroes(number)