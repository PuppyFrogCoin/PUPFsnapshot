import { writeFileSync } from "fs";
const url = `HELIUS SOLANA RPC`;

const getTokenAccounts = async () => {
    let allOwners = new Set();
    let cursor;

    while (true) {
        let params = {
            limit: 1000,
            mint: "B9LeEmSNkGiNAz2iwmPb6cPvwHMhchTNhBJLPBqVYgk7"
        };

        if (cursor != undefined) {
            params.cursor = cursor;
        }

        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                jsonrpc: "2.0",
                id: "helius-test",
                method: "getTokenAccounts",
                params: params,
            }),
        });

        const data = await response.json();

        if (!data.result || data.result.token_accounts.length === 0) {
            console.log("No more results");
            break;
        }

        data.result.token_accounts.forEach((account) => {
            allOwners.add(account.owner);
        });

        cursor = data.result.cursor;
    }
    
    writeFileSync("output.json", JSON.stringify(Array.from(allOwners), null, 2));
}

getTokenAccounts();