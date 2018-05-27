# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
import json


def gen_json():
    uid = "urn:uuid:" + str(uuid.uuid4())
    updateDate = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.0Z")
    titleText = "Panzoto's Artificial Intelligence News Brief"
    mainText = "Intelligent search. Recently, I started working on a business problem, where people want to search relevant material through many sources of documents by asking a question. This can be solved using model such as DrQA, with the data set similar to SQuAD. However, in order to use this model, the training data needs to be in question and answer pairs. This requires a lot of preprocessing to build up a good data set. So the next thing we did is to use Solr to index the database first, creating links to the source and raw text of the source document. Searching by the question against the content of the Solr database, we first find the relevant document. Once we find the relevant document, we first try to use machine comprehension function of AllenNLP to find the answer in the document. However, because AllenNLP use attention model, when the document is large ( > 90,000 characters), the model require too much memory. So we tried Google’s Talk to Book approach. Using Universal Sentence Encoder by tensorflow, we separated the document into pages or paragraphs, and find the most similar page or paragraph to our question. This did not work because our question is in a question form and it is structurally different from the source document content. So we can either compare using a statement form to the document, or convert the document into many questions, and find which paragraph is the most similar to our question. We tried the first option and used a statement to to find the most similar paragraph. It work fine and the 2nd most relevant answer was the one we are looking for. But from a user perspective, we cannot limit the user to not search in a question format. So we used Spacy and filtered out STOP WORDS, which include things like “what”, “how”, “do”, “I” and all the frequent words. This essentially turn question or statement into keywords we can use for search. Another improvement we made was pulling top 3 most relevant document, parsed every paragraph from those documents and find the most relevant paragraph, regardless of where it came from. In this way, we able to rank the most relevant “paragraph” from multiple sources, and improve the search result as a whole."
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
    output = gen_json()
    with open('../alexa.json', 'w') as outfile:
        json.dump(output, outfile)

if __name__ == '__main__':
    main()
