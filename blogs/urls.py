from django.urls import path
from blogs.views import BlogView

app_name = "blogs"

urlpatterns = [
       path('blogs/', BlogView.as_view(), name='blogs'),
]