from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest, JsonResponse

from common.exceptions import NovelPlusHttpExceptionResponse
from common.models import ItemData


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
