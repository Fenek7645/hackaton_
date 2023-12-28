from django.utils import timezone
from .models import UserPageVisit



class UserPageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Сохранение информации о посещенной странице
        if request.user.is_authenticated and request.path != '/admin/':  # Игнорируем посещения админки
            UserPageVisit.objects.create(
                user=request.user,
                visited_at=timezone.now(),
                page_visited=request.path
            )

        return response