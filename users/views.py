import json

from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from users.models import User


@csrf_exempt
def get_me(request: HttpRequest) -> HttpResponse:
    user: User = request.user

    if user.is_authenticated:
        return JsonResponse(
            {
                'username': user.username,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
                'avatar': user.avatar.url if user.avatar else None,
                'isAdmin': user.is_staff,
                'isAuthenticated': True
            }
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
        return HttpResponse(
            "invalid username or password",
            status=401
        )

@csrf_exempt
def register_user(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        data = dict(request.GET or request.POST)

    if User.objects.filter(username=data['username'].lower()).exists():
        return JsonResponse(
            {
                'message': "username already exists"
            },
            status=400
        )

    user = User.objects.create_user(
        data['username'].lower(),
        data.get('email', None),
        data['password']
    )

    login(request, user)
    return get_me(request)
