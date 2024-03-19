from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.ProjectModelAPIView)
from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('short_list/', views.ShortScheduleProjectTaskList.as_view(), name='short-schedule-project-task-list'),
    path('count/', views.CountView.as_view(), name='counts'),
]


# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views
# urlpatterns = [
#     path('', views.ProjectModelAPIView.as_view(), name='project_list'),
# ]