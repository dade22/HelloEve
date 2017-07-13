# -*- coding: utf-8 -*-
""" run """
from eve import Eve
#from kauth import MyBasicAuth

if __name__ != '__main__':
    exit()

app = Eve() #auth=MyBasicAuth)

@app.route('/zipcodes')
def zipcodes():
    """ zipcodes """
    return 'hello zipcodes!'

@app.route('/resources')
def resources():
    """ resources """
    return 'hello resources!'

@app.route('/other')
def other():
    """ other """
    return 'hello other!'

print('start')
app.run()
print('end')