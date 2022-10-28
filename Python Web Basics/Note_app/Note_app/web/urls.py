from django.urls import path

from Note_app.web.views import profile, details_note, delete_note, edit_note, create_note, index, create_profile

urlpatterns = (

    path('', index, name='index'),
    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('profile/', profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
)