from etls.aws_etl import connect_to_s3, create_bucket, load_to_s3
import os 
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")
def aws_pipeline(ti):
    file_log = ti.xcom_pull(task_ids='log_extraction')
    user_file = ti.xcom_pull(task_ids='enrich_user', key='new_user_file')

    s3 = connect_to_s3()
    create_bucket(s3)
    s3_key_log = f"logs/{os.path.basename(file_log)}"
    s3_key_user = f"users/{today}_user.csv"

    if not os.path.exists(file_log):
        raise FileNotFoundError(f"There is no file {file_log}")
    load_to_s3(s3,file_log,s3_key_log)
    
    if user_file:
        load_to_s3(s3, user_file, s3_key_user)
    else:
        print("[INFO] No new user file to upload.")