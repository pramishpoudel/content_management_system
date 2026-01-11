from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('register/',views.register_view,name='register_view'),
    path('record/<int:pk>/',views.customer_record,name='customer_record'), 
    path('delete_record/<int:pk>/',views.delete_record,name='delete_record'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>/',views.update_record,name='update_record'),
    ]