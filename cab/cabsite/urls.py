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
    path('logout/',views.logout,name="logout"),
    path('previoustrips',views.previoustrips,name='previoustrips'),
    path('booking/request',views.bookingrequest,name='bookingrequest'),
    path('edit/passenger',views.editpassenger,name='editpassenger'),
    path('edit/driver',views.editdriver,name='editdriver'),
    path('edit/details',views.savechanges,name="savechanges"),
    path('manage',views.Mangevehicles,name='Mangevehicles'),
    # path('cabsite/',include('cabsite.urls'))
]