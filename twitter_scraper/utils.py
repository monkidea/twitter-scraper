import pandas as pd
import csv


''' Get the list of urls from dataset '''
def get_urls(filename='seeds.csv', index=-1):
    df = pd.read_csv(filename,dtype=object)
    tweet_ids = df.ix[:,index]
    return [ 'https://twitter.com/anyuser/status/' + tweet_id for tweet_id in list(tweet_ids) ]

''' Get tweet ids and sentiments 
def get_(filename, tid):
    with open(filename) as f:
        reader = csv.reader(f)
        _list = list(reader)
    return [ item[tid] for item in _list ]
'''

''' extract tweet_id from url '''
def url2id(url):
    return url.split('/')[-1].replace('/','')

