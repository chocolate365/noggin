# tasks/models.py

from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
	name = models.CharField(max_length=20)
	display_order = models.IntegerField(default=1)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ['display_order']

	def __str__(self):
		return self.name

class Task(models.Model):

	name = models.CharField(max_length=60)
	notes = models.TextField(blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	user_date = models.DateTimeField(blank=True, null=True)
	url = models.URLField(blank=True, null=True)
	lists = models.ManyToManyField(List, related_name='tasks')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	display_order = models.IntegerField (default=1)

	class Meta:
		ordering = ['display_order']


	def __str__(self):
		return self.name

