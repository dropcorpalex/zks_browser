# main.py

import requests
import time
from utils import to_hex, from_hex  # Import helper functions
from logger import setup_logger  # Import logger setup

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
    logger = setup_logger()
    explorer = BlockExplorer()
    
    while True:
        logger.info('Fetching block')
        block = explorer.get_block(0)  # Replace 0 with the actual block number you want to track
        logger.info(f'Block fetched: {block}')
        time.sleep(10)

if __name__ == "__main__":
    main()
