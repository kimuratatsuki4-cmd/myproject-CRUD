"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ルーティング（ブラウザから送られるHTTPリクエストに応じて、表示するページを指示）
    # 第二引数：views.pyのTopViewクラスを指定する。
    # 第三引数：指定したクラスに対するニックネームを指定する。
    path('admin/', admin.site.urls),
    path('',views.TopView.as_view(), name="top"),
    path('crud/',views.ProductListView.as_view(), name="list"),
    path('crud/new/',views.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>',views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>',views.ProductDeleteView.as_view(), name="delete"),
    path('login/',views.Loginview.as_view(), name="login"),
    path('logout/',views.Logoutview.as_view(), name="logout"),
]

if settings.DEBUG: #開発モードの場合のみ、画像ファイルを静的ファイルとして扱う
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)