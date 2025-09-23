# Grocery list operations
groceryList = ["milk", "bread", "egg"]

def add_item(item):
    groceryList.append(item)
    return groceryList

print("Added List:", add_item("Mango"))

def remove_last_item():
    if groceryList:  
        groceryList.pop()
    return groceryList


print("Remove Last Item:", remove_last_item())

# Lambda for display
display_item = lambda item: print(f"Item: {item}")
for x in groceryList:
    display_item(x)

# Recursive character count
def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("Recursive: Total no of characters in all items:", count_characters(groceryList))