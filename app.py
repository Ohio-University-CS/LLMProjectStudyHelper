import json
import requests

from functions.create_task import create_task
from functions.update_task import update_task
from functions.delete_task import delete_task

from functions.reason_task import reason_task_from_task
from functions.reason_task import reason_task

from functions.generate_study_plan import generate_study_plan_from_tasks
from functions.generate_study_plan import generate_study_plan

from google.genai import types # Add this to your imports

# from functions.analyze_image import # Not done. Unable to do without proper API key setup.
# from tools.generate_image import # Not done. Unable to do without proper API key setup.

from client import client

def main():

    tasks = [{
        "name": "Test Task",
        "class": "CS 2401",
        "body": "Test Body.",
        "due_date": None
    }]

    print("Collin Blumenauer - CS3560 LLM Project")
    print("Class study helper")

    while True:
        command = input("""
            Enter function index:
            1. Create Task
            2. Update Task
            3. Delete Task
            4. Reason Task
            5. Generate Study Plan
            6. Exit
            """
        )

        command = int(command)

        if command == 1:
            args_input = input("Enter arguments formatted as follows: name, body, due date. Seperated by commas.")
            args = {}

            for pair in args_input.split(","):
                if "=" in pair:
                    k, v = pair.split("=")
                    args[k.strip()] = v.strip()

            result = create_task(tasks, **args)
            print("Created task.")
        
        if command == 2:
            task_index = input("Enter task index to update: ")
            task_index = int(task_index)

            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;

            # Need a way to print all tasks with index.
            args_input = input("Enter arguments formatted as follows: name, body, due date. Seperated by commas.")
            args = {}

            for pair in args_input.split(","):
                if "=" in pair:
                    k, v = pair.split("=")
                    args[k.strip()] = v.strip()

            result = update_task(tasks, task_index, **args)
            print("Updated task.")

        if command == 3:
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            task_index = input("Enter task index to delete: ")
            task_index = int(task_index)

            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;

            args_input = input("Enter arguments formatted as follows: task index")
            args = {}

            for pair in args_input.split(","):
                if "=" in pair:
                    k, v = pair.split("=")
                    args[k.strip()] = v.strip()

            delete_task(tasks, task_index, **args)
            print("Deleted task.")
        if command == 4:
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            task_index = input("Enter task index to reason: ")
            task_index = int(task_index)

            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;

            result = reason_task_from_task(tasks, task_index)
            print("Reasoned task.")

            tool_definition = {
                "function_declarations": [reason_task] 
            }

            chat = client.chats.create(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(
                    tools=[tool_definition]
                )
            )

            prompt = f"Please help me understand and get started with this: {tasks[task_index]}"
            response = chat.send_message(prompt)

            print(response.text)

        if command == 5:
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            args_input = input("Enter arguments formatted as follows: days, hours per day")
            args = {}

            for pair in args_input.split(","):
                if "=" in pair:
                    k, v = pair.split("=")
                    args[k.strip()] = v.strip()

            result = generate_study_plan_from_tasks(tasks, **args)

            result = reason_task_from_task(tasks, task_index)
            print("Reasoned task.")

            tool_definition = {
                "function_declarations": [reason_task] 
            }

            chat = client.chats.create(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(
                    tools=[tool_definition]
                )
            )

            prompt = f"Please help me understand and get started with this: {tasks[task_index]}"
            response = chat.send_message(prompt)

            print("Generated Study Plan from Task.")
        if command == 6:
            break

if __name__ == "__main__":
    main()