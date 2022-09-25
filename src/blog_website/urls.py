from django.contrib import admin
from django.urls import path, include #Add in include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # This was added as the link to the the blog app urls
]