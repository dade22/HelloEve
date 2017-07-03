""" from tutorial """
import sys
import json
import random
import requests

from eve import Eve
app = Eve()

@app.route('/hello')
def hello_world():
    return 'hello world!'

@app.route('/hellojson')
def hello_world_json():
    works = []
    for i in range(2):
        works.append(
            {
                'title': 'Book Title #%d' % i,
                'description': 'Description #%d' % i,
                'owner': 'owner_customer',
            }
        )

    r = json.dumps(works)
    return r

if __name__ == '__main__':
    app.run()
