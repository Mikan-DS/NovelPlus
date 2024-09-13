from django.http import JsonResponse, HttpResponse, HttpRequest

from users.models import User


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
                'isAdmin': user.is_staff
            }
        )
    else:
        return JsonResponse(
            {
                'username': "Anonymous",
                'firstName': "Гость",
                'lastName': "",
            }
        )

