
from django.urls import path

from .views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = 'mytodo'

urlpatterns = [
    path('',TaskListView.as_view(), name='task-list'),
    path('create/',TaskCreateView.as_view(), name='task-create'),
    path('detail/<int:pk>/',TaskDetailView.as_view(), name='task-detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]

