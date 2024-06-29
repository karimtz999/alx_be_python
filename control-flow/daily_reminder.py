# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = ""

match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task"
    case 'low':
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Modify the reminder if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"
else:
    if priority in ["high", "medium", "low"]:
        reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

