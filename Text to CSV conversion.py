import pandas as pd

def txt_to_csv(input_file, output_file):
    # Read the text file into a pandas DataFrame
    df = pd.read_csv(input_file, delimiter='\t')  # Adjust delimiter if needed

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

# Replace 'input_file.txt' with the path to your input text file
# Replace 'output_file.csv' with the desired path for the output CSV file
input_file = 'input_file.txt'
output_file = 'output_file.csv'
txt_to_csv(input_file, output_file)
