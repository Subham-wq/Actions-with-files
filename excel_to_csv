import pandas as pd

def excel_to_csv(input_excel_file, output_csv_file):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_excel_file)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_file, index=False)

# Replace 'input_file.xlsx' with the path to your input Excel file
# Replace 'output_file.csv' with the desired path for the output CSV file
input_excel_file = 'input_file.xlsx'
output_csv_file = 'output_file.csv'
excel_to_csv(input_excel_file, output_csv_file)
