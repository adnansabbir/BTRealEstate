from django.urls import path
from listings import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]