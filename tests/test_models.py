from uuid import UUID
from app.models.result import TaskResult
from app.models.task import Task, TaskStatus
import pytest

def test_model():
    task = Task()

    assert isinstance(task.id, UUID)