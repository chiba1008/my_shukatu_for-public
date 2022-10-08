from readline import append_history_file
from django.urls import path
from . import views

app_name = 'es'

urlpatterns = [
    path('es_list', views.EsListView.as_view(), name='es_list'),
    path('es_create', views.EsCreateView.as_view(), name='es_create'),
    path('es/<int:pk>/delete', views.EsDeleteView.as_view(), name='es_delete'),
    path('es/<int:pk>/update', views.EsUpdateView.as_view(), name='es_update'),

]