
from django.urls import path

from .views import index, koizumi_btn1

app_name = 'env_watcher'

urlpatterns = [ 
        path('', index, name='env-watcher'), 
        path('controllers/koizumi/btn1', koizumi_btn1, name='koizumi-btn1'),



]

