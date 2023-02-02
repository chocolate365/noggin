from django import forms
from django.contrib.auth.models import User
from .models import List, Task

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('name', 'lists', 'priority', 'user_date', 'notes')
		labels = {
		'name': 'What do you want to remember?', 
		'lists': 'Which lists do you want to add to?', 
		'priority': 'Priority', 
		'user_date': 'Would you like to add a date?'

		}
		widgets = {
		'lists': forms.CheckboxSelectMultiple, 
		'priority': forms.RadioSelect, 
		'user_date': forms.DateInput
		}


	def __init__(self, user, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['lists'].queryset = List.objects.filter(owner=user)


class ListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('name', 'display_order')
		