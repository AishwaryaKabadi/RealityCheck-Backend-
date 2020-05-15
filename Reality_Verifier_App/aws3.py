import boto3

client = boto3.client('s3', region_name='us-west-2')

client.upload_file('images/image_0.jpg', 'mybucket', 'image_0.jpg')
