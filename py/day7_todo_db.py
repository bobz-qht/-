import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def load_todos():
    response = supabase.table("tasks").select("*").order("id").execute()
    return response.data


def save_todo(task_text):
    supabase.table("tasks").insert({"task": task_text}).execute()


def mark_done(task_id):
    supabase.table("tasks").update({"done": True}).eq("id", task_id).execute()


def delete_todo(task_id):
    supabase.table("tasks").delete().eq("id", task_id).execute()


def print_todos(todos):
    if not todos:
        print("할일이 없습니다.")
        return
    for todo in todos:
        status = "✅" if todo["done"] else "❌"
        print(f'[{todo["id"]}] {status} {todo["task"]}')


def main():
    while True:
        print("\n1. 할일 추가  2. 완료 처리  3. 목록 보기  4. 삭제  5. 종료")
        choice = input("선택: ")

        if choice == "1":
            task_text = input("할일 입력: ")
            save_todo(task_text)
            print("추가 완료")

        elif choice == "2":
            todos = load_todos()
            print_todos(todos)
            try:
                task_id = int(input("완료 처리할 항목의 [id] 입력: "))
                mark_done(task_id)
                print("완료 처리됨")
            except ValueError:
                print("숫자를 입력하세요.")

        elif choice == "3":
            todos = load_todos()
            print_todos(todos)

        elif choice == "4":
            todos = load_todos()
            print_todos(todos)
            try:
                task_id = int(input("삭제할 항목의 [id] 입력: "))
                delete_todo(task_id)
                print("삭제됨")
            except ValueError:
                print("숫자를 입력하세요.")

        elif choice == "5":
            break

        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
