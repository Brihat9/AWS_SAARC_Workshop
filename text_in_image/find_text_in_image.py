import boto3
import base64
import json

client = boto3.client('rekognition')

file = open("../images/text_in_file.png", 'rb').read()

response = client.detect_text(
    Image = {
        'Bytes': file,
    }
)

# print(response['TextDetections'])
texts = []

for text in response['TextDetections']:
    # print(json.dumps(text, indent=4, sort_keys=True))
    if(text['Type'] == "WORD"):
        texts.append(text["DetectedText"])

print(" ".join(texts))
