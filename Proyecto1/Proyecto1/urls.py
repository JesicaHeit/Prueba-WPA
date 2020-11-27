"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import  path,include
from django.conf import settings
from django.conf.urls.static import static

import recetas
from users import views
from users.views import register
from users.views import activate
from users.views import login
from users.views import logout
from users.views import ProfileListView

from users.views import follow_unfollow_profile
from Proyecto1.views import home
from Proyecto1.views import recipes
from Proyecto1.views import pantalla_intermedia
from recetas import views
from recetas.views import post_new
from recetas.views import post_list
from recetas.views import post_detail
from recetas.views import post_list2
from recetas.views import post_edit
from recetas.views import post_detail2
from recetas.views import borrar_receta
from recetas.views import post_of_following_profiles, LikeView, recetas_sandwiches, recetas_sopas, recetas_postres
from recetas.views import search_vista, recetas_entradas, recetas_carnes, recetas_pastas, recetas_veggie, recetas_todas
from recetas.views import add_comment_to_post
from recetas.views import post_of_following_profiles
from recetas.views import ListReports
from users.views import UserEditView,ShowProfilePageView, show_profile, EditPofilePageView
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [

    # Sección para usuarios
    path('', home, name='home'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls, name='administrador'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('login/', login, name='login'),
    path('logout/', logout),
    path('home/', home),
    path('recipes/', login_required(recipes), name='recipes'),
    path ('pantalla_intermedia/', pantalla_intermedia),
    path ('nueva_receta/', post_new, name='post_new'),
    path('receta_user/', post_list2, name='receta_user'),
    path('receta_all/', post_list, name='recetas'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('userpost/<int:pk>/', post_detail2, name='post_detail2'),
    path('edit_profile/<int:pk>', EditPofilePageView.as_view(), name='edit_profile_page'),
    #path('profile/<int:pk>', show_profile, name='show_profile_page'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('borrar/<int:pk>/', borrar_receta, name='borrar_receta'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('recetas_follow/', post_of_following_profiles, name='recetas_follow'),
    path('switch_follow/', follow_unfollow_profile, name ='follow_unfollow_profile'),
    #path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('search2/', search_vista, name = 'search_vista'),
    path('search/', include('haystack.urls')),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('post/<int:pk>/reports/', views.ListReports, name='reports'),
    path('ajax/recetas_entradas/', recetas_entradas),
    path('ajax/recetas_carnes/', recetas_carnes),
    path('ajax/recetas_pastas/', recetas_pastas),
    path('ajax/recetas_veggie/', recetas_veggie),
    path('ajax/recetas_sandwiches/', recetas_sandwiches),
    path('ajax/recetas_sopas/', recetas_sopas),
    path('ajax/recetas_postres/', recetas_postres),
    path('ajax/recetas_todas/', recetas_todas),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
