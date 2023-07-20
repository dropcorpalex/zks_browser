# main.py
import requests
import time
from utils import to_hex, from_hex  # Import helper functions

class BlockExplorer:
    ...
    def get_block(self, block_number):
        hex_block_number = to_hex(block_number)  # Convert the block number to hex
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [hex_block_number, True],
            "id": 1
        }
        response = requests.post(self.api_url, json=payload)
        return response.json()

def main():
    ...
    while True:
        block = explorer.get_block(0)  # Replace 0 with the actual block number you want to track
        print(block)
        time.sleep(10)

if __name__ == "__main__":
    main()
