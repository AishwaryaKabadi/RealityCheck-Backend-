import random
import time
import boto3
from django.conf import settings

DJANGO_AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
DJANGO_AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
DJANGO_AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME


def upload_files_to_s3(image):
    """
    Uploads the InMemory file to the s3 bucket and returns bytes
    """
    random_num = random.randint(0, 1000000)
    curr_timestamp = int(str(time.time()).replace('.', ''))
    file_name = f'media/images-{random_num}{curr_timestamp}-{image}'
    s3 = boto3.client(
        's3',
        aws_access_key_id=DJANGO_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=DJANGO_AWS_SECRET_ACCESS_KEY
    )

    s3.upload_file(image, DJANGO_AWS_STORAGE_BUCKET_NAME, file_name)

    return 'https://esp32cam.s3.us-east-2.amazonaws.com/' + file_name
