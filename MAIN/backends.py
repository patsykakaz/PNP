from .models import Client

class ClientAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Client.objects.get(email=username)
            return user

            if password == 'master':
                # Authentication success by returning the user
                return user
            else:
                # Authentication fails if None is returned
                return None
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None