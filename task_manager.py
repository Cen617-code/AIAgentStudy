"""
简单的任务管理器 - 用于 Day 4 代码分析练习
"""

from datetime import datetime
from typing import Optional


class Task:
    """任务类"""

    def __init__(self, title: str, description: str = "", priority: int = 1):
        self.id = self._generate_id()
        self.title = title
        self.description = description
        self.priority = priority  # 1-5, 1最高
        self.completed = False
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None

    @staticmethod
    def _generate_id() -> str:
        """生成唯一ID"""
        return datetime.now().strftime("%Y%m%d%H%M%S")


class TaskManager:
    """任务管理器"""

    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, title: str, description: str = "", priority: int = 1) -> Task:
        """添加新任务"""
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: str) -> bool:
        """标记任务完成"""
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                task.completed_at = datetime.now()
                return True
        return False

    def delete_task(self, task_id: str) -> bool:
        """删除任务"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False

    def get_pending_tasks(self) -> list[Task]:
        """获取未完成的任务"""
        return [t for t in self.tasks if not t.completed]

    def get_by_priority(self, priority: int) -> list[Task]:
        """按优先级获取任务"""
        return [t for t in self.tasks if t.priority == priority]


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("学习 Claude Code", "完成7天学习计划", 1)
    manager.add_task("阅读文档", "查看官方文档", 2)
    task = manager.add_task("写代码", "练习 Python", 3)
    manager.complete_task(task.id)
    print(f"待完成任务: {len(manager.get_pending_tasks())}")