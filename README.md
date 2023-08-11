# Inventory Tracker

This is a Python code for an Inventory Tracker that uses Google Sheets to store and manage item data. The code provides functionality to connect to a Google Sheets document, create an inventory table, insert new items, search for items, update item quantities, restock items, remove items, and print the inventory.
 

# Overview
The inventory tracking program is designed for individuals or businesses that need to manage and keep track of their inventory. It can be used by store owners, warehouse managers, inventory control teams, or any individual or organization that deals with maintaining and monitoring stock levels of products or items.

# Prerequisites

Before running the code, ensure that you have the following:

- Python 3.x installed on your system.
- The necessary Python packages installed, including `gspread` and `google-auth`.
- A Google Sheets document created for your inventory.
- A service account with a service account key file (JSON format) obtained from the Googe Cloud Console

# Getting Started

- Clone the repository or download the inventory_tracker.py file.
- Rename the service account key file to credentials.json and place it in the same directory as the Python script.
- Install the required Python packages by running pip install gspread google-auth.
- Open the terminal and run the Python script using python inventory_tracker.py.

## Usage
 

Upon running the code, the program will display a menu with the following options:
 
1. Search for an item
2. Insert a new item
3. Update quantity
4. Restock item
5. Remove item
6. Print inventory
0. Exit

Enter the number corresponding to the desired operation and follow the prompts to provide the necessary information.

## Example
Choose an operation:
1. Search for an item
2. Insert a new item
3. Update quantity
4. Restock item
5. Remove item
6. Print inventory
0. Exit

Enter your choice (1-6, or 0): 1
Enter the item model or shorthand code to search: Laptop
Matching items:
Item: Laptop, Quantity: 5
![picture of Website logo](search.png)

...

Choose an operation:
1. Search for an item
2. Insert a new item
3. Update quantity
4. Restock item
5. Remove item
6. Print inventory
0. Exit

Enter your choice (1-6, or 0): 0
Exiting the inventory tracking application.
![picture of Website logo](exit.png)

# Testing Steps/Guidelines
Before testing the application, ensure that you have completed the prerequisites and have set up the Google Sheets document with the correct structure.

1. Connect to the Spreadsheet:

Verify that the application connects to the Google Sheets document named "inventory" successfully.
Check for any connection errors and ensure the main menu is displayed after successful connection.

2. Insert a New Item:

Verify that you can add a new item to the inventory with a valid item model and positive integer quantity.
Check that the program provides appropriate feedback for empty or invalid data entry.
Check the Google Sheets document to ensure the new item and quantity have been added correctly.

3. Search for an Item:

Verify that the application can search for an existing item by its name or shorthand code.
Check that the program provides informative messages when the item is not found or when the search input is empty.

4. Update Quantity:

Verify that the application can update the quantity of an existing item based on the quantity sold during the daily sale.
Check that the program handles invalid data entry, such as non-integer quantities.
Check the Google Sheets document to ensure the quantity is updated correctly.

5. Restock Item:

Verify that you can restock an existing item with an additional quantity.
Check that the program handles invalid data entry, such as non-integer quantities.
Check the Google Sheets document to ensure the item has been restocked correctly.

6. Remove Item:

Verify that you can remove an existing item from the inventory.
Check the Google Sheets document to ensure the item has been removed correctly.

7. Print Inventory:

Verify that the application can print the entire inventory with item names and quantities.
Check that the program provides informative messages if the inventory is empty.

8. Invalid Inputs:

Test the program with various invalid inputs, such as providing an empty item model, non-integer quantities, and incorrect item names.
Verify that the application handles such inputs gracefully and displays appropriate error messages.

9. Exit the Application:

Verify that the application can be terminated gracefully without any errors.


10. Database Structure

The inventory is stored in a Google Sheets document with the following columns:
- Item Model
- Quantity

# pep8 Validator 
-I used the https://pep8ci.herokuapp.com App and made sure it contains zero erros 
## Before
![Screenshot 2023-08-11 184704](https://github.com/DavidcD8/InventoryTrackerGoogleSheets/assets/91196677/2791fe77-cfd4-4137-89d8-87f38848d1dd)

## After
 ![Screenshot 2023-08-11 190107](https://github.com/DavidcD8/InventoryTrackerGoogleSheets/assets/91196677/403aed10-8219-480b-8f9e-c0e2e882c120)

# Issues Found and Fixes
- The `Restock` method was not finding the items. The code should have been using `get_all_values()` instead of `get_all_records()`.
- An issue was found while removing the item from the list. It was removing any item that had a quantity of one.
- The code was truncated in a way that caused the application to break with an error. The issue was fixed by changing the print statement in the code.
- The program was allowing duplicate. The issue was fixed by replacing the item_exists function for is_valid_quantity


# Acknowledgements
The Inventory Tracker application was developed as a programming school project. We would like to acknowledge the following sources that contributed to the development of this project:

- Stack Overflow for providing guidance on input validation.
- Google Sheets API for enabling the interaction with the Google Sheets document.
- Continuous Integration (CI) for providing valuable feedback on the code.


# Future Additions

The addition of a UI.

# Credit
- https://stackoverflow.com/questions/41684523/how-can-i-add-validation-for-input-length-of-a-string
 if len(item_model) < 3:
                    print("Can not be less than 3 ")

- Google Sheets API 
- CI : SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
- https://python-forum.io/thread-28805.html
- data = self.stock.get_all_values()

# DEPLOYMENT
The project has been successfully deployed to Heroku. You can access the deployed application at the following link: [Inventory Tracker App](https://inventory-tracker-app-725424cf8abe.herokuapp.com)

# Version Control (Git)
The project has been version controlled using Git. Commits have been made at appropriate intervals, and commit messages have been improved to provide descriptive information about each change made.

