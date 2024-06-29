task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be addressed soon"
    case "low":
        reminder += " that can be done when you have free time"
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " today!"

print(reminder)
