from django.urls import path
from .views import post_of_following_profiles

app_name='recetas'

urlpatterns=[
    path('', post_of_following_profiles, name='posts-follow-view'),
]