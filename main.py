from user import User
def main():
    user = User()
    user.id="tester"
    while True:
        print("1. 메모하기  2. 종료")
        user_input = int(input("> "))
        print()

        match(user_input):
            case 1:
                print("메모할 내용을 적어주세요.")
                memo = input("> ")
                user.make_memo("test_memo",memo)
                print("메모가 저장되었습니다!\n")
                continue
            case 2:
                break
            case _:
                print("1~2 사이의 숫자를 입력해주세요.\n")
                continue
if __name__ == "__main__":
    main()