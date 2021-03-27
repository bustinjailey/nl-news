import os
import logging
import newspaper
import boto3
#from aws_xray_sdk.core import xray_recorder
#from aws_xray_sdk.core import patch_all
import jsonpickle

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)
#patch_all()


def main():
    sites = ['https://www.rt.com/', 'https://www.oann.com/', 'https://www.foxnews.com']
    newspapers = []
    for site in sites:
        print('building site: ' + site)
        paper = newspaper.build(url=site, memoize_articles=False)
        newspapers.append(paper)
        print(paper.brand + ' has ' + str(paper.size()) + ' recent articles')

    N_ARTICLES_TO_ANALYZE = 5
    for paper in newspapers:

        if paper.size() == 0:
            continue

        i = 0
        while(i < N_ARTICLES_TO_ANALYZE and i <= paper.size()):
            article = paper.articles[i]
            article.download()
            article.parse()
            article.nlp()
            print(article.keywords)
            i += 1

def lambda_handler(event, context):
    main()

main()
