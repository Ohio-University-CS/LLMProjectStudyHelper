def delete_task(tasks, task_index):
    if(task_index >= len(tasks)):
        return {
            "status": "error", 
            "message": "task not found"}
    
    removed = tasks.pop(task_index)

    return {
        "status": "success",
        "removed_task": removed
    }