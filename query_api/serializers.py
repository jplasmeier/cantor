from django.contrib.auth.models import User, Group 
from query_api.models import QueryObject, Query
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
    #query = serializers.HyperlinkedRelatedField(view_name='queries', read_only=True)

    class Meta:
        model = QueryObject
        fields = ('short_description',
                  'long_description',
                  'visual_representation',
                  'next_query',
                  'query_ref',
                  'mapbox_aux',)

class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('url', 'query_text')
