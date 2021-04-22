import json

from django.http import HttpResponse


def controller_api(function):
    def wrap(request, *args, **kwargs):
        try:
            return function(request, *args, **kwargs)
        except:
            response = {}
            response['status'] = "failure"
            response['reason'] = "Please check all your data is correct."
            return HttpResponse(json.dumps(response),status=400)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap