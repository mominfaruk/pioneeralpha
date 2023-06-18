from django.urls import include, path
from rest_framework import routers
from .views import DirectoryViewSet, TodoTaskViewSet, ClearDataView

router = routers.DefaultRouter()
router.register(r'directories', DirectoryViewSet)
router.register(r'todotasks', TodoTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cleardata/', ClearDataView.as_view(), name='cleardata'),
]
