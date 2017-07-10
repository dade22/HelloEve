# -*- coding: utf-8 -*-
""" run """
import auth
from eve import Eve
from eve.auth import BasicAuth

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    app.run()
