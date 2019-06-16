################
##Elastic Search
################
import requests, json, os
from elasticsearch import Elasticsearch

directory = '/path/to/files/'

#ElasticSearch can be accessed via localhost:9200 on the browser

res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

#Create an index value object

i = 1

#Iterate over each JSON file and import it into Elasticsearch

for shakespeare in os.listdir(directory):
    if shakespeare.endswith(".json"):
        f = open(shakespeare)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket', 
        id=i, body=json.loads(docket_content))
        i = i + 1
        
        
