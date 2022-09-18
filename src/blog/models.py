from django.db import models
 
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
 
# List of tuples for my status field
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Article(models.Model):
    title = models.CharField(max_length = 120)
    header_image = models.CharField(max_length = 2040, null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='article_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category =  models.CharField(max_length=255, default="None")
    content = RichTextField(blank=True, null=True)
 
    # This orders the data by the date the article was created 
    class Meta:
        ordering = ['-created_on']
 
    def __str__(self): # I add this to make the objects in the admin have a clean name
        return self.title + " | " + str(self.author)
 
    # Need to redirect from form
    def get_absolute_url(self):
        return reverse("article-detail", kwargs = {"slug": self.slug})