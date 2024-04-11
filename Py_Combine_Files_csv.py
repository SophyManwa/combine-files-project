#import Libraries
import os
import pandas as pd

# Define the path to the input and output directories
input_path = r'C:\Users\Administrator\Documents\Python Automation\Data\Input'
output_path = r'C:\Users\Administrator\Documents\Python Automation\Data\Output'

# Read all CSV files into a list of DataFrames
df = []
for file in os.listdir(input_path):
    if file.endswith('.csv'):
        print('Loading file {0}...'.format(file))
        df.append(pd.read_csv(os.path.join(input_path, file)))

#Concatenate the files
combined_file = pd.concat(df, axis = 0)

#Export the file to excel
combined_file.to_excel(f"{output_path}/combined_file1.xlsx",index =False)
print('File Successfully Exported')