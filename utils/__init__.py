import json

from django.http import HttpRequest


def get_request_data(request: HttpRequest) -> dict:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)
    return data
