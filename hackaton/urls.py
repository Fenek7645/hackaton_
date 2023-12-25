from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

 

# Здесть мы отслеживаем url адреса по которым переходит пользователь

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('regestration/', include('regestration.urls')), 
    path('courses/', include('courses.urls')),
    path('game/', include('game.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
