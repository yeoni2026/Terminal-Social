from pathlib import Path
import json
import uuid
try:
    import readline
except ImportError:
    import pyreadline3 as readline
BASE_DIR=Path(__file__).resolve().parent
DATA_DIR=BASE_DIR / "Data"
def bring_text(string):
    readline.insert_text(string)
    readline.redisplay()
class User :
    def __init__(self):
        self.__id=None
        self.__password=None
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id_input:str):
        self.__id=id_input
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password_input:str):
        self.__password=password_input

    def make_memo(self,title:str,content:str):
        memo_id=str(uuid.uuid4())
        with open(DATA_DIR/"MemoData", "r",encoding="utf-8") as f:
            all_Data = json.load(f)
            all_Data.setdefault(self.__id,{})
            all_Data[self.__id][memo_id]={}
            all_Data[self.__id][memo_id]["content"]=content
            all_Data[self.__id][memo_id]["title"]=title
            self.save_memo(all_Data)
    def save_memo(self, all_data):
        with open(DATA_DIR/"MemoData", "w",encoding="utf-8") as f:
            json.dump(all_data, f, indent="\t", ensure_ascii=False)
    def edit_memo(self,memo_id,id):
        with open(DATA_DIR/"MemoData","r",encoding="utf-8") as f:
            all_Data = json.load(f)
            if all_Data.get(id) is None:
                print("메모를 생성한 적이 없습니다.")
                return
            if all_Data[id].get(memo_id) is None:
                print("해당하는 메모가 존재하지 않습니다.")
                return
            print(f"--{all_Data[id][memo_id]["title"]}--")
            #여기부터는 내일 할듯
            original_text=all_Data[id][memo_id]["content"]
            setup_text=lambda : bring_text(original_text)
            readline.set_startup_hook(setup_text)
            try:
                input_text=input("content:")
            finally:
                readline.set_startup_hook(None)
            all_Data[id][memo_id]["content"]=input_text
            self.save_memo(all_Data)