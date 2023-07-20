# logger.py

import logging

def setup_logger():
    logger = logging.getLogger('block-explorer')
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler('block_explorer.log')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger
