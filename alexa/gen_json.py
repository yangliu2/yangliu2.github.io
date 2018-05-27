import uuid
from datetime import datetime
import json


def gen_json():
    uid = "urn:uuid:" + str(uuid.uuid4())
    updateDate = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.0Z")
    titleText = "Panzoto's Artificial Intelligence News Brief"
    mainText = "MESSAGE HERE"
    redirectionUrl = "https://data.panzoto.com"

    output = {}
    output['uid'] = uid
    output['updateDate'] = updateDate
    output['titleText'] = titleText
    output['mainText'] = mainText
    output['redirectionUrl'] = redirectionUrl

    return output

def main():
    output = gen_json()
    with open('alexa.txt', 'w') as outfile:
        json.dump(output, outfile)

if __name__ == '__main__':
    main()
