from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

appname = 'orders'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('', include('blogs.urls', namespace="blogs")),
    path('', include('product.urls', namespace="product")),
    path('', include('users.urls', namespace="users")),
    path('', include('orders.urls', namespace="orders")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
