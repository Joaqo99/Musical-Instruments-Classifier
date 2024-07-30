import boto3

BUCKET_NAME = "mic-dataset"
s3 = boto3.client("s3")

def get_train_data():
    pass

def get_test_data():
    pass

resp = s3.list_objects_v2(Bucket=BUCKET_NAME)
for obj in resp["Contents"]:
    print(obj)