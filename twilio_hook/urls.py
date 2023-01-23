from django.urls import path

from . import views

urlpatterns = [
    path("hi/", views.index, name="index"),
    path("callTo/<str:s>/<slug:l>/", views.high_response, name="high-response"),
    path("response/<slug:l>/<str:s>/", views.handle_response, name="handle-response"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="loginTemp"),
    path("query/", views.search, name="query"),
    path("msg/", views.msg, name="msg"),
    # path('get_query_history/',views.get_query_history,name='get_query_history'),
]
