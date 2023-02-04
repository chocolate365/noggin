from django import forms
from django.contrib.auth.models import User
from .models import List, Task

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('name', 'lists', 'priority', 'user_date', 'notes', 'url')
		labels = {
		'name': 'What do you want to remember?', 
		'lists': 'Which lists do you want to add to?', 
		'priority': 'Priority', 
		'user_date': 'Would you like to add a date?',
		'url': 'Web site?'

		}
		widgets = {
		'lists': forms.CheckboxSelectMultiple, 
		'priority': forms.RadioSelect, 
		'user_date': forms.DateInput,
		'url': forms.URLInput
		}


	def __init__(self, user, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['lists'].queryset = List.objects.filter(owner=user)


class ListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('name', 'display_order')

	def __init__(self, user, *args, **kwargs):
		super(ListForm, self).__init__(*args, **kwargs)
		#self.fields['tasks'].queryset = Task.objects.filter(owner=user)
		