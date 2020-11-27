from django.contrib import admin
from users.models import Profile, UsuarioGeneral, UsuarioVerificado
# Register your models here.

admin.site.register(Profile)
admin.site.register(UsuarioGeneral)
admin.site.register(UsuarioVerificado)