from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('add/', views.add_note, name='add_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('pin/<int:note_id>/', views.pin_note, name='pin_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
]
