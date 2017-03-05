from django.contrib.auth.models import User, Group
from query_api.models import QueryObject, Query
from query_api.data_bridge import text_query
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from query_api.serializers import UserSerializer, GroupSerializer, QueryObjectSerializer, QuerySerializer


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

class QueryViewSet(viewsets.GenericViewSet):
    """
    API endpoint for GeoJSON
    The endpoint should return a "custom" view of GeoJSON
    The GeoJSON being the result of the query operation of the model
    """
    queryset = Query.objects.all()
    # We need to use the serializer for a list of queries
    serializer_class = QuerySerializer

    #@list_route(methods=['GET'])
    def list(self, request):
        queryset = Query.objects.all()
        serializer = QuerySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        return self.get_geojson(request, pk)

    @detail_route(methods=['GET'])
    def get_geojson(self, request, pk=None):
        query = self.get_object()
        return Response(text_query("Hello"))
