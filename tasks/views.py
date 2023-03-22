# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, List
from .forms import TaskForm, ListForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	lists = List.objects.filter(owner=request.user)
	priority_list = List.objects.filter(owner=request.user, name='Priority').first()
	print(priority_list)
	if priority_list:
		tasks = priority_list.tasks.order_by('display_order')
	else:
		tasks = Task.objects.filter(owner=request.user)
	
	context = {'lists': lists, 'tasks': tasks}
	return render(request, 'tasks/home.html', context)

@login_required
def lists(request):
	lists = List.objects.filter(owner=request.user)
	tasks = Task.objects.filter(owner=request.user)
	context = {
	'lists': lists, 'tasks': tasks,
	}
	return render(request, 'tasks/lists.html', context)

@login_required
def tasks(request):
	context = {
	'tasks': Task.objects.filter(owner=request.user),
	}
	return render(request, 'tasks/tasks.html', context)

@login_required
def about(request):
	return render(request, 'tasks/about.html')


@login_required
def list(request, list_id):
	lists = List.objects.filter(owner=request.user)
	list_item = List.objects.get(id=list_id)
	list_tasks = list_item.tasks.order_by('display_order')
	context = {'lists': lists, 'list_item': list_item, 'list_tasks': list_tasks}
	return render(request, 'tasks/list.html', context)


@login_required
def task(request, task_id):
	task = Task.objects.get(id=task_id)
	task_lists = task.lists.all()
	context = {'task': task, 'task_lists': task_lists}
	return render(request, 'tasks/task.html', context)


@login_required
def new_list(request):
	if request.method == 'POST':
		form = ListForm(request.user, request.POST)
		if form.is_valid():
			to_save = form.save(commit=False)
			to_save.owner = request.user
			form.display_order = to_save.id
			form.save()
			return redirect('/')
			
	#lists = List.objects.filter(owner=request.user)

	#context = {"form": form, "lists": lists}
	form = ListForm(request.user)
	#tasks = Task.objects.filter(owner=request.user)
	#lists = List.objects.filter(owner=request.user)
	#context = {"form": form, 'tasks': tasks, 'lists': lists}
	context = {"form": form}
	return render(request, 'tasks/new_list.html', context)


@login_required
def new_task(request):
	if request.method == 'POST':
		form = TaskForm(request.user, request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.display_order = Task.objects.filter(owner=request.user).count() + 1
			task.owner = request.user
			form.save()
			return redirect('tasks-task', task_id=task.id)
			#return redirect('/')

	form = TaskForm(request.user)
	#tasks = Task.objects.filter(owner=request.user)
	#lists = List.objects.filter(owner=request.user)

	#context = {"form": form, "tasks": tasks, "lists": lists}
	context = {"form": form}
	return render(request, 'tasks/new_task.html', context)


@login_required
def search(request):
	searchTerm = request.GET.get('searchNoggin')
	if searchTerm:
		
		tasks = Task.objects.filter(owner=request.user).filter(name__icontains=searchTerm)
		lists = List.objects.filter(owner=request.user).filter(name__icontains=searchTerm)
	else:
		tasks = Task.objects.filter(owner=request.user)
		lists = List.objects.filter(owner=request.user)
		
	return render(request, 'tasks/search.html', {'searchTerm': searchTerm, 'tasks': tasks, 'lists': lists})


@login_required
def updatetask(request, task_id):
	task = get_object_or_404(Task, pk=task_id, owner=request.user)
	#task = Task.objects.get(id=task_id)
	#if task.owner != request.user:
	#	return redirect('/')
	if request.method == "GET":
		form = TaskForm(request.user, instance=task)
		return render(request, 'tasks/updatetask.html', {'task': task, 'form': form})
	else:
		try:
			form = TaskForm(request.user, request.POST, instance=task)
			form.save()
			return redirect('tasks-task', task_id=task.id)
			#return redirect('/')
		except ValueError:
			return render(request, 'tasks/updatetask.html', {'review': review, 'form': form, 'error': 'Bad date in form'})

	task_lists = task.lists.all()
	#lists = List.objects.all()
	#tasks = Task.objects.all()
	#context = {'task': task, 'task_lists': task_lists, 'lists': lists, 'tasks': tasks}
	context = {'task': task, 'task_lists': task_lists}
	return render(request, 'tasks/task.html', context)


@login_required
def deletetask(request, task_id):
	task = get_object_or_404(Task, pk=task_id, owner=request.user)
	task.delete()
	return redirect('/')


@login_required
def updatelist(request, list_id):
	list = get_object_or_404(List, pk=list_id, owner=request.user)
	#task = Task.objects.get(id=task_id)
	#if task.owner != request.user:
	#	return redirect('/')
	if request.method == "GET":
		form = ListForm(request.user, instance=list)
		return render(request, 'tasks/updatelist.html', {'list': list, 'form': form})
	else:
		try:
			form = ListForm(request.user, request.POST, instance=list)
			#form = ListForm(request.POST, instance=list)
			form.save()
			#return redirect('/')
			return redirect('tasks-list', list_id=list.id)
		except ValueError:
			return render(request, 'tasks/updatelist.html', {'list': list, 'form': form, 'error': 'Bad data in form'})

	form = ListForm(request.user, instance=list)
	lists = List.objects.filter(owner=request.user)
	tasks = Task.objects.filter(owner=request.user)
	context = {'form': form, 'lists': lists, 'tasks': tasks}
	return render(request, 'tasks/list.html', context)


@login_required
def deletelist(request, list_id):
	list = get_object_or_404(List, pk=list_id, owner=request.user)
	if list.name != 'Priority':
		list.delete()
	else:
		print('Priority list cannot be deleted')
	lists = List.objects.filter(owner=request.user)
	return redirect('/')


def sort(request):
    list_pks_order = request.POST.getlist('list_order')
    lists = []
    for idx, list_pk in enumerate(list_pks_order, start=1):
        userlist = List.objects.get(pk=list_pk)
        if idx != userlist.display_order:
        	userlist.display_order = idx
        	userlist.save()
        lists.append(userlist)

    return render(request, 'partials/list-list.html', {'lists': lists})

def sorttask(request):
    task_pks_order = request.POST.getlist('task_order')

    tasks = []
    for idx, task_pk in enumerate(task_pks_order, start=1):
        usertask = Task.objects.get(pk=task_pk)
        if idx != usertask.display_order:
        	usertask.display_order = idx
        	usertask.save()
        tasks.append(usertask)

    return render(request, 'partials/task-list.html', {'tasks': tasks})

def sortmini(request):
	
	# task_pks_order is a list of the sorted primary keys
	task_pks_order = request.POST.getlist('task_order')

	# initialize a list of updated sorted tasks to pass back to the template
	list_tasks = []
	# loop through the list of sorted primary keys, indexing from 1
	for idx, task_pk in enumerate(task_pks_order, start=1):
		# get the task that has that primary key
		usertask = Task.objects.get(pk=task_pk)
		# if the index is not equal to that task's display order
			# set its display order to the index
			# save it to the database
		if idx != usertask.display_order:
			usertask.display_order = idx
			usertask.save()
		
		# add the database task to the list begin passed back
		list_tasks.append(usertask)

	# get all tasks from the updated table
	all_tasks = Task.objects.filter(owner=request.user)
	all_tasks_pks_order = [item.pk for item in all_tasks]
	
	# now straighten out the display order in the entire table after sorted tasks added
	for idx, task_pk in enumerate(all_tasks_pks_order, start=1):
		# get the task that has that primary key
		usertask = Task.objects.get(pk=task_pk)
		# if the index is not equal to that task's display order
			# set its display order to the index
			# save it to the database
		if idx != usertask.display_order:
			usertask.display_order = idx
			usertask.save()

	return render(request, 'partials/task-mini.html', {'list_tasks': list_tasks})
