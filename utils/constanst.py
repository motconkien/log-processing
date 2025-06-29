import json
import os

def load_config(config_path="config/config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

config = load_config()

API_URL = config['api_url']
OUTPUT_PATH = config['output_path']
HEADERS = config['headers']
FETCH_INTERVAL = config.get('fetch_interval_sec', 60)
