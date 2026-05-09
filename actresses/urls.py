from django.urls import path
from .views import actress_list

urlpatterns = [
    path('actresses/', actress_list, name='actress_list'),
]