from django.contrib import admin
from django.urls import path, include
from . import views                           # !!!

urlpatterns = [
    path('', views.homepage, name='home'),    # !!!
    path('admin/', admin.site.urls),
    # path('accounts/login/', views.login, name='login'),
    # path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'}),
    # 'accounts/'라는 urlpattern은 'django.contrib.auth.urls'에게 전달
    path('accounts/', include('django.contrib.auth.urls')),  # !!!
    path('blog/', include('blog.urls')),
    # path('', include('blog.urls')),
]
