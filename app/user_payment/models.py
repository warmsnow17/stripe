from django.db import models


class Item(models.Model):
	class Meta:
		verbose_name_plural = 'Товар'

	name = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	price = models.IntegerField()
