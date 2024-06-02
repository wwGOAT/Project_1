from django.db import models
from django.contrib.auth.models import User

class CategoryProductsModel(models.Model):
    name = models.CharField(max_length=129)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "CategoryProduct"
        verbose_name_plural = "CategoryProducts"
        
class ManufactureProductsModel(models.Model):
    name = models.CharField(max_length=129)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ManufactureProduct"
        verbose_name_plural = "ManufactureProducts"
        
        
class ColorProducstModel(models.Model):
    name = models.CharField(max_length=129)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ColorProduct"
        verbose_name_plural = "ColorProducts"
    
class ProductTagModel(models.Model):
    name = models.CharField(max_length=129)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ProductTag"
        verbose_name_plural = "ProductTags"
    
    
class ProducuctsChoisSizeModel(models.Model):
    name = models.CharField(max_length=129)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "ProducuctsChoisSize"
        verbose_name_plural = "ProducuctsChoisSizes"
        
    
# Create your models here.
class ProducstModel(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="product")
    image2 = models.ImageField(upload_to="product" ,null=True)
    reyting = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dicount = models.IntegerField(null=True)
    description = models.TextField()
    count = models.IntegerField()
    
    
    code = models.CharField(max_length=8,null=True, blank=True)
    
    category = models.ManyToManyField(CategoryProductsModel, related_name="products")
    manufacture = models.OneToOneField(ManufactureProductsModel, on_delete=models.CASCADE, related_name="products")
    color = models.ManyToManyField(ColorProducstModel, related_name="products")
    tags = models.ManyToManyField(ProductTagModel, related_name="products")
    sizes = models.ManyToManyField(ProducuctsChoisSizeModel, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def count_stock(self):
        return self.count != 0        
    
    def is_discount(self):
        return self.dicount != 0
    
    def cheack_count(self):
        return self.count != 0
    
    def get_math_price(self):
        if self.is_discount():
            return self.price - self.price * self.dicount / 100
        
        
    def get_relete_function(self):
        return ProducstModel.objects.filter(category=1).exclude(pk=self.pk)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
        


class CommentsProductsModle(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(ProducstModel, on_delete=models.CASCADE, related_name='comments')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.comment} - {self.user} - {self.products}"
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'