letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

import random
print("密碼產生器")
upper_num = int(input("需要幾個大寫字母?\n"))
lower_num = int(input("需要幾個小寫字母?\n"))
number_num = int(input("需要幾個數字?\n"))
symbol_num = int(input("需要幾個符號?\n"))

password = ""
for i in range(0,upper_num):
    password += letters_upper[random.randint(0,25)]
for i in range(0,lower_num):
    password += letters_lower[random.randint(0,25)]
for i in range(0,number_num):
    password += numbers[random.randint(0,9)]
for i in range(0,symbol_num):
    password += symbols[random.randint(0,9)]

# 將密碼排列打散
password_list = list(password) # 將字串轉為陣列
random.shuffle(password_list) # 將密碼打散
new_password = "" 
for char in password_list: # 將陣列轉為字串
    new_password += char
print(new_password)