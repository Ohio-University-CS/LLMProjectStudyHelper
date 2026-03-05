def update_task(tasks, task_index, name=None, body=None, due=None):
    if(task_index >= len(tasks)):
        return {
            "status": "error", 
            "message": "task not found"}
    
    if(name):
        tasks[task_index]["name"] = name
    if(body):
        tasks[task_index]["body"] = body
    if(due):
        tasks[task_index]["due"] = due

    return {
        "status": "success",
        "task": tasks[task_index]
    }