import json
import uuid
from io import BytesIO

import requests
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from common.exceptions import NovelPlusHttpExceptionResponse
from users.models import User


@csrf_exempt
def get_me(request: HttpRequest) -> HttpResponse:
    user: User = request.user

    if user.is_authenticated:
        return JsonResponse(
            user.as_user_info_dict
        )
    else:
        return JsonResponse(
            {
                'username': "Anonymous",
                'firstName': "Гость",
                'lastName': "",
                'isAuthenticated': False
            }
        )


@csrf_exempt
def get_user(request: HttpRequest, user_id: int) -> HttpResponse:
    try:
        user: User = User.objects.get(id=user_id)
        return JsonResponse(user.get_user_page_info_dict(user_id))
    except User.DoesNotExist:
        return NovelPlusHttpExceptionResponse(request, "Пользователь не найдет", 404)
    except Exception as e:
        return NovelPlusHttpExceptionResponse(request, "Произошла ошибка на стороне сервера", 500, repr(e))


@csrf_exempt
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)

    return JsonResponse(
        {
            'username': "Anonymous",
            'firstName': "Гость",
            'lastName': "",
            'isAuthenticated': False
        }
    )


@csrf_exempt
def login_user(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)

    user = authenticate(request, username=data['username'].lower(), password=data['password'])
    if user is not None:
        login(request, user)
        return get_me(request)
    else:
        return NovelPlusHttpExceptionResponse(
            request,
            "Неправильный логин или пароль",
            status=401
        )


@csrf_exempt
def register_user(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)

    if User.objects.filter(username=data['username'].lower()).exists():
        return NovelPlusHttpExceptionResponse(
            request,
            "Пользователь с таким ником уже существует",
            status=401
        )

    user = User.objects.create_user(
        data['username'].lower(),
        data.get('email', None),
        data['password']
    )

    login(request, user)
    return get_me(request)


@csrf_exempt
def login_via_vk(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        'access_token': data['access_token'],
        "client_id": 52316017  # TODO Move to config
    }
    answer = requests.post('https://id.vk.com/oauth2/user_info', headers=headers, data=body)

    if answer.status_code != 200:
        return JsonResponse({'message': answer.text}, status=400)

    vk_user = answer.json()
    vk_user = vk_user['user']

    user, create = User.objects.get_or_create(
        vk_user_id=vk_user.get('user_id'),
        defaults={
            'first_name': vk_user.get('first_name'),
            'last_name': vk_user.get('last_name'),
            'email': vk_user.get('email', None),
            'username': str(vk_user.get('user_id')) + "_" + str(uuid.uuid4())
        }
    )
    if create is True:
        r = requests.get(vk_user.get('avatar').replace("&cs=50x50", "&cs=300x300"))

        avatar = None
        if r.status_code == 200:
            avatar = BytesIO(r.content)
        user.avatar.save(user.username + ".jpg", avatar, save=True)

    login(request, user)

    return get_me(request)
