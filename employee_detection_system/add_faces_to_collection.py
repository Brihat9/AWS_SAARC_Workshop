import boto3
import base64

client = boto3.client('rekognition')

file = open('../images/screenshot.png', "rb").read()

CollectionId = "TestCollection"

response = client.index_faces(
    CollectionId = CollectionId,
    Image={
        'Bytes': file
    },
    ExternalImageId="Group",
)

print(response)
