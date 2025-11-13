# daily_reminder.py
# Personal daily reminder using match-case, if statements, and loops

# Prompt for task
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
