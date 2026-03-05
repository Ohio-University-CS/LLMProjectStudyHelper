def generate_study_plan_from_tasks(tasks, days=1, hours_per_day=2):
    if not tasks:
        return {"study_plan": "No tasks to schedule."}
    
    plan = {}

    for i, task in enumerate(tasks):
        day = (i % days) + 1

        if day not in plan:
            plan[day] = []

        plan[day].append({"task": task["name"], "hours": round(hours_per_day / len(tasks), 2)})
        
    return {"study_plan": plan}

generate_study_plan = {
    "name": "generate_study_plan",
    "description": "Generates a study plan from a comma-seperated list of tasks, each defined with elements such as name, class, body, due date.",
    "parameters": {
        "tasks": {
            "type": "array",
            "description": "List of tasks, each with a name, class, body, and optional due date.",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "class": {"type": "string"},
                    "body": {"type": "string"},
                    "due": {"type": "string"}
                },
                "required": ["name"]
            }
        },
        "days": {
            "type": "integer",
            "description": "number of days to plan"
        },
        "hours_per_day": {
            "type": "integer",
            "description": "Hours per day to plan for studying."
        }
    },
    "required": ["tasks"]
}