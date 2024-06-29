name = input("Enter your task: ")
piriority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match time:
case 'yes':
    print(f"Reminder: {name} is a {piriority} priority task that requires immediate attention today!")
case 'no':
    print(f"Note: {name} is a {piriority} priority task. Consider completing it when you have free time.")


