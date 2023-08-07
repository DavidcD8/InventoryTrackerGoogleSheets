import gspread
from google.oauth2.service_account import Credentials


  def get_gspread_client():
    # Connect to Google Sheets API
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('credentials.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    return GSPREAD_CLIENT

  
 

    def item_exists(self, item_model):
        # Check if an item already exists in the inventory
        items = self.stock.get_all_records()
        return any(
            item.get("item_model") == item_model
            for item in items
        )

    def insert_item(self, item_model, quantity):
        # Insert a new item into the inventory
        if self.item_exists(item_model):
            print("Item already exists in the inventory.")
        else:
            row = [item_model, quantity]
            try:
                self.stock.append_row(row)
                print("Item added successfully.")
            except Exception as e:
                print(f"Error occurred while adding item: {str(e)}")

    def retrieve_items(self, item_search):
        # Get all values from the worksheet
        data = self.stock.get_all_values()
        '''Search for the item name in the first column
        (index 0) and print the matching names and quantities '''
        matching_items = [(row[0], row[1])
                          for row in data if
                          item_search.lower() in row[0].lower()]
        if matching_items:
            print("Matching items:")
            for item_name, quantity in matching_items:
                print(f"Item: {item_name}, Quantity: {quantity}")
        else:
            print("No matching items found.")

    def update_quantity(self, item_search, quantity_sold):
        # Update the quantity of an item in the inventory
        data = self.stock.get_all_values()
        matching_items = [(row[0], row[1])
                          for row in data if
                          item_search.lower() in row[0].lower()]

        if len(matching_items) > 0:
            for item_name, quantity in matching_items:
                transferred_item = item_name
                transferred_quantity = int(quantity)
                transferred_quantity -= quantity_sold
                # Make item_data a 2D list
                item_data = [[transferred_item, str(transferred_quantity)]]
                cell = self.stock.find(transferred_item)
                self.stock.update(cell.address, item_data)
                print(f"Updated:{transferred_quantity} for {transferred_item}")

        else:
            print("Item not found in the inventory.")

    def restock_item(self, item_model, additional_quantity):
        # Restock an item in the inventory
        try:
            additional_quantity = int(additional_quantity)
        except ValueError:
            print("Invalid additional quantity." +
                  "Please enter a valid integer value.")
            return

        data = self.stock.get_all_values()
        # Start from index 1 to skip the header row
        for index, row in enumerate(data[1:], start=2):
            if row[0] == item_model:
                current_quantity = int(row[1])
                new_quantity = current_quantity + additional_quantity
                row_number = index
                cell_range = f"B{row_number}"
                self.stock.update(cell_range, str(new_quantity))
                print("Item restocked successfully.")
                return

        # Item not found
        print("Item not found in the inventory.")

    def remove_item(self, item_model):
        # Remove an item from the inventory
        data = self.stock.get_all_values()
        matching_items = [(row[0], row[1])
                          for row in data if item_model.lower()
                          == row[0].lower()]

        if len(matching_items) > 0:
            for item_name, _ in matching_items:
                cell = self.stock.find(item_name)
                self.stock.delete_rows(cell.row)
                print(f"Item '{item_name}' removed successfully.")
        else:
            print("Item not found in the inventory.")

    def print_inventory(self):
        # Print the entire list of items in the inventory
        data = self.stock.get_all_values()
        if len(data) > 1:
            print("Inventory List:")
            for row in data[1:]:
                item_name, quantity = row[0], row[1]
                print(f"Item: {item_name}, Quantity: {quantity}")
        else:
            print("Inventory is empty.")

    def run(self):
        # Main loop for the inventory tracking application
        while True:
            print("Choose an operation:")
            print("1. Search for an item")
            print("2. Insert a new item")
            print("3. Update quantity")
            print("4. Restock item")
            print("5. Remove item")
            print("6. Print inventory")
            print("0. Exit")

            choice = int(input("Enter your choice (1-6, or 0):\n"))
            if choice == 1:
                item_search = input(
                    "Enter the item model or shorthand code to search:\n")
                self.retrieve_items(item_search)
            elif choice == 2:
                item_model = input("Enter item model:\n")
                if len(item_model) < 3:
                    print("Can not be less than 3 ")
                    continue
                while True:
                    quantity = input("Enter initial quantity:\n")
                    try:
                        quantity = int(quantity)
                        break
                    except ValueError:
                        print("Invalid quantity." +
                              "Please enter a valid integer value.")
                self.insert_item(item_model, quantity)
            elif choice == 3:
                item_search = input(
                    "Enter the item model to update quantity:\n")
                while True:
                    quantity_sold = input(
                        "Enter the quantity sold during the daily sale:\n")
                    try:
                        quantity_sold = int(quantity_sold)
                        break
                    except ValueError:
                        print("Invalid quantity." +
                              "Please enter a valid integer value.")
                self.update_quantity(item_search, quantity_sold)
            elif choice == 4:
                item_model = input("Enter the item model to restock:\n")
                additional_quantity = input(
                    "Enter the additional quantity to be added:\n")
                self.restock_item(item_model, additional_quantity)
            elif choice == 5:
                item_model = input("Enter the item model to remove:\n")
                self.remove_item(item_model)
            elif choice == 6:
                self.print_inventory()
            elif choice == 0:
                print("Exiting the inventory tracking application.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Create an instance of the InventoryTracker class and run the application
    tracker = InventoryTracker()
    tracker.run()
