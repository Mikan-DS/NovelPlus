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

