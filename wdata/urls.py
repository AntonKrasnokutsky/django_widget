from django.urls import path
from . import views

app_name = 'selectdatetime'
urlpatterns = [
    # Главная страница
    path('',
         views.SelectDateTimeViews.as_view(),
         name='select'),
]