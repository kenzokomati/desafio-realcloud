from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_record/<int:pk>', views.get_record, name='get_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
