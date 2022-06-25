"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'^user/',include('apps.users.urls',namespace='user')),   # 用户模块  namespace = //反向解析
#     path(r'^cart/',include('apps.cart.urls',namespace='cart')),   # 购物车模块
#     path(r'^order/',include('apps.order.urls',namespace='order')),   # 订单模块
#     path(r'^',include('apps.goods.urls',namespace='goods')),   # 商品模块
# ]

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 富文本编辑器注册
    re_path('tinymce/', include('tinymce.urls')),
    # 全文检索框架
    # re_path('search/', include('haystack.urls')),

    # 注册自定义应用的路由
    re_path('user/', include(('apps.users.urls', 'user'), namespace='user')),
    re_path('cart/', include(('apps.cart.urls', 'cart'), namespace='cart')),
    re_path('order/', include(('apps.order.urls', 'order'), namespace='order')),
    re_path(r'^', include(('apps.goods.urls', 'goods'), namespace='goods')),
]