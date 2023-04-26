from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class HomeView(ListView):
    model = Product
    paginate_by = 9
    template_name = 'home.html'