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

