#import Libraries
import os
import pandas as pd

# Define the path to the input and output directories
input_path = r'Data\Input'
output_path = r'Data\Output'

# Read all Excel files into a list of DataFrames
df = []
for file in os.listdir(input_path):
    if file.endswith('.xlsx'):
        print('Loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(input_path, file)))

#Concatenate the files
combined_file = pd.concat(df, axis = 0)

#Export the file to excel
combined_file.to_excel(f"{output_path}/combined_file2.xlsx",index =False)
print('File Successfully Exported')
