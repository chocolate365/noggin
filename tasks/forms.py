from django import forms
from django.contrib.auth.models import User
from .models import List, Task

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('name', 'lists', 'user_date', 'url', 'notes')
		labels = {
		'name': 'Task', 
		'lists': 'Lists', 
		'user_date': 'Date',
		'url': 'URL'

		}
		widgets = {
		'lists': forms.CheckboxSelectMultiple, 
		'user_date': forms.DateInput,
		'url': forms.URLInput
		}


	def __init__(self, user, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['lists'].queryset = List.objects.filter(owner=user)


class ListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('name',)

	def __init__(self, user, *args, **kwargs):
		super(ListForm, self).__init__(*args, **kwargs)
		#self.fields['tasks'].queryset = Task.objects.filter(owner=user)
		