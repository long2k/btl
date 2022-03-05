from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addItem, name='add'),
    path('error/',views.notFound, name='notFound'),
    path('save-item/', views.saveData, name = 'saveData'),
    # path('show/', views.show, name =  'show')
]
