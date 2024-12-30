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
            print("添加任务成功")
        elif choice == "2":
            print("列出任务成功")
        elif choice == "3":
            print("完成任务成功")
        elif choice == "4":
            print("删除任务成功")
        elif choice == "5":
            print("退出成功")
            # 终止循环
            break
        else:
            print("无效的选择,请重试")


# __name__是python内置变量,表示当前模块的名称,如果模块被直接运行,则__name__一定等于__main__
# 如果模块被导入,则__name__的值为模块的名称 语法: from 模块名 import 函数名
if __name__ == "__main__":
    main()
