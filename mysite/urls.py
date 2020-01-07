from django.contrib import admin
from django.urls import path, include
# from . import views                           # 이전 코드
from .views import HomeView                     # 신규 코드 !!! (.views.HomeView 작성 필요)

urlpatterns = [
    # path('', views.homepage, name='home'),    # 이전 코드
    path('', HomeView.as_view(), name='home'),  # 신규 코드 !!!
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
]
