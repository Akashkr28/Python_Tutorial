# Numbered Task List You’re improving the UX of a task management app by numbering the user’s task list automatically.
# Tasks:
#   - Define a function generate_numbered_tasks that takes a list of task names.
#   - Use the enumerate() function to loop through the list with numbering starting from 1.
#   - Format each task as "1. Task Name" and return the final list.

generated_numbered_tasks = ["Buying Groceries", "Paying Bills"]

for number, task in enumerate(generated_numbered_tasks, start=1):
    print(f"{number}. {task}")