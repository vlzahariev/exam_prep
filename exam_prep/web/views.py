from django.shortcuts import render, redirect

from exam_prep.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from exam_prep.web.models import Profile, Album


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'albums': Album.objects.all(),
        'hide_nav_links': True,
    }

    return render(request, 'core/home-with-profile.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def add_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "GET":
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/delete-album.html', context)


def details_profile(request):
    user = get_profile()
    albums_count = Album.objects.count()
    context = {
        "user": user,
        'albums_count': albums_count,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    user = get_profile()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=user)
    else:
        form = ProfileDeleteForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-delete.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)
