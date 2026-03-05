def reason_task_from_task(tasks, task_index):
    if(task_index >= len(tasks)):
        return {"task": "No tasks to schedule."}
    
    return {"task": tasks[task_index]}

reason_task = {
    "name": "reason_task",
    "description": "Reason about this task. Help the student get started.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "task": {
                "type": "OBJECT",
                "properties": {
                    "name": {"type": "STRING"},
                    "class": {"type": "STRING"},
                    "body": {"type": "STRING"},
                    "due": {"type": "STRING"}
                },
                "required": ["name"]
            }
        },
        "required": ["task"]
    }
}