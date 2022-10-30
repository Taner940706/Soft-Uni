from django.shortcuts import render, redirect

from car.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from car.web.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'core/index.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/profile-delete.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    car = Car.objects.all()
    budget = sum(e.price for e in car)
    context = {
        'profile': profile,
        'budget': budget,
    }
    return render(request, 'profile/profile-details.html', context)


def create_car(request):
    if request.method == "POST":
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()
    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "POST":
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def delete_car(request, pk):
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:

        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    car_len = len(cars)
    context = {
        'profile': profile,
        'cars': cars,
        'car_len': car_len,
    }
    return render(request, 'core/catalogue.html', context)
