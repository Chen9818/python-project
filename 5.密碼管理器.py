import json

def get_password_dic():
    with open("password.json","r") as f:
        password_str = f.read()
        if password_str == "":  #json.read讀取時，json檔不可為空，所以如果為空，回傳{}
            return {}
        else:
            return json.loads(f.read()) #讀取時，json檔轉字串 

def check_name(name): #防止重複輸入帳號名稱
    password_dic = get_password_dic()
    if name in password_dic.keys():         #password.keys()會顯示password內的key 例:[google,fb,...]
        return False  #已有帳號名稱                     #in可以檢查name是否在array內 回傳布林值
    else:
        return True   #無帳號名稱


def add_password(name,account,password):
    if check_name(name):    #true
        password_dic = get_password_dic()
        password_dic[name] = {
            "account":account,
            "password":password
        }
        with open("password.json","w") as f:
            f.write(json.dumps(password_dic))  #寫入時，字串轉json
        return True
    else:
        return False

while True:
    mode = input("請請問要使用甚麼模式?(r查詢  a新增  q離開):")
    if mode == "q":
        break
    elif mode == "a":
        name = input("輸入帳號名稱:")
        account = input("輸入帳號:")
        password = input("輸入密碼:")
        if add_password(name,account,password):
            print("新增成功")
        else:
            print("已有此帳號名稱")
    elif mode == "r":
        name = input("輸入帳號名稱:")
        if check_name(name):
            print("無此帳號名稱")
        else:
            password_dic = get_password_dic()
            account = password_dic[name]["account"]
            password = password_dic[name]["password"]
            print(f"帳號:{account},密碼:{password}")
