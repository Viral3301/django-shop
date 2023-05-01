from django.urls import path,include
from .views import HomeView,CatalogView
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('jet_ski/',CatalogView.as_view(), name='catalog'),
]
