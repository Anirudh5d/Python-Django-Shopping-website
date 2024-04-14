"""
URL configuration for mulweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from myapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),   
    path('order_digital_appliances/', views.order_digital_appliances, name='order_digital_appliances'),  
    path('order_clothes/', views.order_clothes, name='order_clothes'),  
    path('order_groceries/', views.order_groceries, name='order_groceries'),  
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
