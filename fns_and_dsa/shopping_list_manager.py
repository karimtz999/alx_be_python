def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")  # Prompt for and add an item
            if item:
                shopping_list.append(item)
                print(f"{item} was added to your shopping list.")
            else:
                print("Invalid input. Please enter a valid item.")
        elif choice == '2':
            item = input("Enter the item to remove: ")  # Prompt for and remove an item
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} was removed from your shopping list.")
            else:
                print(f"{item} is not in the list.")
        elif choice == '3':
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
