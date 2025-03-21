"""
URL configuration for shopping_cart project.

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
from django.urls import path, include
from .views import CartItemViews, ItemViews, CartViews, Cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', CartItemViews.as_view()),
    path('get/', ItemViews.as_view()),
    path('update/<int:id>/', CartViews.as_view()),
    path('delete/<int:id>/', Cart.as_view())
]
