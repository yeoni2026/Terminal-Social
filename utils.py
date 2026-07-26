def get_safe_int(prompt):
    while True:
        try:
            return int(input(f"{prompt}\n> ")) 
        except ValueError:
            print("숫자만 입력할 수 있습니다. 다시 입력해주세요.\n")

def get_valid_str(prompt):
    while True:
        text = input(f"{prompt}\n> ")
        if text.strip():
           return text