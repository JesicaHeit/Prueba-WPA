from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Receta(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    choices_state=(
        (1,'Activa'),
        (2,'Bloqueada'),
        )
    state= models.PositiveSmallIntegerField(choices=choices_state,blank=False, null=True)
    ingredients = RichTextField(config_name='nombre_referencia',verbose_name="Ingredientes",default='')
    text = RichTextField(config_name='default',verbose_name="Receta")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes= models.ManyToManyField('auth.User', related_name='receta_post')
    imagen = models.ImageField(upload_to="foto_receta")
    categorias = (
        (0,'Entradas'),
        (1,'Carnes'),
        (2,'Pastas'),
        (3,'Veggie'),
        (4,'Sandwiches'),
        (5,'Sopas'),
        (6,'Postres'),
    )
    categoria = models.PositiveSmallIntegerField(choices=categorias, blank=False, null=False)

    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=20)

class Comment(models.Model):
    post = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Reports(models.Model):
    
    choices_report=(
        (1,'Receta inválida'),
        (2,'Spam'),
        (3,'Otro'),
    )
    report = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='reports', null = True)
    informer = models.CharField(max_length=200)
    informed = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null = True)
    options = models.PositiveSmallIntegerField(choices=choices_report,blank=False, null=False)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_report = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Reports'
        verbose_name_plural = 'Reports'