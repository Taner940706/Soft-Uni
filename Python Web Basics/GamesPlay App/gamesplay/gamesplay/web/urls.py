from django.urls import path
from gamesplay.web.views import index, add_profile, add_game, details_game, edit_game, delete_game, details_profile, edit_profile, delete_profile, dashboard

urlpatterns = (
	path('', index, name='index'),
	path('profile/create/', add_profile, name='add profile'),
	path('dashboard/', dashboard, name='dashboard'),
	path('game/create/', add_game, name='add game'),
	path('game/details/<int:pk>/', details_game, name='details game'),
	path('game/edit/<int:pk>/', edit_game, name='edit game'),
	path('game/delete/<int:pk>/', delete_game, name='delete game'),
	path('profile/details/', details_profile, name='details profile'),
	path('profile/edit/', edit_profile, name='edit profile'),
	path('profile/delete/', delete_profile, name='delete profile'),

)