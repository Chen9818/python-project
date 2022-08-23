eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

import random
question_num = int(input("請問要做幾題?"))

question = list(eng_dic)
score = 0
for i in range(1,question_num+1):
    random_question = question[random.randint(0,len(question)-1)]
    print(f"第{i}題")
    ans = input(f"請問{random_question}的英文是?")
    if ans == eng_dic[random_question]:
        print("恭喜答對")
        score += 1
    else:
        print(f"答錯，答案是{eng_dic[random_question]}")

print(f"總共{question_num}題，答對{score}題")