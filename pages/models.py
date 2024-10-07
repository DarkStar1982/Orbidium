from django.db import models
from django.contrib import admin

# satellite TLE record + system definition data
class MinorPlanetBody(models.Model):
	asteroid_id = models.IntegerField(default=0, primary_key=True)
	asteroid_name = models.CharField(max_length=255)
	flags_short = models.CharField(max_length=127)
	attributes= models.CharField(max_length=127) # unpacked flags
	magnitude = models.FloatField()
	semimajor_a = models.FloatField(default=0.0)
	radius_a = models.FloatField()
	radius_p = models.FloatField()
	eccentricty = models.FloatField(default=0.0)
	inclination = models.FloatField()
	mean_anomaly = models.FloatField()
	argument_perihelion = models.FloatField()
	asc_node_longitude = models.FloatField()
	mean_daily_motion = models.FloatField() 
