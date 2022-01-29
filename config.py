from pathlib import Path

class Configuration:

    PROJECT = "Kowel"
    ROOT = Path("D:\INNE\Marcin_Marta_files\Big Archive\HISTORY_KOWEL")
    IMAGE_SIZE = 120
    HASH_SIZE = 8
    THUMBNAIL_DIR = 'thumbnails'
    SAVE_FORMAT = 'png'
    #TODO:Currently only supports phash --other models may not have correct params available
    HASH_TO_USE = 'phash'