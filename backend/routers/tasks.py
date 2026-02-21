from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date

from backend.services.task_service import create_task, remove_task, get_tasks

router = APIRouter()


# ✅ Request Model
class Profile(BaseModel):
    name: str
    date: date
    mark: bool = False


# ✅ CREATE TASK
@router.post("/tasks")
def insert_task(data: Profile):
    try:
        create_task(
            name=data.name,
            date=str(data.date),   # convert to string
            is_critical=data.mark
        )
        return {"message": "task created successfully"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ✅ DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        remove_task(task_id=task_id)
        return {"message": "task deleted successfully"}

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")


# ✅ GET TASKS
@router.get("/tasks")
def fetch_tasks():
    try:
        return get_tasks()

    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")