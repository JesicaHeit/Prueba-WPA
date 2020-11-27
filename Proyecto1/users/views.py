from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse, reverse_lazy
from django.views import generic
from .tokens import account_activation_token
from .forms import CustomUserForm
from django.views.generic import DetailView
from .models import Profile
from django.apps import apps
modelReceta = apps.get_model('recetas', 'Receta')
from django.utils import timezone
from django.template import Context, Template
from django.views.generic import ListView, DetailView

def register(request):
   # if request.method == 'GET':
   #     return render(request, 'users/register.html')
    # Creamos el formulario de autenticación vacío
    form = CustomUserForm()
    if  request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CustomUserForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save(commit= False)
            user.is_active = False
            user.save()
            Profile.objects.create(user=user)
            uidb64= urlsafe_base64_encode(force_bytes(user.pk)) # crea el token encodeado

            domain = get_current_site(request).domain
            link= reverse('activate', kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)}) # arma el link de activacion

            activate_url = domain+link # le agrega el dominio al link

            mail_subject = 'Activa tu cuenta' 

            message = 'Hola '+ user.username + \
                ' Verifica tu cuenta con el siguiente link:\n' + activate_url

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
            mail_subject, message, to=[to_email]
            )
            email.send(fail_silently=False)

            return redirect('/pantalla_intermedia')#('/login'+'?message='+'Revisa tu correo para activar la cuenta')
        else:
            form = CustomUserForm(request.POST)
        # Si llegamos al final renderizamos el formulario
    return render(request, "registration/register.html", {'form': form})
             
    # Si existe el usuario
    if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/pantalla_intermedia')

    # Si queremos borramos los campos de ayuda
  
  # form.fields['username'].help_text = None
  #  form.fields['password1'].help_text = None
  #  form.fields['password2'].help_text = None

def activate(request, uidb64=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not account_activation_token.check_token(user,token):
            return HttpResponseRedirect('/login'+'?message='+'El usuario ya esta activado')

        if user.is_active:
            return HttpResponseRedirect('/login')
        user.is_active=True
        user.save()   

        # messages.success(request,'La cuenta se activo correctamente')
        return HttpResponseRedirect('/login')

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

   
    return HttpResponseRedirect('/login')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


def show_profile(request,pk):
    profile=get_object_or_404(Profile, user__id=pk)
    name = profile.user
    receta = modelReceta.objects.filter(author=name, published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'registration/user_profile.html',{'page_user': profile, 'receta': receta})

class ShowProfilePageView (DetailView):

	model= Profile
	template_name='registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)

		page_user=get_object_or_404(Profile, user__id=self.kwargs['pk']) #Obtener perfil
		
		my_profile = Profile.objects.get(user=self.request.user) #Usuario

		name =page_user.user

		receta = modelReceta.objects.filter(author=name, published_date__lte=timezone.now()).order_by('published_date')

		view_profile = self.get_object()
		if view_profile.user in my_profile.following.all():
			follow = True
		else:
			follow = False

		context["follow"] = follow

		context["page_user"]= page_user
		context["my_profile"] = my_profile

		context["name"]		= name
		context["receta"]	= receta
		return context

	def get_object(self, **kwargs):
		view_profile = Profile.objects.get( user__id=self.kwargs['pk'])
		return view_profile

class EditPofilePageView (generic.UpdateView):
    model=Profile
    template_name = 'registration/edit_profile.html'
    fields = [ 'bio', 'profile_pic', 'facebook_url', 'twitter_url', 'pinterest_url', 'website_url',]
    success_url = reverse_lazy('home')

class UserEditView (generic.UpdateView):
    form_class=UserChangeForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')
    def get_object(self):
        return self.request.user

def follow_unfollow_profile(request):
    if request.method== "POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect('profile/<int:pk>')


class ProfileListView(ListView):
    model = Profile
    template_name ='main.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

