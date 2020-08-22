import boto3
import os
import base64
import json

client = boto3.client('rekognition')

# if aws cli is not configured
# client = boto3.client('rekognition', aws_session_token="", aws_access_key_id="", aws_secret_access_key="", region_key="")
# client = boto3.client('rekognition', aws_session_token=os.getenv(''), aws_access_key_id=os.getenv(''), aws_secret_access_key=os.getenv(''), region_key=os.getenv(''))

file = open('../images/rajeshhamal.jpg', 'rb').read()

response = client.detect_faces(
    Image = {
        'Bytes': file
    },
    Attributes= ['ALL']
)

# print(response['FaceDetails'])

for face in response['FaceDetails']:
    print(json.dumps(face, indent=4, sort_keys=True))
