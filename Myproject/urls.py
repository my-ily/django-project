"""
URL configuration for Myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mobile import views
from django.conf import settings
from django.conf.urls.static import static
from converter import views as p1
from cryptcon import views as p2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/',views.Welcome),
    path('getdata/',views.getdata),
  path('datasend/<str:name>/', views.datasend),
  path('add/<int:x>/<int:y>', views.add)
  ,path('runindex/',views.runindex)
  ,path('',views.landpage ,name='landpage')
  ,path('about/',views.about,name='about')
    ,path('blog/',views.blog,name='blog')
     ,path('phonemenu/',views.phonemenu,name='phonemenu')
       ,
       path('invoice/',views.invoice,name="invoice"),
       path('details/',views.Datils,name="details"),
       path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
       path('Checkout/',views.Checkout,name='Checkout'),
      path('auth_login/', views.auth_login, name='auth_login'),

       path('auth_reg/',views.auth_reg,name='auth_reg'),
       path('get_remote/',views.get_remote,name='get_remote'),
       path('remoteProduct/',views.get_remoteProduct,name='get_remoteProduct'),
       path('convert_currancy/',p1.convert_currancy,name='convert_currancy')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
