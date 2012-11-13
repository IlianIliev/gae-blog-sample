from google.appengine.api import users


class AnonymousUser(object):
    """ Anonymous User class allows the attachment of method/properties to
     unidentified users.
    """
    def __nonzero__(self):
        return False

def auth(request):
    """ Add the user to the context """
    user = users.get_current_user() or AnonymousUser()
    if user:
        user.is_admin = users.is_current_user_admin()
        user.logout_url = users.create_logout_url('/')
    else:
        user.login_url = users.create_login_url(request.get_full_path())

    return {
        'user': user,
    }