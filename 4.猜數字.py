import random


print("1-100 猜一數字，猜測次數五次")

random_number = random.randint(1,100)
guess_num = 0

while True:
    guess_num +=1
    if guess_num>=6:
        print("超出猜測次數")
        print(f"答答案是:{random_number}")
        break

    print(f"第{guess_num}次")
    user_guess = input("輸入數字:")
    if user_guess.isdigit():  #判斷是否為數字字串
        user_guess = int(user_guess)
    else:
        print("僅限輸入數字")
        continue  #跳回輸入數字

    if user_guess>random_number:
        print('小一點')
    elif user_guess<random_number:
        print('大一點')
    else:
        print("恭喜答對")
        break