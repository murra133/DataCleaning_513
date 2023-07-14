import pandas as pd
import numpy as np
import re


# Load CSV file #
df = pd.read_csv('Food_Inspections.csv',skiprows=[1,4])

# Regex for Data curation #
re_ = '[^[a-zA-Z0-9][1-9][0-9]?\.\s]*'

# Add a space at front of all violations to allow for standard format ' 12. ' to match regex
df['Violations_spaced'] = ' ' + df['Violations'].astype(str)

# Filter out Violation Number #
df['Cleaned_Violations'] = df['Violations_spaced'].str.extractall(pat = r'('+re_+')').unstack(level=-1).fillna('').sum(axis=1)

# Replace nan values with 0 #
df['Cleaned_Violations'] = df['Cleaned_Violations'].replace(np.nan, '')

# Find Max Violation #
set_ = set()
m = 0
for s in df['Cleaned_Violations'][1:]:
    temp = re.findall(r"[1-9][0-9]?",s)
    for i in temp:
        m = max(m,int(i))

# Create new Template for new Data Frme #
tempList = []  # List to hold all rows
columns = []  # Holds values for all column headers
columns.append("DBA Name")
columns.append("Facility Type")
tempRow = [] # Sample row to populate tempList
tempRow.append("DBA Name")
tempRow.append("Facility Type")

# Populate columns and sample row with values
for i in range(1,m+1):
    columns.append(str(i))
    tempRow.append(0)


# Loop through data frame, insert all values into temp row # 
for j in range(1,len(df['Cleaned_Violations'])):
    tempList.append(tempRow.copy())
    l = len(tempList)-1
    tempList[l][0] = df['DBA Name'][j]
    tempList[l][1] = df['Facility Type'][j]
    temp = re.findall(r"[1-9][0-9]?",df['Cleaned_Violations'][j])
    for i in temp:

        tempList[l][int(i)+1] = 1

# Create new dataframe with data, output to csv #
new_df = pd.DataFrame(data = tempList, columns=columns)
print(new_df)
compression_opts = dict(method='zip',
                        archive_name='out.csv')  
new_df.to_csv('out.zip',index=False, compression=compression_opts)