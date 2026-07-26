from pathlib import Path
import uuid
from prompt_toolkit import prompt
BASE_DIR=Path(__file__).resolve().parent
DATA_DIR=BASE_DIR / "Data"

#이 함수는 cli 환경에서 메모를 수정가능하게 만들기 위해서 필요: input에서 플레이어가 입력하기 전에 특정 문자열을 밀어넣는다.
def bring_text(string):
    readline.insert_text(string)

# 이 함수는 메모를 작성할때 작성 유저마다 다른 메모 공간을 사용하고 유저들을 구분할 수 있기 위해 유저라는 클래스를 만들고 그 프로퍼티와 메서드를 넣었다.
class User :
    def __init__(self, id, password):
        self.id = id 
        self.password = password
        self.memo_list = []

    #메모를 작성해서 저장하게 하는 함수, 파라미터로 제목, 그 내용, 유저 자기자신을 항목으로 받음
    def make_memo(self, title, content):
        memo_id = str(uuid.uuid4()) # uuid는 겹치지 않는 문자열?을 생성해주는 기능, 이를 적용해서 새로운 메모를 작성할 때마다 고유한 번호를 부여, 이로써 나중에 제목이 같은 메모도 고유한 번호 식별로 수정 가능
        data = {memo_id : {"title": title, "content": content}}
        self.memo_list.append(data)

    def edit_memo(self, memo_dic):
        print(f"--{memo_dic["title"]}--")
        original_text = memo_dic["content"]
        input_text = prompt("content: ", default=original_text)
        memo_dic["content"] = input_text

    def find_memo(self, memo_id):
        for item in self.memo_list:
            if item.get(memo_id):
                return item.get(memo_id)
        print("해당하는 메모가 존재하지 않습니다.") 
        return 0