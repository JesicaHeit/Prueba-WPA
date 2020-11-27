from django.contrib import admin
from .models import Comment, Reports, Receta
from .forms import RecetasForm
from django.shortcuts import render, redirect, get_object_or_404

admin.site.register(Comment)
#admin.site.register(Reports)
#admin.site.register(Receta)


class RecetaAdmin(admin.ModelAdmin):
	actions = ['bloquear_receta','activar_receta']
	list_display =['title', 'author', 'state', 'categoria']
	list_filter = ['title', 'author', 'state','categoria']

	def bloquear_receta(modeladmin,request,queryset):
		queryset.update(state = 2)
	bloquear_receta.description = "Bloquear receta"

	def activar_receta(modeladmin,request,queryset):
		queryset.update(state = 1)
	activar_receta.description = "Activar receta"


admin.site.register(Receta,RecetaAdmin)


class ReportAdmin(admin.ModelAdmin):
	actions = ['bloquear_receta','activar_receta', 'ver_contenido']
	list_display = ['report', 'informed', 'text']
	list_filter = ['report', 'informed']

	def bloquear_receta(self,request,queryset):
		for repo in queryset:
			receta = Receta.objects.filter(title=repo.report, author = repo.report.author).order_by("-published_date")
			receta.update(state=2)
	bloquear_receta.description = "Bloquear receta"

	def activar_receta(self,request,queryset):
		for repo in queryset:
			receta = Receta.objects.filter(title=repo.report, author = repo.report.author).order_by("-published_date")
			receta.update(state=1)
	activar_receta.description = "Activar receta"

	def ver_contenido(self,request,queryset):
		recetas= []
		for repo in queryset:
			receta = Receta.objects.filter(title=repo.report, author = repo.report.author).order_by("-published_date")
			recetas.extend(list(receta))
		return render(request, 'recetas/post_detail_admin.html', {'recetas': recetas})	

	ver_contenido.description = "Ver Contenido"

admin.site.register(Reports,ReportAdmin)


# Register your models here.

	