import backend.repositories.task_repo as repo

def create_task(name: str, date: str, is_critical: bool):
    if not name.strip():
        raise ValueError("Task name cannot be empty")

    repo.add_task(
        name=name.strip(),
        date=date,
        is_critical=is_critical
    )

def remove_task(task_id: int):
    rows_deleted = repo.delete_task(task_id)

    if rows_deleted == 0:
        raise ValueError("Task ID does not exist")

def get_tasks():
    return repo.fetch_tasks()