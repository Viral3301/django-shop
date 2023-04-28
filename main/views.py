from django.shortcuts import render
from django.views.generic import ListView
from .models import Accessories
# Create your views here.

class HomeView(ListView):
    model = Accessories
    paginate_by = 9
    template_name = 'home.html'

