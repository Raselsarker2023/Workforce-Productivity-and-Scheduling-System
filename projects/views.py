from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import ProjectModel
from schedule. models import ScheduleModel
from tasks. models import TaskModel
from team. models import TeamModel
from .models import ProjectModel
from schedule .serializers import ScheduleModelSerializer
from tasks .serializers import TaskModelSerializer
from .serializers import ProjectModelSerializer
from django.utils import timezone
from . import serializers

class ProjectModelAPIView(viewsets.ModelViewSet):
    queryset = models.ProjectModel.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'user__username', 'priority', 'abandon_reason', 'status']

    



# List API views

class ShortScheduleProjectTaskList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            
            now = timezone.now()

            # Fetch upcoming schedules, projects, and tasks
            upcoming_schedules = ScheduleModel.objects.filter(
                created_by=user,
                reminder_time__isnull=False,
                reminder_time__gt=now
            ).order_by('reminder_time')[:5]

            projects = ProjectModel.objects.filter(
                created_by=user,
                end_date__gt=now
            ).order_by('end_date')[:5]

            tasks = TaskModel.objects.filter(
                user_name=user,  
                end_date__gt=now
            ).order_by('end_date')[:5]


            # Serialize the data
            upcoming_schedules_data = ScheduleModelSerializer(upcoming_schedules, many=True).data
            projects_data = ProjectModelSerializer(projects, many=True).data
            tasks_data = TaskModelSerializer(tasks, many=True).data

            return Response({
                'upcoming_schedules': upcoming_schedules_data,
                'projects': projects_data,
                'tasks': tasks_data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# count view 
class CountView(APIView):
    def get(self, request, format=None):
        project_count = ProjectModel.objects.count()
        schedule_count = ScheduleModel.objects.count()
        task_count = TaskModel.objects.count()
        team_count = TeamModel.objects.count()

        data = {
            'project_count': project_count,
            'schedule_count': schedule_count,
            'task_count': task_count,
            'team_count': team_count,
        }

        serializer = serializers.CountSerializer(data)
        return Response(serializer.data)



# class ProjectModelAPIView(APIView):
#     def get(self, request, pk=None):
#         if pk is not None:
#             project = ProjectModel.objects.get(pk=pk)
#             serializer = ProjectModelSerializer(project)
#             return Response(serializer.data)
#         else:
#             projects = ProjectModel.objects.all()
#             serializer = ProjectModelSerializer(projects, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = ProjectModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None):
#         if pk is not None:
#             project = ProjectModel.objects.get(pk=pk)
#             serializer = ProjectModelSerializer(project, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Please provide a valid project ID.'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None):
#         if pk is not None:
#             project = get_object_or_404(ProjectModel, pk=pk)
#             project.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             ProjectModel.objects.all().delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

