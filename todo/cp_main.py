class SimpleTodo:
    # 初始化方法,传入任务标题和描述,默认新增的任务未完成
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
