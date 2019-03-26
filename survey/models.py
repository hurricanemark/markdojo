from django.db import models
import django.utils.timezone as timezone

class SurveyItem(models.Model):
	entry_name = models.CharField('Entry Name', max_length=100)
	content = models.TextField()