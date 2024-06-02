from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import BlogModel, BlogcategoryModle, BlogTag
# Create your views here.
class BlogView(ListView):
    paginate_by = 2    
    template_name = "blog-list-sidebar-left.html"
    context_object_name = "blogs"
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = BlogModel.objects.all().order_by('-pk')
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        
        if cat:
            qs = qs.filter(category=cat)
        if tag:
            qs = qs.filter(tags=tag)
            
        return qs
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update ({
            "category": BlogcategoryModle.objects.all(),
            "famous_blog": BlogModel.objects.all().order_by("-create_at")[::2],
            "tags": BlogTag.objects.all()
        })
        
        return context
    
    
    
