import requests
import time 
import os 
import sys 
import pandas as pd 

last_event_id = None 

def connect_API(API_URL, headers):
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            events = response.json()
            return events
        else:
            print(f"API returned status {response.status_code}")
            return []
    except Exception as e:
        print(f"Exception while connecting API: {e}")
        return []


def fetch_data(events):
    global last_event_id

    new_events = []
    user_urls = set()
    for event in events:
        if last_event_id is None or int(event['id']) > int(last_event_id):
            base = {
                "event_id": event['id'],
                "event_type": event["type"],
                "created_at": event['created_at'],
                "actor": event['actor']['login'],
                'url':event['actor']['url'],
                "repo":event['repo']['name']
            }

            payload = event.get("payload",{})

            base['action'] = payload.get('action')
            if event["type"] == "PushEvent" and "commits" in payload:
                for commit in payload['commits']:
                    row = base.copy()
                    row['commit_sha'] = commit.get("sha")
                    row['commit_message'] = commit.get("message")
                    new_events.append(row)
            else:
                row = base.copy()
                row["commit_sha"] = None
                row["commit_message"] = None
                new_events.append(row)

            #for user 
            user_urls.add(event['actor']['url'])

        else:
            break 
    
    if new_events:
        last_event_id = int(new_events[0]['event_id'])
    
    return new_events
    
def transform_data(new_events):
    df = pd.DataFrame(new_events)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['event_id'] = df['event_id'].astype(int)
    return df 

def load_file(df, file_path):
    df.to_csv(file_path, index = False)