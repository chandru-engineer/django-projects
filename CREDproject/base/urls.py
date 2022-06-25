from django.contrib import admin
from django.urls import path
from .views import TaskList
from .views import TaskDetails
from .views import TaskCreate
from .views import TaskUpdate
from .views import TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='to-do-list'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
