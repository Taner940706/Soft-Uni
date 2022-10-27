from django.urls import path

from library.web.views import index, add_book, edit_book, details_book, profile_user, edit_profile, delete_profile, \
    create_profile

urlpatterns = (

    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('profile/', profile_user, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
