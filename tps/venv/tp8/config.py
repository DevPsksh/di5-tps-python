import json

CONFIG_FILE_PATH = "config.json"


def load():
    return json.load(open(CONFIG_FILE_PATH, encoding='utf-8'))

