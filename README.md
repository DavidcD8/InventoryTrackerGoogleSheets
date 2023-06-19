
# Inventory Tracker

This is a Python code for an Inventory Tracker that uses Google Sheets to store and manage item data. The code provides functionality to connect to a Google Sheets document, create an inventory table, insert new items, search for items, update item quantities, restock items

## Prerequisites

Before running the code, ensure that you have the following:

- Python 3.x installed on your system.
- The necessary Python packages installed, including `gspread` and `google-auth`.

## Getting Started

1. Make sure you have a Google Sheets document created for your inventory.
2. Create a service account and download the service account key file (JSON format) from the Google Cloud Console.
3. Rename the service account key file to `credentials.json` and place it in the same directory as the Python script.
4. Open the `inventory_tracker.py` file and modify the `DOCUMENT_NAME` constant to match your Google Sheets document name.
5. Run the Python script using `python inventory_tracker.py`.

## Usage

1. Upon running the code, the program will display a menu with the following options:
   - Search for an item
   - Insert a new item
   - Update quantity
   - Restock item
   - Exit

2. Follow the prompts and enter the appropriate information for each operation.

## Example

Choose an operation:

1.  Search for an item
2.  Insert a new item
3.  Update quantity
4.  Restock item
5.  Exit Enter your choice (1, 2, 3, 4, or 0): 2 Enter item model: Laptop Enter initial quantity: 5 Item added successfully.

Choose an operation:

1.  Search for an item
2.  Insert a new item
3.  Update quantity
4.  Restock item
5.  Exit Enter your choice (1, 2, 3, 4, or 0): 1 Enter the item model or shorthand code to search: Laptop Matching items: Item: Laptop, Quantity: 5

Choose an operation:

1.  Search for an item
2.  Insert a new item
3.  Update quantity
4.  Restock item
5.  Exit Enter your choice (1, 2, 3, 4, or 0): 3 Enter the item model to update quantity: Laptop Enter the quantity sold during the daily sale: 2 Quantity updated for Laptop: 3

Choose an operation:

1.  Search for an item
2.  Insert a new item
3.  Update quantity
4.  Restock item
5.  Exit Enter your choice (1, 2, 3, 4, or 0): 4 Enter the item model to restock: Laptop Enter the additional quantity to be added: 10 Item restocked successfully. Matching items: Item: Laptop, Quantity: 13

Choose an operation:

1.  Search for an item
2.  Insert a new item
3.  Update quantity
4.  Restock item
5.  Exit Enter your choice (1, 2, 3, 4, or 0): 0 Exiting the inventory tracking application.


## Database Structure

The inventory is stored in a Google Sheets document with the following columns:
- Item Model
- Quantity

## Note

- When searching for an item, you can enter either the item model or a shorthand code. The application will return matching items based on the input.
- When inserting a new item, the application will automatically generate a unique stock number for the item.
- If multiple items.

## Issues Found
Method Restock was not finding the items. `I should've been using `get_all_values()`and not get_all_records()`, 


## Acknowledgements

The Inventory Tracker application was developed as a programming school project.

## Future additions

The addition of a UI