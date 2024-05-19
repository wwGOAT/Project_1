from django.urls import path

from pages.views import HomePageView, ContactPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),

]