todos = []

while True:
    print("\n1. 할일 추가")
    print("2. 할일 완료 처리")
    print("3. 목록 보기")
    print("4. 종료")
    choice = input("선택: ")
    
    if choice == "4":
        break

    if choice == "1":
        user_input = input("할 일을 입력하세요 (종료하려면 '그만' 입력): ")
        if user_input.lower() == '그만':
            break
        todos.append({"task": user_input, "done": False})

    elif choice == "2":
        task_index = int(input("완료할 할 일의 번호를 입력하세요: ")) - 1
        if 0 <= task_index < len(todos):
            todos[task_index]["done"] = True

    elif choice == "3":
        print("할 일 목록:")
        for todo in todos:
            status = "✅" if todo["done"] else "⬜"
            print(f"{status} {todo['task']}")

    else:
        print("잘못된 선택입니다. 1~4 중에 골라주세요.")
