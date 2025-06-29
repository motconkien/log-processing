import json
import os

def load_config(config_path="config/config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

config = load_config()

API_URL = config['github']['api_url']
OUTPUT_LOGS = config['output_logs']
OUTPUT_USERS = config['output_users']
HEADERS = config['github']['headers']
FETCH_INTERVAL = config.get('fetch_interval_sec', 60)
TOKEN = config['github']['token']
