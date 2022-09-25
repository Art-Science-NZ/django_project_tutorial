from django.views.generic import ListView
 
# Importing my model classes
from .models import Article
# # Create your views here.
class HomeView(ListView):
    model = Article
    template_name = "blog_index.html"
    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        return {"articles": articles}