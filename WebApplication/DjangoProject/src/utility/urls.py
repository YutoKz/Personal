from django.urls import path

from .views import index

app_name = 'utility'

urlpatterns = [ 
        path('', index, name='utility'), 


]
