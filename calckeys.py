import pandas as pd

def calculate_keys(wallet_balance):
    DIAMOND_KEY = 1000000
    GOLD_KEY = 500000
    SILVER_KEY = 250000
    BRONZE_KEY = 100000

    diamond_keys = wallet_balance // DIAMOND_KEY

    gold_keys = wallet_balance // GOLD_KEY

    silver_keys = wallet_balance // SILVER_KEY

    bronze_keys = wallet_balance // BRONZE_KEY

    return pd.Series((diamond_keys, gold_keys, silver_keys, bronze_keys))

def read_and_append_keys(csv_file):
    df = pd.read_csv(csv_file)
    df[['Diamond Keys', 'Gold Keys', 'Silver Keys', 'Bronze Keys']] = df['Balance'].apply(calculate_keys)
    df.to_csv(csv_file, index=False)

# Call Function
read_and_append_keys('wallet_token_balances.csv')