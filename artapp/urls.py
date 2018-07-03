from django.conf.urls import url
from artapp import views

urlpatterns = [
    # 声明主页的请求
    url(r'^$', views.index),
]
