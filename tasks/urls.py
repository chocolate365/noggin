# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('lists/', views.lists, name='tasks-lists'),
    path('tasks/', views.tasks, name='tasks-tasks'),
    path('list/<int:list_id>/', views.list, name='tasks-list'),
    path('list/<int:list_id>/update/', views.updatelist, name='tasks-updatelist'),
    path('list/<int:list_id>/delete/', views.deletelist, name='tasks-deletelist'),
    path('task/<int:task_id>/', views.task, name='tasks-task'),
    path('task/<int:task_id>/update/', views.updatetask, name='tasks-updatetask'),
    path('task/<int:task_id>/delete/', views.deletetask, name='tasks-deletetask'),
    path('new_task/', views.new_task, name='new-task'),
    path('new_list/', views.new_list, name='new-list'),
    path('about/', views.about, name='tasks-about'),
    path('search/', views.search, name='tasks-search'),
    path('priority/', views.priority, name='tasks-priority'),
]
