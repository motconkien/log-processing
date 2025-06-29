from etls.users_etls import *
import os
from utils.constanst import OUTPUT_USERS
from datetime import datetime


def user_pipeline(ti, user_file):
    file_today = ti.xcom_pull(task_ids='log_extraction')
    print(f"[DEBUG] File path from XCom: {file_today}")
    print(f"[DEBUG] File exists: {os.path.exists(user_file)}")

    today_user_urls = load_file_log(file_today)
    existed_user_urls = load_file_users(user_file)
    new_user_urls = new_urls(today_user_urls,existed_user_urls)
    print(f"[INFO] Found {len(new_user_urls)} new user URLs.")

    file_path = f"{OUTPUT_USERS}/{user_file}.csv"
    new_user_data = get_user_info(new_user_urls,file_path)
    print(f"[INFO] Enriched {len(new_user_data)} users.")
    
    if new_user_data is not None and not new_user_data.empty:
        tmp_path = f"/tmp/new_users_{datetime.now().strftime('%Y%m%d')}.csv"
        new_user_data.to_csv(tmp_path, index=False)
        ti.xcom_push(key='new_user_file', value=tmp_path)