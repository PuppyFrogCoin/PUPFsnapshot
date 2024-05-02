import os
import requests
import json
import csv

MY_TOKEN = "B9LeEmSNkGiNAz2iwmPb6cPvwHMhchTNhBJLPBqVYgk7"

url = "SOLANA RPC"
headers = {"accept": "application/json", "content-type": "application/json"}

# load wallet addresses
with open('output.json', 'r') as file:
    wallets = json.load(file)

# open the csv file in write mode
with open('wallet_token_balances.csv', 'w') as file:
    writer = csv.writer(file)
    # write the headers
    writer.writerow(["Wallet", "Balance"])

    for wallet in wallets:
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getTokenAccountsByOwner",
            "params": [
                wallet,
                {"mint": MY_TOKEN},
                {"encoding": "jsonParsed"},
            ],
        }
        response = requests.post(url, json=payload, headers=headers)
        balance = response.json()["result"]["value"][0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
        # writing values of each wallet and balance into the csv file
        writer.writerow([str(wallet), str(balance)])