import requests
import time 
import os 
import sys 
import pandas as pd 
from utils.constanst import TOKEN

TODAY = pd.Timestamp.now().strftime("%Y-%m-%d")


def load_file_log(log_file):
    if not os.path.exists(log_file):
        print(f"No log file for {TODAY}. Skipping user pipeline.")
        return
    log_df = pd.read_csv(log_file)
    users_urls = log_df['url'].tolist()
    return set(users_urls)

def load_file_users(user_file): 
    if os.path.exists(user_file):
        df = pd.read_csv(user_file)
        users_urls = df['url'].tolist()
        return set(users_urls)
    else:
        return set()
    
def new_urls(urls_today, existed_urls):
    return list(urls_today - existed_urls)

def enrich_user(url):
    header = {"Authorization": f"Bearer {TOKEN}"}
    try:
        res = requests.get(url, headers=header)
        if res.status_code == 200:
            data = res.json()
            return {
                "id":data["id"],
                "login":data['login'],
                "url":data['url'],
                "type":data.get('type'),
                "name":data.get('name'),
                "location":data.get('location'),
                "email": data.get('email')
            }
        else:
            print(f"Failed to fetch {url}: {res.status_code}")
            return None
    except Exception as e:
        print(f"Error for {url}: {e}")
        return None

def get_user_info(new_urls, user_file):
    new_user_data = []
    for url in new_urls:
        data = enrich_user(url)
        if data:
            new_user_data.append(data)
        
    if not new_user_data:
        print("No new user data to write.")
        return

    new_df = pd.DataFrame(new_user_data)
    new_df.fillna("N/A", inplace=True)

    new_df.to_csv(user_file, mode='a', header=False, index=False)
    print(f"Appended {len(new_df)} new users to {user_file}")
    return new_user_data

