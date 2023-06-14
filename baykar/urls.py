"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Programın sitemapini oluşturma yolların belirlenmesi.
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('ekle/',views.ekleme,name='ekle'),
    path('search/', views.search_view, name='search'),
    path('filter/', views.filter_results, name='filter_results'),
    path('show/', views.filter_results, name='show_all'),
    path('delete/<int:id>/', views.delete_iha, name='delete_iha'),
    path('duzenle/<int:id>/', views.duzenle_iha, name='duzenle_iha'),



 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
