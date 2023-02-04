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

	PRIORITIES = (
		(1, 'First thing'),
		(2, 'ASAP'),
		(3, 'Soon'),
		(4, 'Whenever'),
	)

	name = models.CharField(max_length=40)
	notes = models.TextField(blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	user_date = models.DateTimeField(blank=True, null=True)
	priority = models.IntegerField(choices=PRIORITIES, default=3)
	lists = models.ManyToManyField(List, related_name='tasks')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ['priority', '-date_added']

	def __str__(self):
		return self.name

