import json

# 定义主程序,创建一个无限循环


def main():
    while True:
        print("\n欢迎使用TodoList")
        print("1. 添加任务")
        print("2. 列出任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")
        choice = input("\n请输入你的选择(1-5): ")
        if choice == "1":
            # print("添加任务成功")
            add_task()
        elif choice == "2":
            list_tasks()
            # print("列出任务成功")
        elif choice == "3":
            # print("完成任务成功")
            complete_task()
        elif choice == "4":
            # print("删除任务成功")
            delete_task()
        elif choice == "5":
            print("退出成功")
            # 终止循环
            break
        else:
            print("无效的选择,请重试")

# 添加一个函数,用于添加任务


def add_task():
    title = input("请输入任务标题: ")
    description = input("请输入任务描述: ")
    # 需要把任务写入本地文件,先读取本地文件,看看新添加的标题是否存在,如果存在,则提示用户,
    # 如果不在, 则添加到本地文件, 本地文件的格式为json
    try:
        # 尝试读取文件,文件不存在则创建一个空列表
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
            print(tasks)
    except FileNotFoundError:
        # 如果文件不存在，创建一个空列表
        tasks = []

    # 检查任务是否存在
    if any(task["title"] == title for task in tasks):
        print("任务已存在")
    else:
        tasks.append({"title": title, "description": description,
                     "status": "未完成", "id": len(tasks) + 1})
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f)
        print("任务添加成功")


def list_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
        if not tasks:
            print("暂无任务")
        else:
            for task in tasks:
                if task['status'] == "完成":
                    print(
                        f"{task['id']}. [√] {task['title']}: {task['description']}")
                else:
                    print(
                        f"{task['id']}. {task['title']}: {task['description']}")
    except FileNotFoundError:
        print("暂无任务")

# 完成任务


def complete_task():
    # 完成任务需要输入任务的id, 然后修改任务的状态为完成,查看的时候,完成任务加个[√]
    id = int(input("请输入任务的id: "))
    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        for task in tasks:
            if task['id'] == id:
                task['status'] = "完成"
                break
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f)
    print("任务完成成功")

# 删除任务


def delete_task():
    # 删除任务需要输入任务的id, 然后删除任务, 查看的时候, 删除任务不显示
    id = int(input("请输入任务的id: "))
    with open('tasks.json', 'r', encoding='utf-8') as f:
        tasks = json.load(f)
        tasks = [task for task in tasks if task['id'] != id]
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f)
    print("任务删除成功")


# __name__是python内置变量,表示当前模块的名称,如果模块被直接运行,则__name__一定等于__main__
# 如果模块被导入,则__name__的值为模块的名称 语法: from 模块名 import 函数名
if __name__ == "__main__":
    main()
