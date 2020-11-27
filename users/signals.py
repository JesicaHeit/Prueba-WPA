from django.db.models.signals import post_save
from django.dispath import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def post_Save_create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)