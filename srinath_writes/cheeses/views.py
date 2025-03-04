from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cheese
# Create your views here.

class CheeseListView(ListView):
    model  = Cheese


class CheeseCreateView(LoginRequiredMixin,CreateView):
    model = Cheese
    fields = [
            'name',
            'description',
            'firmness',
            'country_of_origin',
            ]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CheeseDetailView(DetailView):
    model = Cheese

    def Post(self, request):
        pass




