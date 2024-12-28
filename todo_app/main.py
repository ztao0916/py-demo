from models.todo import Todo
from utils.file_handler import FileHandler


class TodoApp:
    def __init__(self):
        self.file_handler = FileHandler()
        self.todos = []
        self.load_todos()

    def load_todos(self):
        """加载所有待办事项"""
        data = self.file_handler.load_todos()
        self.todos = [Todo.from_dict(item) for item in data]

    def save_todos(self):
        """保存所有待办事项"""
        data = [todo.to_dict() for todo in self.todos]
        self.file_handler.save_todos(data)

    def add_todo(self, title, description=""):
        """添加新的待办事项"""
        todo = Todo(title, description)
        todo.id = self.file_handler.get_next_id()
        self.todos.append(todo)
        self.save_todos()
        print(f"已添加待办事项: {todo}")

    def list_todos(self):
        """列出所有待办事项"""
        if not self.todos:
            print("没有待办事项")
            return

        print("\n待办事项列表:")
        for todo in self.todos:
            print(todo)

    def complete_todo(self, todo_id):
        """完成待办事项"""
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = True
                self.save_todos()
                print(f"已完成待办事项: {todo}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")

    def delete_todo(self, todo_id):
        """删除待办事项"""
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)
                self.save_todos()
                print(f"已删除待办事项: {todo}")
                return
        print(f"未找到ID为 {todo_id} 的待办事项")


def main():
    app = TodoApp()

    while True:
        print("\n=== TODO 应用 ===")
        print("1. 添加待办事项")
        print("2. 查看所有待办")
        print("3. 完成待办事项")
        print("4. 删除待办事项")
        print("5. 退出")

        choice = input("\n请选择操作 (1-5): ")

        if choice == "1":
            title = input("请输入标题: ")
            description = input("请输入描述 (可选): ")
            app.add_todo(title, description)

        elif choice == "2":
            app.list_todos()

        elif choice == "3":
            todo_id = int(input("请输入要完成的待办事项ID: "))
            app.complete_todo(todo_id)

        elif choice == "4":
            todo_id = int(input("请输入要删除的待办事项ID: "))
            app.delete_todo(todo_id)

        elif choice == "5":
            print("感谢使用！再见！")
            break

        else:
            print("无效的选择，请重试")


if __name__ == "__main__":
    main()
