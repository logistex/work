from django.contrib.auth import views as auth_views  # 장고에 내장된 인증 기능을 활용하기 위하여
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),  # url()는 장고 1.x 방식
    path('drafts/', views.post_draft_list, name='post_draft_list'),  # path()는 장고 2.x 방식
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('login/', auth_views.LoginView.as_view(), name='login'),       # !!!
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    # !!!
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
]