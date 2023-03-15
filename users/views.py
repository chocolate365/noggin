# users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from tasks.models import List
from django.contrib.auth.models import User

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in.')
			last_user = User.objects.get(username=username)
			List.objects.create(name='Priority', owner=last_user, display_order=1)
			List.objects.create(name='Waiting', owner=last_user, display_order=2)
			List.objects.create(name='Go', owner=last_user, display_order=3)
			List.objects.create(name='Do', owner=last_user, display_order=4)
			List.objects.create(name='Call', owner=last_user, display_order=5)
			List.objects.create(name='Groceries', owner=last_user, display_order=6)
			List.objects.create(name='Online', owner=last_user, display_order=7)
			List.objects.create(name='Medical', owner=last_user, display_order=8)
			List.objects.create(name='Money management', owner=last_user, display_order=9)
			List.objects.create(name='Home improvement', owner=last_user, display_order=10)
			List.objects.create(name='Pets', owner=last_user, display_order=11)
			List.objects.create(name='Books to read', owner=last_user, display_order=12)
			List.objects.create(name='Restaurants to try', owner=last_user, display_order=13)
			List.objects.create(name='Vacation places', owner=last_user, display_order=14)
			List.objects.create(name='Gifts to buy', owner=last_user, display_order=15)
			List.objects.create(name='Bucket list', owner=last_user, display_order=16)
			
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)


