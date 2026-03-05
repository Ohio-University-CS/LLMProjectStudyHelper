import json

def generate_study_plan_prompt(tasks):
    task_text = json.dumps(tasks, indent=2)

    return f"""
    You are an academic study planner.

    Given the following list of assignments, create a structured study plan.

    Requirements:
    - Prioritize tasks by due date if available.
    - Break work into reasonable study sessions (not by the hour, but based on a realistic daily allocated amount of time)
    - Suggest an order for tasks
    - Include estimated focus areas.
    - DO NOT ASK THE USER FOR QUESTIONS. PURELY REASON.
    - Do not repeat the table.
    - Stop after the table.

    Tasks:
    {task_text}
    """