import json
import re

from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse

from common.exceptions import NovelPlusHttpExceptionResponse
from common.models import ItemData, ContextButtonType
from users.models import User
from utils import get_request_data, update_context_buttons


def get_cards(request: HttpRequest, variant: str, collection: str) -> HttpResponse:
    try:
        cards = []
        items: QuerySet[ItemData] = ItemData.objects.filter(
            collection__name=collection).order_by('-updated_at', '-created_at')
        if variant == 'store':
            for item in items:
                cards.append(item.card_dict)
        elif variant == 'vacancy':
            for item in items:
                cards.append(item.mini_card_dict)

        return JsonResponse({
            'cards': cards
        })
    except Exception as e:
        return NovelPlusHttpExceptionResponse(
            request,
            "Exception",
            500,
            {"message": repr(e)}
        )


def get_item(request: HttpRequest, collection: str, item_id: int) -> HttpResponse:
    try:
        item: ItemData = ItemData.objects.get(collection__name=collection, id=item_id)
        return JsonResponse(item.item_dict)
    except Exception as e:
        return NovelPlusHttpExceptionResponse(
            request,
            "Exception",
            500,
            {"message": repr(e)}
        )


def update_item(request):
    data = get_request_data(request)
    user: User = request.user
    item: ItemData = ItemData.objects.filter(
        id=data['id'][0]
    ).first()
    if item is None:
        return NovelPlusHttpExceptionResponse(request, "Такого объекта не существует", status=403)

    try:
        if not (user.id == int(data['author'][0]) == item.author.id):
            return NovelPlusHttpExceptionResponse(request, "Вы не имеете право на эту операцию", status=403)
    except KeyError:
        return NovelPlusHttpExceptionResponse(request, "Вы не имеете право на эту операцию", status=403)
    except ValueError:
        return NovelPlusHttpExceptionResponse(request, "Вы не имеете право на эту операцию", status=403)

    for change in data['changes']:
        if change == "image":
            try:
                item.image.save(user.username + str(item.id) + ".jpg", request.FILES['image'], save=False)
            except Exception as e:
                return NovelPlusHttpExceptionResponse(request, "Произошла ошибка", 500, repr(e))
        elif change == "contextButtons":
            update_context_buttons(data.get(change)[0], item)
        else:
            setattr(item, change, data.get(change)[0])

    item.save()

    return JsonResponse({"success": True})


def context_buttons_list(request):
    return JsonResponse(
        {
            "success": True,
            "context_buttons": [cb.verbose for cb in ContextButtonType.objects.all()]
        }
    )
