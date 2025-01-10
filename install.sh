# install.sh

pip install poetry

poetry config virtualenvs.in-project true
poetry install

poetry run python datos_demre/scripts/raw_processing.py