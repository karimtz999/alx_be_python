# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the base reminder message
reminder = ""

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be addressed soon today!"
        else:
            reminder += "."
    case "low":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a low priority task that needs attention today."
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Print the customized reminder
print(reminder)
