from google.appengine.api import users

from django.http import HttpResponseRedirect, HttpResponseForbidden

def admin_required_decorator(func):
    def _login_redirect(request):
        return HttpResponseRedirect(users.create_login_url(
                                                    request.path()))
    user = users.get_current_user()
    if user:
        if users.is_current_user_admin():
            return func
        else:
            return HttpResponseForbidden
    else:
        return _login_redirect