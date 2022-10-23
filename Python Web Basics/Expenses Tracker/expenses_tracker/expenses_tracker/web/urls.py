from django.urls import path

from expenses_tracker.web.views import show_index, edit_expense, delete_expense, show_profile, edit_profile, \
    delete_profile, create_expense, create_profile

urlpatterns = (
    path('', show_index, name='show index'),

    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),

    # profile doesnt created, not include in exam, when alone must get it
    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show_profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
