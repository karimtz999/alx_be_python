name = input("Enter your task: ")
piriority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
if time == 'yes':
    print(f"Reminder: {name} is a {piriority} priority task that requires immediate attention today!")
else:
    print(f"Note: {name} is a {piriority} priority task. Consider completing it when you have free time.")


