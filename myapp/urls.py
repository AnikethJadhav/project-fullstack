from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('records', views.list_records, name='records'),
  path('save-record', views.save_record, name='save-record')
]