from uuid import UUID
from app.models.result import TaskResult
from app.models.task import Task, TaskStatus
import pytest
from datetime import datetime, timezone, timedelta

def is_recent(dt: datetime, seconds: float = 5.0) -> bool:
    assert dt.tzinfo is not None, "created_at powinien być timezone-aware (np. UTC)"
    now_utc = datetime.now(timezone.utc)
    delta = now_utc - dt
    return timedelta(0) <= delta <= timedelta(seconds=seconds)

def test_model():
    task = Task()

    # id jest UUID
    assert isinstance(task.id, UUID)
    # created_at: niedawny i timezone-aware (UTC)
    assert is_recent(task.created_at, seconds=5)
    # result i error
    assert task.result is None
    assert task.error is None
    assert task.status == "Pending"
