import json
import re
import typing

from django.http import HttpRequest, RawPostDataException

from common.models import ContextButtonType, ItemData
from users.models import User


def get_request_data(request: HttpRequest) -> dict:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)
    except RawPostDataException:
        data = dict(request.GET or request.POST)
    return data

def update_context_buttons(buttons_json: str, target: typing.Union[User, ItemData]):
    buttons = json.loads(buttons_json)
    for button in buttons:
        button_type = ContextButtonType.objects.filter(verbose=button["name"]).first()
        if button_type:
            if not button["url"]:
                item_context_button = target.context_buttons.filter(button_type=button_type).first()
                if item_context_button:
                    item_context_button.delete()
            elif re.match(button_type.host_regex, button["url"]):
                item_context_button, create = target.context_buttons.get_or_create(
                    button_type=button_type,
                    defaults={
                        "url": button["url"]
                    }
                )
                if not create:
                    item_context_button.url = button["url"]
                item_context_button.save()
