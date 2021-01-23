from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('maktab_haqida', views.about, name='maktab_haqida'),
    path('tadbirlar', views.blog, name='tadbirlar'),
    path('aloqa', views.contact, name='aloqa'),
    path('darslar', views.courses, name='darslar'),
    path('oqituvchi', views.teacher, name='oqituvchi'),
    path('rasmlar', views.rasm, name='photolar'),
    path('kitoblar', views.book, name='book'),
    path('>', views.elbook, name='elbook'),
]