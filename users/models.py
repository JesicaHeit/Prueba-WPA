from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User

class UsuarioGeneral(User):
    pass

class UsuarioVerificado(User):
    pass

class Moderador(User):
    pass

class Profile (models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic=models.ImageField(default='default.png', upload_to='profile_pics')
    facebook_url= models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    following = models.ManyToManyField(User,related_name = 'following', blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now = True)

    def profiles_posts(self):
    	return self.post_set.all()

    def __str__(self):
       return str(self.user.username)

    class Meta:
     	ordering = ('-created',)

class Post(models.Model):
	author = models.ForeignKey(Profile, on_delete = models.CASCADE)
	body = models.TextField()
	updated = models.DateTimeField(auto_now =True)
	created = models.DateTimeField(auto_now =True)

	def __str__(self):
		return str(self.body)[:30]

	class Meta:
		ordering = ('-created',)
