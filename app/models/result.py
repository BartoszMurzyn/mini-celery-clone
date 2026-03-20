from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime, timezone
from app.models.task import TaskStatus, Task

class TaskResult(BaseModel):
    task_id: str
    status: TaskStatus
    result: Optional[Any] = None
    error: Optional[Any] = None
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))

    @classmethod
    def from_task(cls, task:Task):
        TaskResult.from_task(task)
