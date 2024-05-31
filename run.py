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
