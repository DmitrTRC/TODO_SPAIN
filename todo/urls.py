from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('uncomplete/<todo_id>', views.uncomplete_todo, name='uncomplete'),
    path('delete', views.delete_complete, name='deletecomplete'),
    path('deleteall', views.delete_all, name='deleteall'),

]
