from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('category/', include('categories.urls')),
    path('task/', include('tasks.urls')),
    path('project/', include('projects.urls')),
    path('schedule/', include('schedule.urls')),
    path('team/', include('team.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)