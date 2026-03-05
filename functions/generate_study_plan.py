def generate_study_plan_from_tasks(tasks):
    return {"tasks": tasks}

generate_study_plan = {
    "name": "generate_study_plan",
    "description": "Generates a study plan from a comma-seperated list of tasks, each defined with elements such as name, class, body, due date.",
    "parameters": {
        "type": "object",
        "properties": {
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
                    }
                }
            }
        },
        "required": ["tasks"]
    },
}