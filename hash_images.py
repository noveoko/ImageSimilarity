from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from operator import attrgetter
from webbrowser import get
from PIL import Image
import imagehash
from pathlib import Path
from glob import glob
import mimetypes
import os.path as pth
import json
from config import Configuration
from resize_image import image_thumbnail
from config import Configuration
import logging
import utility

logging.basicConfig(filename='app.log')
logging.basicConfig(level=logging.NOTSET)
handle = "image-similarity-app"
logger1 = logging.getLogger(handle)


def get_all_images(root):
    logger1.info('Getting all image paths')
    files = [a for a in glob(root.as_posix() + "\**", recursive=True) if pth.isfile(a)]
    image_ext = ['jpg','jpeg','png','tiff','gif']
    return [a for a in files if any([i in a for i in image_ext])]

def get_image_hash(image):
    logger1.info(f'getting image hash {image}')
    assert pth.isfile(image),'Not a file!'
    try:
        logger1.info(f'attempting to process {image}')
        return getattr(imagehash, Configuration.HASH_TO_USE)(Image.open(image),hash_size=Configuration.HASH_SIZE)
    except Exception as ee:
        logger1.error(f"file: {image}, error:{ee}")
        print(image, ee)

def image_diff(hash_1, hash_2):
    logger1.info('getting image diff {hash_1} {hash_2}')
    return 1 - (hash_1 - hash_2)

def all_image_hashes():
    list_of_images = get_all_images(ROOT)
    logger1.info(f'getting all image hashes size: {len(list_of_images)}')
    images = {}
    for image in list_of_images:
        hash = get_image_hash(image)
        serialized_hash = utility.hash_to_hex_string(hash)
        path_to_thumbnail = image_thumbnail(image)
        if hash:
            images[image] = {'hash':serialized_hash, 'similar':{}, 'thumbnail':path_to_thumbnail}
    return images

def all_image_hashes_report(image_hash_dict):
    logger1.info('generating report')
    with open('image_hashes.json','w') as outfile:
        to_json = json.dumps(image_hash_dict, sort_keys=True)
        outfile.write(to_json)

if __name__ == "__main__":
    ROOT = Configuration.ROOT
    hash_dict = all_image_hashes()
    all_image_hashes_report(hash_dict)


