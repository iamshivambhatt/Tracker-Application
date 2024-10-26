import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                print(f"Updated {name}: {item.quantity}")
                return
        self.items.append(InventoryItem(name, quantity))
        print(f"Added {name}: {quantity}")

    def remove_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    print(f"Removed {quantity} of {name}: {item.quantity}")
                    if item.quantity == 0:
                        self.items.remove(item)
                        print(f"{name} removed from inventory")
                else:
                    print(f"Not enough {name} in inventory to remove {quantity}")
                return
        print(f"{name} not found in inventory")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty")
        else:
            print("Current Inventory:")
            for item in self.items:
                print(item)

def main():
    inventory = Inventory()
    while True:
        print("\nInventory Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            print("Exiting inventory application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
)
