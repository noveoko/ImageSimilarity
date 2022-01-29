from PIL import Image
from uuid import uuid4
from config import Configuration
import logging

handle = "image-similarity-app"
logger1 = logging.getLogger(handle)

def image_thumbnail(image_path):
    """Squeeze image down to square thumbnail"""
    logger1.info("Creating thumbnail: {image_path}")
    try:
        square_dimensions = Configuration.IMAGE_SIZE
        im = Image.open(image_path)
        newsize = (square_dimensions, square_dimensions)
        im1 = im.resize(newsize)
        return im1
    except Exception as ee:
        logger1.warn(r'Unable to create thumbnail: {ee}')

def save_image(hash, image_path):
    """Save image to new path"""
    logger1.info("Saving image {image_path} with hash {hash}")
    new_image = image_thumbnail(image_path)
    new_path = f"{Configuration.THUMBNAIL_DIR}/{hash}_{uuid4()}.{Configuration.SAVE_FORMAT}"
    new_image.save(new_path)
    return new_path

