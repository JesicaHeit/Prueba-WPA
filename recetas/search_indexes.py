from haystack import indexes
from .models import Receta

class RecetaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    ingredients = indexes.CharField(model_attr='ingredients')
    created_date = indexes.DateTimeField(model_attr='created_date')
    author = indexes.CharField(model_attr='author')
    imagen = indexes.CharField(model_attr='imagen')

    def get_model(self):
        return Receta

    def index_queryset(self, using=None):
        """Queremos que se indexen todas las noticias que tengan archivada=False"""
        return self.get_model().objects.filter()

