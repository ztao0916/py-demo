from datetime import datetime


class Todo:
    def __init__(self, title, description="", completed=False):
        self.id = None  # 将由文件处理器分配
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """将Todo对象转换为字典格式"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """从字典创建Todo对象"""
        todo = cls(data['title'], data['description'], data['completed'])
        todo.id = data['id']
        todo.created_at = data['created_at']
        return todo

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.title} - {self.description}"
