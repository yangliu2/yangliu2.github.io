# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
import json


def gen_json():
    uid = "urn:uuid:" + str(uuid.uuid4())
    updateDate = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.0Z")
    titleText = "Panzoto's Artificial Intelligence News Brief"
    mainText = "You know how powerful transfer learning is for image processing? Now imagine you can do the same for text and even sequence in general. This is what fast.ai can do. Checkout Universal Language Model Fine-tuning"
    # print type(mainText)
    redirectionUrl = "https://data.panzoto.com"

    output = {}
    output['uid'] = uid
    output['updateDate'] = updateDate
    output['titleText'] = titleText
    output['mainText'] = mainText
    output['redirectionUrl'] = redirectionUrl

    return output

def main():

    # save to published alex.json file
    output = gen_json()
    with open('alexa.json', 'w') as outfile:
        json.dump(output, outfile)

    # read and save the old alexa.json object for archieve
    with open("alexa/brief_archieve.json", mode='r') as feedsjson:
        feeds = json.load(feedsjson)

    with open("alexa/brief_archieve.json", mode='w') as feedsjson:
        feeds.append(output)
        json.dump(feeds, feedsjson)

if __name__ == '__main__':
    main()
