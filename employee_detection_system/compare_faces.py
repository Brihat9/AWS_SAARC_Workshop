import boto3
import base64
import json

client = boto3.client('rekognition')
file = open('../images/kpolitest.jpg', 'rb').read()
CollectionId = "TestCollection"

response = client.detect_faces(
    Image = {
        'Bytes': file
    },
)

if (len(response['FaceDetails']) > 0):
    res = client.search_faces_by_image(
        CollectionId=CollectionId,
        Image = {
            'Bytes': file
        }
    )
    print(res['FaceMatches'])
else:
    print("no faces detected in image")
