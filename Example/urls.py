from django.urls import path
from . import views
from .views import index, detail

urlpatterns = [
    path('',views.index, name= index),
    path('<int:question_id>/', views.detail, name=detail)
]