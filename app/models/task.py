from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime, timezone
import uuid
from enum import Enum




class TaskStatus(str, Enum):
    PENDING= 'Pending'
    RUNNING= 'Running'
    DONE= 'Done'
    FAILED= 'Failed'

class Task(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
    result: Optional[Any] = None
    error: Optional[Any] = None
    status : TaskStatus = TaskStatus.PENDING

    function_name: str   
    args: list = Field(default_factory=list) 
    # kwargs: dict = Field(default_factory=dict) 

class TaskSubmit(BaseModel):
    function_name: str
    args: list = Field(default_factory=list) 
    # kwargs: dict = Field(default_factory=dict) 