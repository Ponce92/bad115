from django.contrib.auth import backends
from .models import Users

class MainAuthBackend(Users):
    """ Email Authentication Backend Allows a user to sign in using an email/password pair, then check
    a username/password pair if email failed """

    def authenticate( username=None, password=None, **kwargs):
        """ Authenticate a user based on email address as the user name. """
        print("-------------------")
        # User = get_user_model()
        try:
            user = Users.objects.get(username=username)
            return user
            # if user.check_password(password):

        except Users.DoesNotExist:
                return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
