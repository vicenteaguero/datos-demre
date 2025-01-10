"""
Procesamiento de Datos: Portal Transparencia DEMRE

Author: Vicente Agüero
LinkedIn: https://www.linkedin.com/in/vicente-aguero/

En estas bases de datos, mi ID para 2019 es `8151581175172`.
Esto, pues rendí la PSU en el año 2018, admisión 2019.

Este script realiza el procesamiento de los archivos .rar de los
datos brutos (raw data) provenientes del portal de transparencia del DEMRE.
Organiza y renombra los archivos .csv y .xlsx extraídos, clasificándolos
por año y tipo de dato.
"""

# datos-demre/scripts/raw_processing.py

from tqdm import tqdm
import rarfile
import shutil
import os

from datos_demre.params import (
    RAW_RAR_DEMRE_OPEN_PATH, RAW_FILES_DEMRE_OPEN_PATH, RAW_DICTIONARIES_DEMRE_OPEN_PATH
)

################################################################################

for folder in [RAW_FILES_DEMRE_OPEN_PATH, RAW_DICTIONARIES_DEMRE_OPEN_PATH]:
    os.makedirs(folder, exist_ok=True)

rar_files = sorted([
    f for f in os.listdir(RAW_RAR_DEMRE_OPEN_PATH)
    if f.endswith('.rar') and f.startswith('PROCESO')
])

change_name = {
    'b': 'inscripciones',
    'c': 'resultados',
    'd': 'postulaciones',
    'mat': 'matriculas',
    'matr': 'matriculas',
    'matricula': 'matriculas',
}

for rar_file in tqdm(rar_files):
    year = rar_file.split('-')[3]
    files_year_folder = os.path.join(RAW_FILES_DEMRE_OPEN_PATH, year)
    dictionaries_year_folder = os.path.join(RAW_DICTIONARIES_DEMRE_OPEN_PATH, year)
    os.makedirs(files_year_folder, exist_ok=True)
    rar_file_path = os.path.join(RAW_RAR_DEMRE_OPEN_PATH, rar_file)
    with rarfile.RarFile(rar_file_path) as rf:
        for file in rf.namelist():
            if file.endswith('.csv'):
                csv_file_path = rf.extract(file, files_year_folder)
                new_name = os.path.basename(csv_file_path).lower().split('_')[0]
                new_name = change_name[new_name.replace('archivo', '')]+'.csv'
                new_csv_file_path = os.path.join(files_year_folder, new_name)
                shutil.move(csv_file_path, new_csv_file_path)
            elif file.endswith('.xlsx'):
                xlsx_file_path = rf.extract(file, dictionaries_year_folder)
                new_name = os.path.basename(xlsx_file_path).lower().split('_')[2]
                new_name = change_name[new_name.split('.')[0].replace('archivo', '')]+'.xlsx'
                new_xlsx_file_path = os.path.join(dictionaries_year_folder, 'dict_'+new_name)
                shutil.move(xlsx_file_path, new_xlsx_file_path)
    if os.path.exists(os.path.dirname(csv_file_path)):
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
        if not str(year) == os.path.basename(os.path.dirname(csv_file_path)):
            os.rmdir(os.path.dirname(csv_file_path))
    if os.path.exists(os.path.dirname(xlsx_file_path)):
        if os.path.exists(xlsx_file_path):
            os.remove(xlsx_file_path)
        if not str(year) == os.path.basename(os.path.dirname(xlsx_file_path)):
            os.rmdir(os.path.dirname(xlsx_file_path))
