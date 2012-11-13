import types

from django.shortcuts import render_to_response
from django.template.context import RequestContext


class RequestMiddleware(object):
    def render(self, request, template, context):
        return render_to_response(template, context, RequestContext(request))

    def process_request(self, request):
        request.render = types.MethodType(self.render, request)


