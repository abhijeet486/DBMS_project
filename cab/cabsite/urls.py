from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.login,name='login'),
    path('booking',views.booking,name='booking'),
    path('customer',views.customer,name='customer'),
    path('driver',views.driver,name='driver'),
    path('payment',views.payment,name='payment'),
    path('login/',views.loginaccess,name="loginaccess"),
    path('previoustrips',views.previoustrips,name='previoustrips'),
    path('editpassenger',views.editpassenger,name='editpassenger'),
    path('editdriver',views.edit_driver,name='edit_driver'),
    path('manage',views.Mangevehicles,name='Mangevehicles'),
    # path('cabsite/',include('cabsite.urls'))
]