from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
            if resource in ('zipcodes', 'countries'):
                # 'zipcodes' and 'countries' are public
                return True
            else:
                # all the other resources are secured
                return username == 'admin' and password == 'secret'

a = 1