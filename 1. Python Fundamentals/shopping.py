# Grocery Shopping Budget and List Manager

# Define variables
budget = 100.0  # Budget in dollars
shopping_list = []
recipes = {
    "Pasta": ["pasta", "tomato sauce", "cheese"],
    "Salad": ["lettuce", "tomato", "cucumber", "dressing"],
    "Omelette": ["eggs", "cheese", "milk"]
}

# Welcome message
print("Welcome to the Grocery Shopping Budget Manager!")

# Function to display current shopping list and budget
def display_status():
    print("\nCurrent Shopping List:")
    for item in shopping_list:
        print(f"- {item['name']} (${item['price']})")
    print(f"Remaining Budget: ${budget - sum(item['price'] for item in shopping_list):.2f}")

# Function to add an item to the shopping list
def add_item(name, price):
    global budget
    if price <= (budget - sum(item['price'] for item in shopping_list)):
        shopping_list.append({"name": name, "price": price})
        print(f"Added {name} to the shopping list.")
    else:
        print(f"Cannot add {name}. Not enough budget.")

# Function to create a shopping list based on selected recipes
def create_shopping_list():
    print("\nAvailable Recipes:")
    for recipe in recipes.keys():
        print(f"- {recipe}")

    selected_recipes = input("Enter the names of the recipes you want to make (comma separated): ").split(",")
    ingredients_needed = set()
    for recipe in selected_recipes:
        recipe = recipe.strip()
        if recipe in recipes:
            ingredients_needed.update(recipes[recipe])
        else:
            print(f"Recipe {recipe} not found.")

    for ingredient in ingredients_needed:
        price = float(input(f"Enter the price for {ingredient}: "))
        add_item(ingredient, price)

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display current shopping list and budget")
    print("2. Add item to shopping list")
    print("3. Create shopping list from recipes")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        display_status()
    elif choice == '2':
        item_name = input("Enter the name of the item: ")
        item_price = float(input("Enter the price of the item: "))
        add_item(item_name, item_price)
    elif choice == '3':
        create_shopping_list()
    elif choice == '4':
        print("Thank you for using the Grocery Shopping Budget Manager!")
        break
    else:
        print("Invalid choice. Please try again.")




