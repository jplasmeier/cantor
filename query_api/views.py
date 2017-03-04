from django.contrib.auth.models import User, Group
from query_api.models import QueryObject
from rest_framework import viewsets
from query_api.serializers import UserSerializer, GroupSerializer, QueryObjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QueryObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Query Objects
    """
    queryset = QueryObject.objects.all()
    serializer_class = QueryObjectSerializer

class QueryViewSet(viewsets.ViewSet):
    """
    API endpoint for GeoJSON
    The endpoint should return a "custom" view of GeoJSON
    The GeoJSON being the result of the query operation of the model
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def get(self, request):
        pass
