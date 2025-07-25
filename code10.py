# 🟢 Creating the Dataset

import pandas as pd
import re

data = {
    'Name': ['Aman Sharma', 'Riya123', 'John.Doe'],
    'Email': ['aman123@gmail.com', 'riya_riya@outlook.com', 'j.doe@company.org'],
    'Message': [
        'Hello, my contact is 9876543210.',
        'My ID is riya_riya@outlook.com and alt is riya123@yahoo.in',
        'Date of joining: 25-07-2025, phone: 8765432109'
    ]
}

df = pd.DataFrame(data)
print(df)

# 🟢 Output:
#           Name                Email                                      Message
# 0  Aman Sharma    aman123@gmail.com             Hello, my contact is 9876543210.
# 1       Riya123  riya_riya@outlook.com  My ID is riya_riya@outlook.com and alt is riya123@yahoo.in
# 2      John.Doe     j.doe@company.org  Date of joining: 25-07-2025, phone: 8765432109


# 🟢 Using re.search() to extract the first phone number

df['First_Phone'] = df['Message'].apply(
    lambda x: re.search(r'\d{10}', x).group() if re.search(r'\d{10}', x) else None
)
print(df[['Name', 'First_Phone']])

# 🟢 Output:
#           Name First_Phone
# 0  Aman Sharma   9876543210
# 1       Riya123        None
# 2      John.Doe   8765432109


# 🟢 Using re.findall() to extract all emails from Message

df['All_Emails'] = df['Message'].apply(
    lambda x: re.findall(r'[\w\.-]+@[\w\.-]+', x)
)
print(df[['Name', 'All_Emails']])

# 🟢 Output:
#           Name                          All_Emails
# 0  Aman Sharma                                []
# 1       Riya123  ['riya_riya@outlook.com', 'riya123@yahoo.in']
# 2      John.Doe                                []


# 🟢 Using re.findall() to extract all dates (DD-MM-YYYY)

df['Dates'] = df['Message'].apply(
    lambda x: re.findall(r'\d{2}-\d{2}-\d{4}', x)
)
print(df[['Name', 'Dates']])

# 🟢 Output:
#           Name          Dates
# 0  Aman Sharma             []
# 1       Riya123            []
# 2      John.Doe  ['25-07-2025']