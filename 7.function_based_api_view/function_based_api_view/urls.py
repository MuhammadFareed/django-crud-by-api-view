from django.contrib import admin
from django.urls import path
from api.views import say_hello, say_hello_post_req

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello/', say_hello),
    path('say_hello_by_post_req/', say_hello_post_req),
]
