from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'', include('core.urls')),
    url(r'', include('article.urls')),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns = staticfiles_urlpatterns() + urlpatterns
