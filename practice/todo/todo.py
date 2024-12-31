import json
from datetime import datetime
import os


class Task:  # 定义任务类
    def __init__(self, title, description):
        self.id = None  # 将在TodoList中设置
        # 任务标题
        self.title = title
        # 任务描述
        self.description = description
        # 创建时间默认设置为当前时间
        self.created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 完成状态默认设置为False
        self.completed = False

    def to_dict(self):  # 将任务对象转换为字典
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_time': self.created_time,
            'completed': self.completed
        }

    # 装饰器classmethod,语法: @classmethod
    # 定义一个类方法,绑定到类上,而不是类的实例,可以直接通过类名调用
    # 第一个参数cls,表示类本身,而不是类的实例
    @classmethod
    def from_dict(cls, data):  # 从字典创建任务对象
        task = cls(data['title'], data['description'])
        task.id = data['id']
        task.created_time = data['created_time']
        task.completed = data['completed']
        return task


class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks],
                      f, ensure_ascii=False, indent=2)

    def add_task(self, title, description):
        task = Task(title, description)
        task.id = len(self.tasks) + 1
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("\n暂无任务。")
            return

        print("\n当前任务列表:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task.completed else " "
            print(f"[{status}] {task.id}. {task.title}")
            print(f"   描述: {task.description}")
            print(f"   创建时间: {task.created_time}")
            print("-" * 50)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False


def main():
    todo_list = TodoList()

    while True:
        print("\n=== Todo 应用 ===")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")

        choice = input("\n请选择操作 (1-5): ")

        if choice == "1":
            title = input("请输入任务标题: ")
            description = input("请输入任务描述: ")
            todo_list.add_task(title, description)
            print("任务添加成功！")

        elif choice == "2":
            todo_list.list_tasks()
            input("\n按回车键返回主菜单...")

        elif choice == "3":
            todo_list.list_tasks()
            task_id = input("\n请输入要完成的任务ID: ")
            # 先检查输入的字符串中是否都是数字isdigit(),然后转换为整数
            if task_id.isdigit() and todo_list.complete_task(int(task_id)):
                print("任务已标记为完成！")
            else:
                print("无效的任务ID！")

        elif choice == "4":
            todo_list.list_tasks()
            task_id = input("\n请输入要删除的任务ID: ")
            if task_id.isdigit() and todo_list.delete_task(int(task_id)):
                print("任务已删除！")
            else:
                print("无效的任务ID！")

        elif choice == "5":
            print("感谢使用，再见！")
            break

        else:
            print("无效的选择，请重试。")


# __name__ 是Python的内置变量,用于表示当前模块的名称,当模块被直接运行时,__name__的值为__main__
# 如果模块被导入,则__name__的值为模块的名称
if __name__ == "__main__":
    main()
