"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        dic_t_num = { 1 : "หนึ่ง", 2: "สอง", 3: "สาม", 4: "สี่", 5: "ห้า", 6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า", 100: "ร้อย", 1000: "พัน", 10000: "หมื่น", 100000: "แสน", 1000000: "ล้าน"}
        if(number < 0):
            print("number can not less than 0")
            return
        
        number = str(number)
        num_text = ""
        for i in range(len(number)):
            if number[i] == "0":
                continue
            num_text += dic_t_num[int(number[i])] + dic_t_num[10**(len(number)-i-1)]
        print(num_text)
        
        pass

number = int(input("Enter number: "))

sol = Solution()
sol.number_to_thai(number)
