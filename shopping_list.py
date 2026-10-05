shopping_list = []

while True:
    print("\nMenu options: add / remove / show / done")
    action = input("What would you like to do? ").strip().lower()

    if action == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to your list.")

    elif action == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your Shopping List:")
            for item in shopping_list:
                print(item)

    elif action == "done":
        print("Goodbye! Thank you for using the shopping list app.")
        break

    else:
        print("Invalid choice. Please choose: add, remove, show, or done.")
