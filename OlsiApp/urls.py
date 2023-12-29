
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('business', views.business, name='business'),
    path('products', views.products, name='products'),
    path('agriculture', views.agriculture, name='agriculture'),
    path('manufacture', views.manufacture, name='manufacture'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
    path('galery', views.galery, name='galery'),
    path('login', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('underconstrunction', views.underconstrunction, name='underconstrunction'),
    path('viewproduct/<int:id>', views.viewproduct, name='viewproduct'),
]
