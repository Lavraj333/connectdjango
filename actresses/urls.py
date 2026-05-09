from django.urls import path
from .views import actress_list,check_admin,reset_admin

urlpatterns = [
    path('actresses/', actress_list, name='actress_list'),   
      path('check-admin/', check_admin),
    path('reset-admin/', reset_admin),
]