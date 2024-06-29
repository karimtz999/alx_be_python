# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match time_bound: 
    case 'yes':
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case 'no':
        if priority in ["high", "medium", "low"]:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Invalid priority level. Please enter high, medium, or low.")
