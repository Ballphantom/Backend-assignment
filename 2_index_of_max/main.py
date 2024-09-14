"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if(len(numbers) == 0):
            print("list can not blank")
            return
        
        max_value = numbers[0]
        temp = 0

        for i in range(1,len(numbers)):
            if numbers[i] > max_value:
                max_value = numbers[i]
                temp = i
        print("maximum number is on index at:", temp, ", with value:", max_value)
    pass

lst = []
number = int(input("Enter amount of array: "))

for i in range(0, number):
    ele = int(input("Enter number[%d]: " %i))
    lst.append(ele)

sol = Solution()
sol.find_max_index(lst)