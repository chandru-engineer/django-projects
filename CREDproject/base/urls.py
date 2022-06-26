from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskList
from .views import TaskDetails
from .views import TaskCreate
from .views import TaskUpdate
from .views import TaskDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('login/', views.CustomLoginView.as_view(), name= 'login'),
    path('', TaskList.as_view(), name='to-do-list'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
