# じゃんけん

scissor = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
'''

import random   #引入模組
option = ["s","r","p"]
computer_choice = option[random.randint(0,2)] #random模組中的方法，在0到2隨機擇一

user_choice = input("please choose s(scissor) or p(paper) or r(rock)\n")
print("you choose:")
if user_choice == "s":
    print(scissor)
elif user_choice == "p":
    print(paper)
else:
    print(rock)

print("computer choose:")
if computer_choice == "s":
    print(scissor)
elif computer_choice == "p":
    print(paper)
else:
    print(rock)

if  (user_choice == "s" and computer_choice == "p") or\
    (user_choice == "r" and computer_choice == "s") or\
    (user_choice == "p" and computer_choice == "r"):
        print("you win!!")
elif (user_choice == "p" and computer_choice == "p") or\
    (user_choice == "s" and computer_choice == "s") or\
    (user_choice == "r" and computer_choice == "r"):
        print("try again!!")
else:
    print("you lose")