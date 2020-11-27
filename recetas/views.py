from itertools import chain
from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Exists, Count
from django.utils import timezone
from .forms import RecetasForm
from users.models import Profile
from Proyecto1 import views
from Proyecto1.views import home
from .models import Receta, Reports
from .forms import CommentForm, ReportsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import management
from django.core.management import call_command
from django.core.management.commands import loaddata
from django.http import JsonResponse

# Create your views here.
@login_required()
def post_new(request):
    if request.method == "POST":
        form = RecetasForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/receta_user')
    else:
        form = RecetasForm()
    #call_command('update_index')  # args and opions are optional.
    return render(request, 'recetas/post_edit.html', {'form': form})

def post_list(request):
    ''
    #if request.user.is_authenticated:
    receta = Receta.objects.all().annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/post_list.html', {'receta': receta})

def post_list2(request):
    if request.user.is_authenticated:
        profile = request.user
        receta = Receta.objects.filter(author=request.user,published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'recetas/post_list2.html', {'page_user': profile,'receta': receta})

def post_detail (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    total_likes=receta.total_likes()
    liked=False
    if receta.likes.filter(id=request.user.id):
        liked=True
    return render(request, 'recetas/post_detail.html', {'receta': receta, 'total_likes':total_likes, 'liked':liked})

def post_detail2 (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/post_detail2.html', {'receta': receta})

def post_edit(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = RecetasForm(request.POST, instance=receta)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.author = request.user
            receta.published_date = timezone.now()
            receta.save()
            return redirect('post_detail', pk=receta.pk)
    else:
        form = RecetasForm(instance=receta)
    return render(request, 'recetas/post_edit.html', {'form': form})

def recetas_todas(request):
    receta = Receta.objects.all().annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_todas.html', {'receta': receta})

def recetas_entradas(request):
    receta = Receta.objects.all().filter(categoria=0).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_entradas.html', {'receta': receta})

def recetas_carnes(request):
    receta = Receta.objects.all().filter(categoria=1).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_carnes.html', {'receta': receta})

def recetas_pastas(request):
    receta = Receta.objects.all().filter(categoria=2).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_pastas.html', {'receta': receta})

def recetas_veggie(request):
    receta = Receta.objects.all().filter(categoria=3).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_veggie.html', {'receta': receta})

def recetas_sandwiches(request):
    receta = Receta.objects.all().filter(categoria=4).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_sandwiches.html', {'receta': receta})

def recetas_sopas(request):
    receta = Receta.objects.all().filter(categoria=5).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_sopas.html', {'receta': receta})

def recetas_postres(request):
    receta = Receta.objects.all().filter(categoria=6).annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/recetas_postres.html', {'receta': receta})

def borrar_receta(request, pk):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Receta.objects.get(pk=pk)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('receta_user')

def LikeView (request, pk):
    receta = get_object_or_404(Receta, id=request.POST.get('receta_id'))
    liked=True
    if receta.likes.filter(id=request.user.id):
        receta.likes.remove(request.user)
        liked=False
    else:
        receta.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))

@login_required()
def add_comment_to_post(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = receta
            comment.save()
            return redirect('post_detail', pk=receta.pk)
    else:
        form = CommentForm(initial={'author':request.user})
    return render(request, 'Comment/add_comment_to_post.html', {'form': form})

def search_vista(request):
    return redirect('/search')

def ListReports(request,pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            reports = form.save(commit=False)
            reports.report = receta
            reports.informer = request.user
            reports.informed = receta.author
            reports.title = receta.title
            if reports.approved_report == True:
               receta.state = 2 #Bloqueada
               
            reports.save()
            
            #receta.save()

            return redirect('post_detail', pk=receta.pk)
    else:
        form = ReportsForm(initial={'informer':request.user, 'informed':receta.author})

    return render(request, 'Reports/reports.html', {'form': form})

def post_of_following_profiles(request):
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.following.all()]
    recetas = []
    qs = None
    for u in users:
        recetas_seguidas = Receta.objects.filter(author=u).order_by("-published_date")
        recetas.extend(list(recetas_seguidas))
    return render(request, 'recetas/main.html', {'recetas':recetas})




