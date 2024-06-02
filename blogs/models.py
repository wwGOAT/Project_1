from django.db import models


class BlogTag(models.Model):
    name = models.CharField(max_length=129)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "BlogTag"
        verbose_name_plural = "BlogsTags"
# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=228)
    image = models.ImageField(upload_to="blog-author")
    about = models.TextField()
    position = models.CharField(max_length=128)
    prefeesion = models.CharField(max_length=100)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def  __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        
        
        
class BlogcategoryModle(models.Model):
    name = models.CharField(max_length=229)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def  __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "BlogCategory"
        verbose_name_plural = "BlogCategorys"
        
class BlogModel(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="blog-image")
    content = models.TextField()
    category = models.ManyToManyField(BlogcategoryModle, related_name='blogs')
    tags = models.ManyToManyField(BlogTag, related_name='blogs')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name="blogs")
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"