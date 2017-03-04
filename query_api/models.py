from django.db import models

class QueryObject(models.Model):
    short_description = models.CharField(max_length=140)
    long_description = models.TextField()
    visual_representation = models.TextField()
    geojson_url = models.CharField(max_length=511)
    mapbox_aux = models.TextField()

    class Meta:
        ordering = ('short_description','long_description',)

class Query(models.Model):
    query_text = models.TextField()
