from django.shortcuts import render, redirect

from gameplay.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from gameplay.web.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    else:
        context = {
            'profile': profile,
        }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def create_game(request):
    if request.method == "POST":
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()
    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)


def details_profile(request):
    return render(request, 'details-profile.html')


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)
