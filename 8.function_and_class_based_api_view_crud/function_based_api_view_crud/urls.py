from django.contrib import admin
from django.urls import path
# from api.views import student_api
from api.views import StudentAPI

# URLS for function based api_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student_api/', student_api),
#     path('student_api/<int:pk>', student_api),
# ]



# URLS for class based api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', StudentAPI.as_view()),
    path('student_api/<int:pk>', StudentAPI.as_view()),
]
