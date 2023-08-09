from django.urls import path
from . import views

app_name = 'dashbourd'

urlpatterns = [
    path('',views.index,name='index'),
]
