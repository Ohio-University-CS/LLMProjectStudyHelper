def create_task(tasks, task_name, class_name, task_body, due_date=None):
    task = {
        "name": task_name,
        "class": class_name,
        "body": task_body,
        "due": due_date
    }
    
    tasks.append(task)
    
    return {
        "status": "success",
        "task": task
    }