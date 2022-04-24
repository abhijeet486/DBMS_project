from xml.etree.ElementInclude import include
from django.urls import path

from . import views
from django.db import connection
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.login,name='login'),
    path('booking',views.booking,name='booking'),
    path('customer',views.customer,name='customer'),
    path('driver',views.driver,name='driver'),
    path('payment',views.payment,name='payment'),
    path('loginaccess',views.loginaccess,name='loginaccess'),
    path('previoustrips',views.previoustrips,name='previoustrips'),
    path('editpassenger',views.editpassenger,name='editpassenger'),
    path('editdriver',views.edit_driver,name='edit_driver'),
    # path('cabsite/',include('cabsite.urls'))
]