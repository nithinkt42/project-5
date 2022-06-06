from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='india'),
    path('kerala/',views.kerala, name='kerala'),
    path('goa/',views.goa,name='goa'),
    path('rajasthan/',views.rajasthan,name='rajasthan'),
    path('kol/',views.kolkkatha,name='kol'),
    path('kashmir',views.KASHMIR,name='kashmir')
]