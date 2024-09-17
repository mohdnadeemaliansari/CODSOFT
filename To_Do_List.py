# Define a dictionary to store to-do list items
todo_list = {}
# Add a new to-do list item
def add_item():
   
    item_name = input("Enter the item name: ")
    item_description = input("Enter the item description: ")
    todo_list[item_name] = {"description": item_description, "status": "completed"}
    print(f"Item '{item_name}' added to the to-do list!")

# Update an existing to-do list item
def update_item():
    
    item_name = input("Enter the item name: ")
    if item_name in todo_list:
        item_description = input("Enter the new item description: ")
        todo_list[item_name]["description"] = item_description
        print(f"Item '{item_name}' updated!")
    else:
        print(f"Item '{item_name}' not found in the to-do list!")


# Delete a to-do list item
def delete_item():
    
    item_name = input("Enter the item name: ")
    if item_name in todo_list:
        del todo_list[item_name]
        print(f"Item '{item_name}' deleted from the to-do list!")
    else:
        print(f"Item '{item_name}' not found in the to-do list!")


# Mark a to-do list item as done
def mark_as_done():
    
    item_name = input("Enter the item name: ")
    if item_name in todo_list:
        todo_list[item_name]["status"] = "done"
        print(f"Item '{item_name}' marked as done!")
    else:
        print(f"Item '{item_name}' not found in the to-do list!")

#View the entire to-do list
def view_list():
    
    print("To-Do List:")
    for item_name, item_info in todo_list.items():
        print(f"  {item_name}: {item_info['description']} ({item_info['status']})")

#Here we can define a main function to execute all the UDFs
def main():
    while True:
        print("To-Do List Menu:")
        print("  1. Add Item")
        print("  2. Update Item")
        print("  3. Delete Item")
        print("  4. Mark as Done")
        print("  5. View List")
        print("  6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            mark_as_done()
        elif choice == "5":
            view_list()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()