import json
from user import User

class UserManager:
    def __init__(self):
        self.user_list = []

    def find_user(self, id):
        for data in self.user_list:
            if id == data.id: 
                return data
        return 0

    def pw_correct(self, user, pw):
        if user.password == pw:
            return 1
        else : return 0
        
    def load_UserData(self):
        with open("Data/UserData.json", "r", encoding="utf-8") as f:
            datas = json.load(f)
            for data in datas:
                user = User(data["ID"], data["PASSWORD"])
                user.memo_list.append(data["MEMO"])
                self.user_list.append(user)
            
    def save_UserData(self):
        with open("Data/UserData.json", "w", encoding="utf-8") as f:
            data = [{"ID": item.id, "PASSWORD": item.password, "MEMO": item.memo_list} for item in self.user_list]
            json.dump(data, f, indent=4, ensure_ascii=False)
    