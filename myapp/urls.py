from django.urls import path
from . import views
from myapp.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name = 'team'),
    path('task/', views.task, name = 'task'),
    path('formname/', views.formname, name = 'formname'),

    path('description/<str:wbsnb>', views.get_description, name = 'description'),

    path('get_info/<str:tablename>', views.get_info, name = 'get_info'),

    path('upload/', views.upload, name='upload'),
    path('test/', views.test),
    path('test2/', views.test2),
    path('uploadtest2/', views.uploadtest2, name='uploadtest2'),
]