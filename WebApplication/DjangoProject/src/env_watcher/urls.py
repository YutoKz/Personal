
from django.urls import path

from .views import index

app_name = 'env_watcher'

urlpatterns = [
    path('', index, name='env-watcher'),
]

