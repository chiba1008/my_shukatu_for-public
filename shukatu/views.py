from re import L
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy

from django.contrib import  messages

from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ShukatuPost
from .forms import ContactForm, RegisterCompanyForm


class IndexView(TemplateView):
    template_name = 'shukatu/index.html'


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'shukatu/home.html'
    context_object_name = 'orderby_posted_records'
    paginate_by = 7
    login_url = '/account/login/'

    def get_queryset(self):
        return ShukatuPost.objects.filter(user=self.request.user).order_by('-posted_at')

class CompanyListView(LoginRequiredMixin, ListView):
    template_name = 'shukatu/company_list.html'
    context_object_name = 'orderby_title_records'
    login_url = '/account/login/'

    def get_queryset(self):
        return ShukatuPost.objects.filter(user=self.request.user).order_by('title')
    
class CompanyDetailView(DetailView):
    template_name = 'shukatu/company_detail.html'
    model = ShukatuPost
    login_url = '/account/login/'


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = ShukatuPost
    from_class = RegisterCompanyForm
    template_name = 'shukatu/register_company.html'
    success_url = reverse_lazy('shukatu:register_done')
    fields = ['title', 'myPageId', 'myPageUrl','category']
    login_url = '/account/login/'


    def form_valid(self, form):
        companyData = form.save(commit=False)
        companyData.user = self.request.user
        companyData.save()

        return super().form_valid(form)



class CreateSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'shukatu/register_success.html'
    login_url = '/account/login/'


class CompanyDeleteView(DeleteView):
    model = ShukatuPost
    template_name = 'shukatu/company_delete.html'
    success_url = reverse_lazy('shukatu:company_list')
    login_url = '/account/login/'


    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'shukatu/company_update.html'
    model = ShukatuPost
    fields = ['title', 'myPageId', 'myPageUrl','category']
    login_url = '/account/login/'

    def get_success_url(self):
        return reverse_lazy('shukatu:company_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        companyData = form.save(commit=False)
        companyData.user = self.request.user
        companyData.save()
        return super().form_valid(form)

class ContactView(FormView):
    template_name = 'shukatu/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('shukatu:contact')


    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = 'お問い合わせ: {}'.format(title)

        message = '送信者名: {0}\nメールアドレス: {1}\nタイトル: {2}\nメッセージ: {3}'.format(name, email, title, message)

        from_email = 'myshukatucontact@gmail.com'
        to_list = ['myshukatucontact@gmail.com']

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,)

        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました')

        return super().form_valid(form)
