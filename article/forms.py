from datetime import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from core.utils import update_entity_properties, get_entity_properties

from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField(required=False)
    content = forms.CharField(widget=forms.Textarea)
    published = forms.BooleanField(required = False)
    publish_date = forms.DateTimeField(initial=datetime.now)

    def __init__(self, instance=None, *args, **kwargs):
        self.instance = instance
        if instance:
            kwargs['initial'] = get_entity_properties(instance)
        return super(self.__class__, self).__init__(*args, **kwargs)

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        x = Article.all().filter('slug =', slug).get()
        if x and x.key() != self.instance.key():
            raise forms.ValidationError(_(u'Slug must be unique')) 
        return slug

    def save(self):
        if not self.cleaned_data['slug']:
            self.cleaned_data['slug'] = unicode(slugify(self.cleaned_data['title']))
        if self.instance:
            article = update_entity_properties(self.instance, self.cleaned_data)
        else:
            article = Article(**self.cleaned_data)
        return article.put()