from rest_framework import viewsets, views, response
from .models import Directory, TodoTask
from .serializers import DirectorySerializer, TodoTaskSerializer


class DirectoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on directories.
    """
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer


class TodoTaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on todo tasks.
    """
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

class ClearDataView(views.APIView):
    """
    API endpoint that allows clearing all data from the database.
    """

    def post(self, request, format=None):
        """
        Clears all data from the database.
        """
        Directory.objects.all().delete()
        TodoTask.objects.all().delete()
        return response.Response({'message': 'All data cleared.'})
