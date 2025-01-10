# datos_demre/params.py

import os

# Vicente Agüero -> Admisión 2019
ID_AUTHOR = 8151581175172

# Folders
DATA_FOLDER = 'data'
DEMRE_FOLDER = 'demre'
DEMRE_OPEN_FOLDER = 'demre_open'
RAR_FOLDER = 'rar'
DATABASES_FOLDER = 'databases'
FILES_FOLDER = 'files'
DICTIONARIES_FOLDER = 'dictionaries'

# Kedro
RAW_FOLDER = 'raw'

################################################################################

ROOT_PATH = os.path.join(os.getcwd())

DATA_PATH = os.path.join(ROOT_PATH, DATA_FOLDER)

RAW_PATH = os.path.join(DATA_PATH, RAW_FOLDER)
RAW_DEMRE_PATH = os.path.join(RAW_PATH, DEMRE_FOLDER)
RAW_DEMRE_OPEN_PATH = os.path.join(RAW_PATH, DEMRE_OPEN_FOLDER)

RAW_RAR_DEMRE_OPEN_PATH = os.path.join(RAW_DEMRE_OPEN_PATH, RAR_FOLDER)
RAW_DATABASES_DEMRE_OPEN_PATH = os.path.join(RAW_DEMRE_OPEN_PATH, DATABASES_FOLDER)
RAW_FILES_DEMRE_OPEN_PATH = os.path.join(RAW_DATABASES_DEMRE_OPEN_PATH, FILES_FOLDER)
RAW_DICTIONARIES_DEMRE_OPEN_PATH = os.path.join(RAW_DATABASES_DEMRE_OPEN_PATH, DICTIONARIES_FOLDER)
