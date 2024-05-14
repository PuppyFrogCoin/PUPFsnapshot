import pandas as pd

# Read the csv data
df = pd.read_csv('wallet_token_balances.csv')

# Calculate the total amount of keys
total_keys = df['Diamond Keys'] + df['Gold Keys'] + df['Silver Keys'] + df['Bronze Keys']

# Calculate and print the absolute total
absolute_total_keys = total_keys.sum()
print(absolute_total_keys)