from django.urls import path
from todo_list import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('make_completed/<list_id>', views.make_completed, name='make_completed'),
    path('make_uncompleted/<list_id>', views.make_uncompleted, name='make_uncompleted'),
    path('edit/<list_id>', views.edit, name='edit'),
]
