from django.urls import path

from car.web.views import index, create_profile, catalogue, create_car, details_car, edit_car, delete_car, \
    details_profile, edit_profile, delete_profile

urlpatterns = (

    path('', index, name='index'),
    path('profile/create/', create_profile, name='create profile'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/create/', create_car, name='create car'),
    path('car/<int:pk>/details/', details_car, name='details car'),
    path('car/<int:pk>/edit/', edit_car, name='edit car'),
    path('car/<int:pk>/delete/', delete_car, name='delete car'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)