# -*- coding: utf-8 -*-
#!/usr/bin python3.5

""" from tutorial """
import sys
import json
import random
import requests

from eve import Eve

print("initialization eve..")
app = Eve()

print("defining routes..")

@app.route('/hello')
def hello():
    return 'hello world!'

@app.route('/hellojson')
def hellojson():
    works = []
    for i in range(2):
        works.append(
            {
                't': 'Book Title #%d' % i,
                'd': 'Description #%d' % i,
                'o': 'own_json',
            }
        )

    r = json.dumps(works)
    return r

@app.route('/helloxml')
def helloxml():
    rXml="""<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>"""
    from flask import Response
    r = Response(response=rXml, status=200, mimetype="application/xml")
    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r

print("http://127.0.0.1:5000/hello")
print("http://127.0.0.1:5000/hellojson")
print("http://127.0.0.1:5000/helloxml")

if __name__ == '__main__':
    print("starting eve..")
    app.run()
