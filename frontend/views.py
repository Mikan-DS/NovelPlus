from django.shortcuts import render

from common.models import ItemData
from users.models import User

TITLE_TAGS = [
    "Визуальные новеллы",
    "NovelPlus"
]

pages = {
    "store": "Игры и ассеты",
    "vacancy": "Вакансии визуальных новелл"
}


def app(request):
    return render(request, 'frontend/app.html', {"title": "Визуальные новеллы | NovelPlus"})


def store(request, page=None):
    titles = []
    if page:
        titles.append(
            {"game": "Игры", "sprite": "Спрайты"}.get(page, "Другое")
        )
    else:
        titles.append("Игры и ассеты")

    title = " | ".join(titles + TITLE_TAGS)

    return render(request, 'frontend/app.html', {"title": title})


def vacancy(request, page=None):
    titles = []
    if page:
        titles.append(
            {"developer": "Поиск разработчиков для визуальных новелл",
             "project": "Поиск проектов визуальных новелл для разработчиков"}.get(page, "Другое")
        )
    else:
        titles.append("Вакансии визуальных новелл")

    title = " | ".join(titles + TITLE_TAGS)

    return render(request, 'frontend/app.html', {"title": title})


def item_page(request, collection, item_id):
    titles = []
    try:
        item = ItemData.objects.get(collection__name=collection, id=item_id)
        titles.append(item.title)
        titles.append(item.collection.verbose)
    except ItemData.DoesNotExist:
        titles.append("Страница не найдена")

    title = " | ".join(titles + TITLE_TAGS)

    return render(request, 'frontend/app.html', {"title": title})


def about(request):
    return render(request, 'frontend/app.html', {"title": "О проекте | Визуальные новеллы | NovelPlus"})


def user(request, user_id):
    titles = []
    try:
        user = User.objects.get(id=user_id)
        titles.append("Страница пользователя "+user.username)
    except ItemData.DoesNotExist:
        titles.append("Страница не найдена")

    title = " | ".join(titles + TITLE_TAGS)

    return render(request, 'frontend/app.html', {"title": title})
