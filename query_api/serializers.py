from django.contrib.auth.models import User, Group 
from query_api.models import QueryObject
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class QueryObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueryObject
        fields = ('short_description',
                  'long_description',
                  'visual_representation',
                  'geojson_url',
                  'mapbox_aux',)
