import json
import os
import requests

from functions.create_task import create_task
from functions.update_task import update_task
from functions.delete_task import delete_task

from functions.reason_task import reason_task_prompt
from functions.generate_study_plan import generate_study_plan_prompt

from tasks_serialization import load_tasks
from tasks_serialization import save_tasks

from google.genai import types

# from functions.analyze_image import # Not done. Unable to do without proper API key setup.
# from tools.generate_image import # Not done. Unable to do without proper API key setup.

from client import client

def main():

    # Tasks
    tasks = load_tasks()

    # Heading stuffs
    print("")
    print("Collin Blumenauer - CS3560 LLM Project")
    print("Class study helper")

    # Main loop
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

        # Turn the command into an integer
        command = int(command)

        if command == 1:
            # Prompt user for task creation
            args_input = input("Enter arguments formatted as follows: name, class, body, due date. Seperated by commas. ")
            task_name, class_name, task_body, due_date = [x.strip() for x in args_input.split(",")]

            # Create the task and append it to tasks
            result = create_task(tasks, task_name, class_name, task_body, due_date)
            print("Created task.")
        
        if command == 2:
            # Print tasks
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            # Prompt user for task
            task_index = input("Enter task index to update: ")
            task_index = int(task_index)

            # Task validation
            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;
            
            # Prompt user for task details to update.
            args_input = input("Enter arguments formatted as follows: name, class, body, due date. Seperated by commas. ")
            task_name, class_name, task_body, due_date = [x.strip() for x in args_input.split(",")]

            # Update the task
            result = update_task(tasks, task_index, task_name, class_name, task_body, due_date)
            print("Updated task.")

        if command == 3:

            # Print all tasks
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            # Prompt the user for a task
            task_index = input("Enter task index to delete: ")
            task_index = int(task_index)

            # Task Validation
            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;
            
            # Delete Task
            delete_task(tasks, task_index)
            print("Deleted task.")

        if command == 4:

            # Print all tasks
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            # Prompt the user for a task
            task_index = input("Enter task index to reason: ")
            task_index = int(task_index)

            # Task validation
            if(task_index < 0 or task_index >= len(tasks)):
                print("Invalid task index.")
                continue;
            
            # Create prompt for task
            prompt = reason_task_prompt(tasks[task_index])

            # Create chat instance
            chat = client.chats.create(
                model="gemini-3.1-flash-lite-preview",
            )

            # Send response and print it
            response = chat.send_message(prompt)
            print(response.text)

        if command == 5:

            # Print all tasks
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i}: {task['name']} (Class: {task.get('class','')}, Due: {task.get('due','')})")

            # Create prompt from tasks
            prompt = generate_study_plan_prompt(tasks)

            # Create chat instance
            chat = client.chats.create(
                model="gemini-3.1-flash-lite-preview",
            )

            # Send response and print
            response = chat.send_message(prompt)
            print(response.text)

        if command == 6:
            break

    save_tasks(tasks)

if __name__ == "__main__":
    main()