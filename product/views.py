from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import ProducstModel, ProductTagModel, ProducuctsChoisSizeModel, ColorProducstModel, ManufactureProductsModel, CategoryProductsModel, CommentsProductsModle
# Create your views here.
class ProductsView(ListView):
    template_name = "product-list.html"
    context_object_name = "products"
    paginate_by = 2
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = ProducstModel.objects.all().order_by('-pk')
        cat = self.request.GET.get('cate')
        manu = self.request.GET.get('manu')
        color = self.request.GET.get('color')
        tag = self.request.GET.get('tag')
        if cat:
            qs = qs.filter(category=cat)
        if manu:
            qs = qs.filter(manufacture=manu)
        if color:
            qs = qs.filter(color=color)
            
        if tag:
            qs = qs.filter(tags=tag)
            
        return qs
    
    
    def get_context_data(self,  object_list=None  ,**kwargs):
        conetxt = super().get_context_data(**kwargs)
        conetxt.update({
            "tags": ProductTagModel.objects.all(),
            "color": ColorProducstModel.objects.all(),
            "size": ProducuctsChoisSizeModel.objects.all(),
            "manufacture": ManufactureProductsModel.objects.all(),
            "category": CategoryProductsModel.objects.all()
        })
        return conetxt
    
    


class ProductsDetailView(DetailView):
    template_name = "product-detail.html"
    model = ProducstModel
    context_object_name = "product_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context.update({
            "categories": product.category.all(),  
            "tags": product.tags.all(), 
            "sizes": product.sizes.all(), 
            "color": product.color.all(), 
            "related_products": product.get_relete_function()
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
    
        comment = request.POST.get("comment")
    
        if comment:
            CommentsProductsModle.objects.create(comment= comment, user= request.user, products= self.object)
            return render(request, self.template_name, self.get_context_data())