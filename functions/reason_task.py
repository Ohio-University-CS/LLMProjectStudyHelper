def reason_task_prompt(task):
    return f"""
    You are helping a student get started with an assignment.

    Reason about the following task and provide:
    - What the task involves
    - Steps to start
    - Challenges
    - A scheduled plan

    Task Information:
    Name: {task.get("name", "")}
    Class: {task.get("class", "")}
    Body: {task.get("body", "")}
    Due Date: {task.get("due", "")}

    DO NOT ASK QUESTIONS. ONLY REASON ABOUT THE TASK.
    """