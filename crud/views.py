from django.shortcuts import render
from .models import Celular
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CelularList(ListView):
    model = Celular

class CelularView(DetailView):
    model = Celular

class CelularCreate(CreateView):
    model = Celular
    fields = ['serie', 'marca', 'modelo', 'so']
    success_url = reverse_lazy('celular_list')

class CelularUpdate(UpdateView):
    model = Celular
    fields = ['serie', 'marca', 'modelo', 'so']
    success_url = reverse_lazy('celular_list')

class CelularDelete(DeleteView):
    model = Celular
    success_url = reverse_lazy('celular_list')

