import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gsheet_to_csv(google_sheet_id, output_csv_file):
    # Set up the Google Sheets API credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
    client = gspread.authorize(creds)

    # Access the Google Sheet by its ID
    sheet = client.open_by_key(google_sheet_id)
    worksheet = sheet.get_worksheet(0)  # Assuming the data is on the first worksheet

    # Read the data from Google Sheet into a pandas DataFrame
    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])  # Use the first row as column headers

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_file, index=False)

# Replace 'your_google_sheet_id' with the actual ID of the Google Sheet
# Replace 'output_file.csv' with the desired path for the output CSV file
gsheet_id = 'your_google_sheet_id'
output_csv_file = 'output_file.csv'
gsheet_to_csv(gsheet_id, output_csv_file)
