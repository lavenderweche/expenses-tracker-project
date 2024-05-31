import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_tracker')

# Define the range for the sheet 
RANGE_NAME = 'Sheet1!A:D' # Adjust the range as needed 
MONTHLY_LIMIT = 1000 # Set your monthly spending limit here

def add_expense():
    """
    Add an expense to Google Sheets with input validation.
    """
    try:
        # Collect user input
        description = input("Enter the description of the expense: ").strip()
        category = input("Enter the category of the expense: ").strip()
        amount = input("Enter the amount spent: ").strip()
        date = input("Enter the date of the expense (YYYY-MM-DD) or leave blank for today: ").strip()

        # Validate description and category
        if not description:
            print("Error: Description cannot be empty.")
            return False
        if not category:
            print("Error: Category cannot be empty.")
            return False

        # Validate amount
        try:
            amount = float(amount)
        except ValueError:
            print("Error: Invalid amount. Please enter a valid number.")
            return False

        # Validate and format date
        if not date:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
        else:
            try:
                date = parser.parse(date).strftime('%Y-%m-%d')
            except ValueError:
                print("Error: Invalid date format. Please use YYYY-MM-DD.")
                return False

        if check_monthly_limit_exceeded(date, amount):
            print("Warning: Adding this expense will exceed your monthly limit!")

        values = [[date, description, category, amount]]
        sheet = SHEET.get_worksheet(0)  # Access the first sheet
        sheet.append_row(values[0])
        print("Expense added successfully.")
        return True
    except gspread.exceptions.APIError as e:
        print(f"An error occurred while communicating with Google Sheets: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def view_summary():
    """
    View a summary of expenses from Google Sheets.
    """
    try:
        sheet = SHEET.get_worksheet(0)  # Access the first sheet
        rows = sheet.get_all_values()

        if not rows or len(rows) == 1:  # Checking if there are no expenses besides headers
            print('No data found.')
            return

        for row in rows:
            print(', '.join(row))
    except gspread.exceptions.APIError as e:
        print(f"An error occurred while communicating with Google Sheets: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def check_monthly_limit_exceeded(date, new_amount):
    """
    Check if adding an expense exceeds the monthly limit.
    
    Args:
        date (str): The date of the expense in YYYY-MM-DD format.
        new_amount (float): The amount of the new expense.
    
    Returns:
        bool: True if the monthly limit is exceeded, otherwise False.
    """
    try:
        sheet = SHEET.get_worksheet(0)  # Access the first sheet
        rows = sheet.get_all_values()
        if not rows or len(rows) == 1:  # Checking if there are no expenses besides headers
            return False

        # Calculate the total spending for the current month
        current_month = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
        total_spent = 0

        for row in rows[1:]:  # Skip the header row
            row_date, _, _, row_amount = row
            try:
                row_date_month = datetime.datetime.strptime(row_date, '%Y-%m-%d').strftime('%Y-%m')
                if row_date_month == current_month:
                    total_spent += float(row_amount)
            except ValueError:
                continue

        return (total_spent + new_amount) > MONTHLY_LIMIT
    except gspread.exceptions.APIError as e:
        print(f"An error occurred while communicating with Google Sheets: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    """
    Command line interface for the expense tracker.
    """
    while True:
        try:
            print("\nExpense Tracker Menu:")
            print("1. Add an expense")
            print("2. View expenses summary")
            print("3. Exit")
            choice = input("Choose an option (1, 2, or 3): ").strip()

            if choice == '1':
                if add_expense():
                    while True:
                        another_entry = input("Would you like to add another entry? (yes/no): ").strip().lower()
                        if another_entry == 'yes':
                            if not add_expense():
                                break
                        elif another_entry == 'no':
                            print("Thank you for using the tracker app.")
                            return
                        else:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
            elif choice == '2':
                view_summary()
                while True:
                    another_action = input("Would you like to perform another action? (yes/no): ").strip().lower()
                    if another_action == 'yes':
                        break
                    elif another_action == 'no':
                        print("Thank you for using the tracker app.")
                        return
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    print("Welcome to your expense tracker app.\n Here to help you manage your expenses.\nPlease enter 1, 2, or 3 to start.")
    main()
