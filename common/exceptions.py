import typing

from django.http import JsonResponse, HttpRequest


class NovelPlusHttpExceptionResponse(JsonResponse):
    def __init__(self,
                 request: HttpRequest,
                 message: str,
                 status_code: int = 400,
                 admin_note: typing.Union[None, str, dict] = None,
                 **kwargs):

        answer = {
            'message': message,
        }
        if admin_note is not None:
            if request.user.is_superuser:
                answer['admin_note'] = admin_note

        super().__init__(answer, status=status_code)
