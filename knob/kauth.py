""" basic auth """
from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    """ simple auth class """
    def check_auth(self, username, password, allowed_roles, resource, method):

        print("%s %s %s %s" % (username, password, resource, method))
        return username == 'admin' and password == 'secret'
'''
        if resource in ('zipcodes', 'countries'):
            # 'zipcodes' and 'countries' are public
            return True
        else:
            # all the other resources are secured
            return username == 'admin' and password == 'secret'
'''
 