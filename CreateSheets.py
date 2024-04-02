
from google.oauth2.service_account import Credentials
import gspread
import csv

def sheetUpdate(csv1, csv2):
    # Define scopes and load credentials
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    
    # Authorize gspread client
    client = gspread.authorize(creds)
    
    # Open the Google Sheets spreadsheet by its key
    sheet_id = "PLEASE ENTER YOUR SPREADSHEET ID HERE"
    sheet = client.open_by_key(sheet_id)
    
    # Open the respective sheets
    sheet1 = sheet.worksheet("apex_03")
    sheet2 = sheet.worksheet("apex_04")

    # Read and import data from CSV files to respective sheets
    import_csv_to_sheet(csv1, sheet1)
    import_csv_to_sheet(csv2, sheet2)

def import_csv_to_sheet(csv_file, sheet):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
        
        # Convert numerical strings to floats
        sheet.clear()
        
        # Write data from CSV to the sheet
        sheet.update("A1", data)

