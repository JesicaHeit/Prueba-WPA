from django.urls import path

from .views import ProfileListView, follow_unfollow_profile

app_name = 'users'

urlpatterns = [
	path('', ProfileListView.as_view(), name = 'profile-list-view'),
	path('switch_follow/', follow_unfollow_profile, name ='follow_unfollow_profile'),
	path('<pk>/', ProfileDetailView.as_view(), name = 'profile-detail-view'),


]