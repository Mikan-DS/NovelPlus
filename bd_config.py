import json
import os
from pathlib import Path

__all__ = ["default_database"]

BASE_DIR = Path(__file__).resolve().parent

if not os.path.exists('config.json'):
    with open('config.json', 'w', encoding='utf-8') as config_file:
        json.dump({
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': str(BASE_DIR / 'db.sqlite3'),
        }, config_file, ensure_ascii=False, indent=4)


with open('config.json', 'r', encoding='utf-8') as config_file:

    default_database = json.load(config_file)
