shopping_list = []

while (choice := input("\n1. Add Item  2. Remove Item  3. View List  4. Check Item  5. Exit\nChoose: ")) != '5':
    if choice == '1':
        item = input("Enter item: ")
        if item not in shopping_list:
            shopping_list.append(item)
            print(f"{item} added.")
        else:
            print(f"{item} is already in the list.")
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found.")
    elif choice == '3':
        print("\nShopping List:")
        print("\n".join(shopping_list) if shopping_list else "No items in the list.")
    elif choice == '4':
        item = input("Enter item to check: ")
        print(f"{item} is in the list." if item in shopping_list else f"{item} is not in the list.")
    else:
        print("Invalid choice.")

print("Goodbye!")
