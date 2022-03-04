from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addItem, name='add'),
    path('error/',views.notFound, name='notFound'),
    path('list/', views.listItem, name= 'listItem'),
    path('save-item/', views.saveData, name = 'saveData')
]
