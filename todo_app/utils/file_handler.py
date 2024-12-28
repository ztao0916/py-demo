import json
import os


class FileHandler:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.current_id = 0
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """确保文件存在，如果不存在则创建"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def load_todos(self):
        """从文件加载所有待办事项"""
        with open(self.filename, 'r') as f:
            data = json.load(f)
            if data:
                self.current_id = max(item['id'] for item in data)
            return data

    def save_todos(self, todos):
        """保存待办事项到文件"""
        with open(self.filename, 'w') as f:
            json.dump(todos, f, indent=2)

    def get_next_id(self):
        """获取下一个可用的ID"""
        self.current_id += 1
        return self.current_id
