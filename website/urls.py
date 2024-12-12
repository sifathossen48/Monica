from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/details/<int:article_id>/', views.BlogDetailView.as_view(), name='blog-details')
]