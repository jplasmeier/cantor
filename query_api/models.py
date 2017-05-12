from django.db import models

class Query(models.Model):
    query_text = models.TextField()

class QueryObject(models.Model):
    short_description = models.CharField(max_length=140)
    long_description = models.TextField()
    visual_representation = models.TextField()
    mapbox_aux = models.TextField()
    query_ref = models.ForeignKey(Query, related_name='query')
    next_query = models.ManyToManyField('self')

    class Meta:
        ordering = ('short_description','long_description',)
"""
class Feature(models.Model):
    dataset = models.ForeignKey(Dataset)
    name = models.CharField(max_length=40)
    description = models.TextField()
    column_name = models.CharField(max_length=100)
    datatype = models.CharField(max_length=40)

class Dataset(models.Model):
    short_name = models.CharField(max_length=40)
    long_name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=140)
    long_description = models.TextField()
    icon = models.CharField(max_length=40)
    initial_feature = models.OneToOneField(Feature)
    table_name = models.CharField(max_length=100)
"""
