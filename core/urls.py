from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_me, name='about_me'),
    path('all-articles/', views.articles, name='all_articles'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('article/<slug:slug>/', views.open_article, name='this_article'),
    path('portfolio/<slug:slug>/', views.project_details, name='this_project'),
]