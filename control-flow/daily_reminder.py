# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder message
reminder = ""

# Process the task based on priority
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Modify the reminder if the task is time-bound
if priority in ['high', 'medium', 'low']:
    if time_bound == "yes":
        reminder = "Reminder: " + reminder + " that requires immediate attention today!"
    else:
        if priority == 'low':
            reminder = "Note: " + reminder + ". Consider completing it when you have free time."
        else:
            reminder = "Reminder: " + reminder + "."

# Print the customized reminder
print(reminder)
