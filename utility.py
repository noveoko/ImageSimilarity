#convert hash to json compatible
import numpy as np
import json
import logging
from imagehash import _binary_array_to_hex
from imagehash import hex_to_hash

handle = "image-similarity-app"
logger1 = logging.getLogger(handle)

def hash_to_hex_string(hash_array):
    logger1.info("Converting Numpy to JSON")
    try:
        hex_hash = _binary_array_to_hex(hash_array)
        return hex_hash
    except Exception as ee:
        print(ee)
        logger1.warn("Unable to convert NP to JSON {ee}")

def hex_to_binary_hash(hash_string):
    logger1.info('Attempting conversion from hash_string to binary_hash')
    return hex_to_hash(hash_string)