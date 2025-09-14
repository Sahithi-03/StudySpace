from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('add', views.add, name='add'),
    path('watch', views.watch, name='watch'),
    path('save', views.save, name='save'),
    path('list', views.list, name='list'),
    path('display/<int:item_id>', views.display, name='display'),
    path('delete/<int:item_id>', views.delete, name="delete"),
    path('edit/<int:item_id>', views.edit, name='edit'),
    path('task', views.task, name='task'),
    path('save_t', views.save_t, name='save_t'),
    path('check/<int:task_id>', views.check, name='check'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('quotes', views.quotes, name='quotes')
]