from django.urls import path
from .views import actress_list,reset_admin

urlpatterns = [
    path('actresses/', actress_list, name='actress_list'),   
    path('reset-admin/', reset_admin),
]