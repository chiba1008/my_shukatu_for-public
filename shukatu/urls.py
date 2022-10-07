from django.urls import path
from . import views

app_name = 'shukatu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home', views.HomeView.as_view(), name='home'),
    path('company_list/', views.CompanyListView.as_view(), name='company_list'),
    path('company_detail/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('register_company/', views.CreateCompanyView.as_view(), name='register_company'),
    path('register_success/', views.CreateSuccessView.as_view(), name='register_done'),
    path('company/<int:pk>/delete', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('company/<int:pk>/update', views.CompanyUpdateView.as_view(), name='company_update'),
]