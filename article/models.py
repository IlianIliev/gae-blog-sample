from datetime import datetime

from google.appengine.ext import db
from django.utils.translation import ugettext_lazy as _

from core.models import UniqueConstrainViolated


class Article(db.Model):
    title = db.StringProperty()
    slug = db.StringProperty()
    content = db.TextProperty()
    published = db.BooleanProperty()
    publish_date = db.DateTimeProperty()

    def __unicode__(self):
        return self.title

    def put(self, **kwargs):
        x = Article.all().filter('slug =', self.slug).get()
        if x and x.key() != self.key():
            raise UniqueConstrainViolated(_(u'Slug must be unique'))
        return super(self.__class__, self).put(**kwargs)

    @classmethod
    def published_query(cls):
        return db.Query(Article).filter('published =', True).filter('publish_date <=', datetime.now())