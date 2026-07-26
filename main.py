from user import User
from utils import get_safe_int, get_valid_str
from user_manager import UserManager

manager = UserManager()

manager.load_UserData()
while True:
    user_id = get_valid_str("ID를 입력해주세요.")
    user = manager.find_user(user_id)
    if user:
        while True:
            user_pw = get_valid_str("비밀번호를 입력해주세요.")
            if manager.pw_correct(user, user_pw):
                print("로그인 성공!\n")
                break
            else:
                print("비밀번호가 일치하지 않습니다.\n")
    else:
        print("존재하지 않는 ID입니다.\n")
        continue
    break

while True:
    user_input = get_safe_int("1.새 메모 2.메모 수정 3.종료")
    print()

    match(user_input):
        case 1:
            title = get_valid_str("메모 제목")
            content = get_valid_str("메모 내용")
            
            user.make_memo(title, content)
            print("메모가 저장되었습니다!\n")
        case 2:
            memo_id = get_valid_str("수정하고 싶은 메모의 id를 입력해주세요.")
            memo_dic = user.find_memo(memo_id)
            if not memo_dic:
                continue
            user.edit_memo(memo_dic)
            print("메모 수정이 완료되었습니다.\n")
        case 3:
            print("프로그램을 종료합니다.")
            manager.save_UserData()
            break
        case _:
            print("1~3 사이의 숫자를 입력해주세요.\n")