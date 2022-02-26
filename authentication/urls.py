from django.urls import URLPattern, path
from django.urls import path,include
from . import views
urlpatterns=[
     path('', include('djoser.urls.jwt')),
     path('signup/',views.UserCreationView.as_view(),name='sign_up'),
]