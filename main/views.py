from django.shortcuts import render
from django.views.generic import ListView
from .models import Accessories,Vehicles,Category
# Create your views here.

class HomeView(ListView):
    model = Accessories
    template_name = 'home.html'



class CatalogView(ListView):
    model = Vehicles
    paginate_by = 12
    template_name = 'catalog.html'

