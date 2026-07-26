from pathlib import Path
import json
import uuid
try:
    import readline
except ImportError:
    import pyreadline3 as readline
BASE_DIR=Path(__file__).resolve().parent
DATA_DIR=BASE_DIR / "Data"
#이 함수는 cli 환경에서 메모를 수정가능하게 만들기 위해서 필요: input에서 플레이어가 입력하기 전에 특정 문자열을 밀어넣는다.
def bring_text(string):
    readline.insert_text(string)
    readline.redisplay()
# 이 함수는 메모를 작성할때 작성 유저마다 다른 메모 공간을 사용하고 유저들을 구분할 수 있기 위해 유저라는 클래스를 만들고 그 프로퍼티와 메서드를 넣었다.
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
    #메모를 작성해서 저장하게 하는 함수, 파라미터로 제목, 그 내용, 유저 자기자신을 항목으로 받음
    def make_memo(self,title:str,content:str):
        memo_id=str(uuid.uuid4()) # uuid는 겹치지 않는 문자열?을 생성해주는 기능, 이를 적용해서 새로운 메모를 작성할 때마다 고유한 번호를 부여, 이로써 나중에 제목이 같은 메모도 고유한 번호 식별로 수정 가능
        with open(DATA_DIR/"MemoData", "r",encoding="utf-8") as f:
            all_Data = json.load(f) # 메모를 생성할고 불러오거나 수정할때 각각의 메모 내용을 저장하고 로드하기 위해서는 어딘가에 내용 저장 필요, 이를 구현하기 위해 각 메모마다 다른 txt 파일에 저장가능, 나는 딕셔너리 json 형식으로 한 txt파일 안에 모든 유저의 메모를 저장함(지금 생각해보니 비효율적일거 같기도함) 
            all_Data.setdefault(self.__id,{})
            all_Data[self.__id][memo_id]={}
            all_Data[self.__id][memo_id]["content"]=content
            all_Data[self.__id][memo_id]["title"]=title
            self.save_memo(all_Data)
    def save_memo(self, all_data): #수정하거나 추가 한 내용을 기존txt 파일에 덮음으로써 저장
        with open(DATA_DIR/"MemoData", "w",encoding="utf-8") as f:
            json.dump(all_data, f, indent="\t", ensure_ascii=False)
    def edit_memo(self,memo_id,id):
        with open(DATA_DIR/"MemoData","r",encoding="utf-8") as f: # 메모를 수정하기 위해 구현해봄
            all_Data = json.load(f)
            if all_Data.get(id) is None:
                print("메모를 생성한 적이 없습니다.")
                return
            if all_Data[id].get(memo_id) is None:
                print("해당하는 메모가 존재하지 않습니다.")
                return
            print(f"--{all_Data[id][memo_id]["title"]}--")
            original_text=all_Data[id][memo_id]["content"]
            setup_text=lambda : bring_text(original_text) # 이 함수로 setup_text변수에 실행하면 input 받을때 bring_text(내용물) 이 내용물을 미리 입력된 값으로 설정하여, 텍스트 원본을 수정하는 듯 한 느낌주기 가능
            readline.set_startup_hook(setup_text) # 이 함수로 위에서 설정한 함수를 input 전에 실행하기 전에 실행하라고 예약 걸어둠
            try:
                input_text=input("content:")
            finally:
                readline.set_startup_hook(None) # 이거로 예약 풀기
            all_Data[id][memo_id]["content"]=input_text
            self.save_memo(all_Data)