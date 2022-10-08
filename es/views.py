from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy

from django.contrib import  messages

from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import EsPost
from .forms import EsForm


class EsListView(LoginRequiredMixin, ListView):
    template_name = 'es/es_list.html'
    context_object_name = 'es_list'
    login_url = '/account/login/'

    def get_queryset(self):
        return EsPost.objects.filter(user=self.request.user).order_by('posted_at')
    
class EsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'es/es_create.html'
    model = EsPost
    success_url = reverse_lazy('es:es_list')
    fields = ['title', 'content']
    login_url = '/account/login/'

    def form_valid(self, form):
        esData = form.save(commit=False)
        esData.user = self.request.user
        esData.save()

        return super().form_valid(form)

class EsDeleteView(DeleteView):
    model = EsPost
    template_name = 'es/es_delete.html'
    success_url = reverse_lazy('es:es_list')
    login_url = '/account/login/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class EsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'es/es_update.html'
    model = EsPost
    form_class = EsForm
    #fields = ['title', 'content']
    login_url = '/account/login/'
    success_url = reverse_lazy('es:es_list')

    def form_valid(self, form):
        esData = form.save(commit=False)
        esData.user = self.request.user
        esData.save()
        return super().form_valid(form)