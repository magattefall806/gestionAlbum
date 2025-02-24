# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Artist
# from .forms import ArtistForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

# # Liste des artistes
# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'artist/list.html', {'artists': artists})

# # Détails d'un artiste
# def artist_detail(request, pk):
#     artist = get_object_or_404(Artist, pk=pk)
#     return render(request, 'artist/detail.html', {'artist': artist})

# # Créer un artiste
# def artist_create(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('artist_list')
#     else:
#         form = ArtistForm()
#     return render(request, 'artist/form.html', {'form': form})

# # Modifier un artiste
# def artist_update(request, pk):
#     artist = get_object_or_404(Artist, pk=pk)
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, instance=artist)
#         if form.is_valid():
#             form.save()
#             return redirect('artist_list')
#     else:
#         form = ArtistForm(instance=artist)
#     return render(request, 'artist/form.html', {'form': form})

# # Supprimer un artiste
# def artist_delete(request, pk):
#     artist = get_object_or_404(Artist, pk=pk)
#     if request.method == 'POST':
#         artist.delete()
#         return redirect('artist_list')
#     return render(request, 'artist/confirm_delete.html', {'artist': artist})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Connecte l'utilisateur après l'inscription
#             return redirect('artist_list')  # Redirige vers la liste des artistes
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Artist
from .forms import ArtistForm

# Vue pour l'inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte l'utilisateur après l'inscription
            return redirect('artist_list')  # Redirige vers la liste des artistes
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Liste des artistes
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist/list.html', {'artists': artists})

# Détails d'un artiste
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist/detail.html', {'artist': artist})

# Créer un artiste
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'artist/form.html', {'form': form})

# Modifier un artiste
def artist_update(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist/form.html', {'form': form})

# Supprimer un artiste
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        artist.delete()
        return redirect('artist_list')
    return render(request, 'artist/confirm_delete.html', {'artist': artist})