
from django.urls import path

from .views import index, koizumi_btn1, koizumi_btn2, koizumi_btn3, koizumi_btn4, koizumi_btn5, koizumi_btn6, koizumi_btn7

app_name = 'env_watcher'

urlpatterns = [ 
        path('', index, name='env-watcher'), 
        path('controllers/koizumi/btn1', koizumi_btn1, name='koizumi-btn1'),
        path('controllers/koizumi/btn2', koizumi_btn2, name='koizumi-btn2'),
        path('controllers/koizumi/btn3', koizumi_btn3, name='koizumi-btn3'),
        path('controllers/koizumi/btn4', koizumi_btn4, name='koizumi-btn4'),
        path('controllers/koizumi/btn5', koizumi_btn5, name='koizumi-btn5'),
        path('controllers/koizumi/btn6', koizumi_btn6, name='koizumi-btn6'),
        path('controllers/koizumi/btn7', koizumi_btn7, name='koizumi-btn7'),


]

