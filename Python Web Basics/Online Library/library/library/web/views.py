from django.shortcuts import render, redirect

from library.web.forms import CreateProfileForm, CreateBookForm, EditBookForm, EditProfileForm, DeleteProfileForm
from library.web.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def index(request):
    profile = get_profile()
    book = Book.objects.all()
    counter = 0
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,
        'book': book,
        'counter': counter,

    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm(request.FILES)
    context = {
        'form': form,
        'no-profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        'book': book,
        }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def profile_user(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST,  request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST,  request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
