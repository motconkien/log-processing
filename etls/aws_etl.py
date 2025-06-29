from utils.constanst import AWS_ACCESS_ID, AWS_SECRET_KEY, AWS_REGION, AWS_BUCKET
import boto3
from botocore.exceptions import ClientError
import sys 

#ETL of AWS 
def connect_to_s3():
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        print("Connect S3 successful")
        return s3
    except Exception as e:
        raise e("No AWS credential found. Please check environment")

def create_bucket(s3):
    try:
        s3.head_bucket(Bucket=AWS_BUCKET)
        print(f"{AWS_BUCKET} existed")
    except ClientError as e:
        err_code = int(e.response['Error']['Code'])
        if err_code == 404:
            print(f"{AWS_BUCKET} hasn't existed. Creating new one...")
            if AWS_REGION:
                s3.create_bucket(
                    Bucket=AWS_BUCKET,
                    CreateBucketConfiguration={'LocationConstraint': AWS_REGION}
                )
            else:
                s3.create_bucket(Bucket=AWS_BUCKET)
            print(f"Bucket {AWS_BUCKET}is created")

def load_to_s3(s3,filename,key):
    try:
        s3.upload_file(filename, AWS_BUCKET, key)
        print(f"File {filename} uploaded")
    except FileNotFoundError:
        print('The file was not found', "\nFile name:", filename, "\nS3_key:", key)