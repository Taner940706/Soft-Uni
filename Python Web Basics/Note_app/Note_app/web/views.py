from django.shortcuts import render, redirect

from Note_app.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from Note_app.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def index(request):
    profiles = get_profile()
    notes = Note.objects.all()
    if not profiles:
        return redirect('create profile')
    context = {
        'profiles': profiles,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


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
        'no-profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def create_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects \
        .filter(pk=pk) \
        .get()
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    profiles = get_profile()
    len_note = len(Note.objects.all())
    context = {
        'profiles': profiles,
        'len_note': len_note,
    }
    return render(request, 'profile.html', context)