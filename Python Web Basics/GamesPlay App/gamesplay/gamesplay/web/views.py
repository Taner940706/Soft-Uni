from django.shortcuts import render

def index(request):
	return render(request, 'home-page.html')

def dashboard(request):
	return render(request, 'dashboard.html')

def add_game(request):
	return render(request, 'create-game.html')

def add_profile(request):
	return render(request, 'create-profile.html')

def details_game(request, pk):
	return render(request, 'details-game.html')

def edit_game(request, pk):
	return render(request, 'edit-game.html')

def delete_game(request, pk):
	return render(request, 'delete-game.html')

def details_profile(request):
	return render(request, 'details-profile.html')

def edit_profile(request):
	return render(request, 'edit-profile.html')

def delete_profile(request):
	return render(request, 'delete-profile.html')



