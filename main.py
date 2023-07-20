# main.py
import requests
import time

class BlockExplorer:
    def __init__(self):
        self.api_url = 'https://api.zksync.io/jsrpc'  # Replace with the actual API URL

    def get_block(self, block_number):
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [hex(block_number), True],
            "id": 1
        }
        response = requests.post(self.api_url, json=payload)
        return response.json()

def main():
    explorer = BlockExplorer()
    
    # Run the block explorer every 10 seconds to get new blocks
    while True:
        block = explorer.get_block(0)  # Replace 0 with the actual block number you want to track
        print(block)
        time.sleep(10)

if __name__ == "__main__":
    main()
