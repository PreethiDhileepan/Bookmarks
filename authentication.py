
from django.contrib.auth.models import User

from account.models import Profile
from django.contrib.auth import get_user_model


class EmailAuthBackend:

    def authenticate(self,request,username=None,password=None):
        try:
            user =User.objects.get(email=username)
            print('gets user')
            print(user)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def create_profile(backend,user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)


def associate_by_email(strategy, details, user=None, *args, **kwargs):
    """
    If no existing social user is found, try to match by email.
    """
    if user:  # User already found, no need to associate
        return {'user': user}

    email = details.get('email')
    if email:
        User = get_user_model()
        try:
            existing_user = User.objects.get(email=email)
            return {'user': existing_user}  # Return the found user instead of creating a new one
        except User.DoesNotExist:
            pass  # No user found, continue with create_user

    return {}  # Proceed to the next step (create_user)